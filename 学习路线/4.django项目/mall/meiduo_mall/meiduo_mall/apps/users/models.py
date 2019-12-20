from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from itsdangerous import TimedJSONWebSignatureSerializer as TJWS,BadData
from .import constants
from meiduo_mall.utils.models import BaseModel

# Create your models here.
class User(AbstractUser):
    """自定义用户模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    # 因为我们需要在users表中添加一个邮箱是否激活的字段
    email_active = models.BooleanField(default=False,verbose_name='邮箱验证状态')
    # 为用户添加一个默认地址
    default_address = models.ForeignKey('Address',related_name='users',null=True,blank=True,
                                        on_delete=models.SET_NULL,verbose_name='默认地址')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


    def generate_verify_email_url(self):
        """生成激活邮件链接"""

        # 1.创建用来签名/加密的序列化器.需要使用settings/dev里面的SECRET_KEY
        # 参数: 盐 过期时间
        serializer = TJWS(settings.SECRET_KEY,constants.VERIFY_EMAIL_TOKEN_EXPIRES)

        # 2.定义要加密的用户数据
        data = {'id':self.id,'username':self.username}

        # 3.加密: 因为dumps之后是bytes类型数据,解码之后才是str类型
        token = serializer.dumps(data).decode()

        # 4.拼接验证链接url
        verify_url = 'http://www.meiduo.site:8080/success_verify_email.html?token=' + token

        return verify_url

    @staticmethod
    def check_verify_email_token(token):
        """验证token并提取user"""

        # 注意:下面这里并没有使用self,所以我们可以将这个方法定义成静态方法或者类方法.
        # 但是,如果定义成类方法,会自动传递一个cls的参数.而下面又没有使用过cls,所以显得多此一举,直接使用静态方法即可
        # 之所以不使用实例方法,是因为在views里面本来就是获取user,你这边传个self又何必获取user?
        # 自相矛盾了.就是需要在没有传递user实例对象的情况下获取user.综合考虑,这里需要使用静态方法




        # 1.创建用来签名/加密的序列化器.需要使用settings/dev里面的SECRET_KEY
        serializer = TJWS(settings.SECRET_KEY,constants.VERIFY_EMAIL_TOKEN_EXPIRES)

        # 2.把用户数据恢复到加密前的状态
        try:
            data = serializer.loads(token)
        except BadData:  # 如果解密失败:因为有过期时间,所以会存在这种解密失败的可能
            return None
        else:
            # 解密成功
            user_id = data.get('id')
            username = data.get('username')
            # 数据库获取对应的用户进行校验.能获取到才算校验成功
            try:
                user = User.objects.get(id=user_id,username=username)
            except User.DoesNotExist:
                return None
            else:
                return user


class Address(BaseModel):
    """
	用户地址:只能放在User的后面.一的模型写在前面,多的写在后面
	"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='用户')
    title = models.CharField(max_length=20, verbose_name='地址名称')
    receiver = models.CharField(max_length=20, verbose_name='收货人')

    # 'areas.Area':写法等价于 areas.models.Area. DRF里面会自动去加一个models这么写是省略了导包的操作.全部交给DRF框架去执行了

    province = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='province_addresses',
                                 verbose_name='省')

    city = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='city_addresses', verbose_name='市')
    district = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='district_addresses',
                                 verbose_name='区')

    place = models.CharField(max_length=50, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    tel = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name='固定电话')
    email = models.CharField(max_length=30, null=True, blank=True, default='', verbose_name='电子邮箱')
    is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_address'
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name
        ordering = ['-update_time']








"""
实际上django已经给我们写好了users模块了,只是他这里没有手机号这一个功能,所以需要我们自定义users,添加手机号,
然后直接继承django的AbstractUser类即可.

django框架默认有邮箱字段,但是没有邮箱是否校验成功的字段,所以我们自己添加


为什么中国需要手机号?
因为手机号可以进行用户数据的收集,然后进行分析.简单粗暴的方式就是电话骚扰.是很值钱的数据资源
"""