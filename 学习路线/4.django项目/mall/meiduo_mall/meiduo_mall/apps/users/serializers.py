import re

from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import User, Address
from celery_tasks.email.tasks import send_verify_email
from goods.models import SKU


# 6.用户浏览记录
class UserBroweHistorySerializer(serializers.Serializer):
	"""反序列化用户浏览记录"""
	sku_id = serializers.IntegerField(label='商品sku编码', min_value=1)

	def validate_sku_id(self, value):
		"""单独对sku_id进行额外校验"""
		try:
			sku = SKU.objects.get(id=value)
		except SKU.DoesNotExist:
			raise serializers.ValidationError('SKU id 不存在')
		# 能走到这里,说明商品存在,验证没有问题
		return value

	def create(self, validated_data):
		"""重写此方法,把浏览记录存储到redis中而不是存储到mysql"""
		# 注意:直接去redis中进行查询即可验证
		# 获取用户信息.动态拼接.当做redis数据的key
		user_id = self.context.get('request').user.id


		# 读取验证后的sku_id
		sku_id = validated_data.get('sku_id')


		# 创建redis连接对象
		redis_conn = get_redis_connection('history')
		# 创建管道  三个连接数据库一起执行一次
		pl = redis_conn.pipeline()

		# 去重					key		0 表示不能有重复数据   value
		pl.lrem('history_%s' % user_id, 0, sku_id)
		# 添加					key      value
		pl.lpush('history_%s' % user_id, sku_id)
		# 截取最前面的5个元素		key    0    4
		pl.ltrim('history_%s' % user_id, 0, 4)

		# 执行
		pl.execute()
		# 返回
		return validated_data


# 5. 用户地址标题
class AddressTitleSerializer(serializers.ModelSerializer):
	"""地址标题"""

	class Meta:
		model = Address
		fields = ['title']  # 修改的是标题,所以这里只设置标题字段即可


# 4. 用户地址序列化器
class UserAddressSerializer(serializers.ModelSerializer):
	# 下面三个字段是为了序列化,输出给前端显示
	province = serializers.StringRelatedField(read_only=True)
	city = serializers.StringRelatedField(read_only=True)
	district = serializers.StringRelatedField(read_only=True)

	# 下面三个字段是为了反序列化,校验之后存储到数据库.
	# 外键都是设置为id.因为占用空间小.但是增加了查询次数
	# property_id = serializers.IntegerField(label='省ID',required=True)
	province_id = serializers.IntegerField(label='省ID', required=True)
	city_id = serializers.IntegerField(label='市ID', required=True)
	district_id = serializers.IntegerField(label='区ID', required=True)

	class Meta:
		model = Address  # 从这个表进行映射
		# 排除下面的字段进行序列化/反序列化.因为下面的字段没有必要进行校验存储到数据库.
		# 或者返回给前端进行展示
		exclude = ['user', 'is_deleted', 'create_time', 'update_time']

	def validate_mobile(self, value):
		"""验证输入的手机号"""
		if not re.match(r'^1[3-9]\d{9}$', value):
			return serializers.ValidationError('输入的手机号格式不正确')
		# 注意必须有返回值结束这个方法,否则永远也结束不掉程序
		return value

	def create(self, validated_data):
		"""保存地址:重写这个新增方法"""

		# 序列化器中获取user的方法:self.context['request'].user
		# request是当前视图的请求对象
		validated_data['user'] = self.context['request'].user

		# 创建并保存地址.中间就是为了地址hi关联这个用户
		# **validated_data:就是user=user.就是把上面刚刚包装好的字典拆开,
		# 拆成key=value的形式
		# 查询出来直接创建对象
		address = Address.objects.create(**validated_data)
		return address


# url(r'^email/$', views.EmailView.as_view())
# 3. 更新用户邮箱/发送邮件
class EmailSerializer(serializers.ModelSerializer):
	"""邮箱序列化器"""

	class Meta:
		model = User
		fields = ['id', 'email']
		extra_kwargs = {
			'email': {
				'required': True,  # 对指定字段进行额外设置.要求email字段必须传
			}
		}

	def update(self, instance, validated_data):
		"""重写此方法,原因:1.只保存邮箱 2.发送激活邮件"""
		user = instance
		user.email = validated_data.get('email')
		user.save()  # 这里是ORM中的保存

		# 1.生成邮箱里面的激活链接:但是下面这么写不严谨,邮件链接需要进行加密处理.使用面向对象实现生成激活链接
		# verify_url = 'this is test '
		verify_url = user.generate_verify_email_url()

		# 2.发激活邮件: 因为发邮件也是一个网络耗时操作,所以需要使用异步服务,所以下面需要delay延时操作
		send_verify_email.delay(user.email, verify_url)

		return user


# url(r'^user/$', views.UserDetailView.as_view()),
# 2. 用户详细信息
class UserDetailSerializer(serializers.ModelSerializer):
	"""用户详细信息:ModelSerializer可以自动去映射models里面的字段,"""

	class Meta:
		model = User
		fields = ['id', 'username', 'mobile', 'email', 'email_active']


# 1.创建用户
class CreateUserSerializer(serializers.ModelSerializer):
	"""注册序列化器"""

	# write_only=True :意思就是只能发序列化操作.
	# 确认密码,验证码,同意协议 这三个都是只进行反序列化中的数据校验/存储
	# 不需要序列化回传给前端显示
	password2 = serializers.CharField(label='确认密码', write_only=True)
	sms_code = serializers.CharField(label='短信验证码', write_only=True)
	allow = serializers.CharField(label='同意协议', write_only=True)
	token = serializers.CharField(label='token', read_only=True)

	# 序列化(输出/响应): id username mobile
	# 反序列化(输入/校验): 除id外所有字段全部需要进行校验

	class Meta:
		model = User  # 序列化器中的字段从哪一个模型类去映射

		# 校验的目的:为了数据的安全,因为如果不校验会有垃圾数据存储到数据库中.
		fields = ['id', 'username', 'mobile', 'password', 'password2', 'sms_code', 'allow', 'token']

		# 使用额外参数对password重新进行设置.
		# 更改验证时候的字段的长度
		extra_kwargs = {
			'username': {
				'min_length': 5,
				'max_length': 20,
				'error_messages': {  # 原来是我这里的error_messages写错了,少写了个s,记住.
					'min_length': '仅允许5-20个字符的用户名',
					'max_length': '仅允许5-20个字符的用户名',
				}
			},
			'password': {
				'write_only': True,  # 不需要输出,只是反序列化
				'min_length': 8,
				'max_length': 20,
				'error_messages': {
					'min_length': '仅允许8-20个字符的密码',
					'max_length': '仅允许8-20个字符的密码',
				}

			}
		}

	def validate_mobile(self, value):
		"""验证手机号"""
		if not re.match(r'^1[3-9]\d{9}$', value):
			raise serializers.ValidationError('手机号码格式不正确')
		# 校验通过返回手机号
		return value

	def validate_allow(self, value):
		"""校验用户是否同意协议"""
		if value != 'true':
			raise serializers.ValidationError('请同意用户协议')

		return value

	def validate(self, attrs):
		"""两个字段联合进行校验"""

		# 判断两次密码
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError('两次密码不一致')

		# 判断短信验证码

		# 1.建立redis数据库连接
		redis_conn = get_redis_connection('verify_codes')
		# 2.取出前端发来的手机号
		mobile = attrs['mobile']
		# 3.取出后端生成的短信验证码  注意这里的验证码需要进行解码
		real_sms_code = redis_conn.get('sms_%s' % mobile).decode()

		if real_sms_code is None:
			raise serializers.ValidationError('无效的短信验证码')

		# 如果前端的验证码和后台真正的验证码不同:
		if attrs['sms_code'] != real_sms_code:
			raise serializers.ValidationError('短信验证码错误')

		# 走到这里,说明校验成功,返回attrs参数

		return attrs

	def create(self, validated_data):
		"""
		创建用户
		:param validated_data: 用户信息的大字典
		:return: 返回一个新增用户user

		需要重写create方法,把不需要存储到数据库的字段排除
		"""

		# 移除数据库模型类中不存在的属性 验证码/确认密码/同意协议 这三个不需要存储到mysql
		del validated_data['password2']
		del validated_data['sms_code']
		del validated_data['allow']

		# 创建一个用户模型:创建的同时直接存储到数据库
		user = User.objects.create(**validated_data)
		# user = User(**validated_data)

		# 调用django中的认证系统加密密码,并且覆盖原有数据
		user.set_password(validated_data['password'])
		# user.set_password(user.password)

		# 保存到数据库
		user.save()

		# 'JWT_PAYLOAD_HANDLER':
		# 'rest_framework_jwt.utils.jwt_payload_handler',
		# __import__('rest_framework_jwt.utils.jwt_payload_handler')
		# token不要写在save前面,它不需要存到数据库中
		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 加载生成载荷函数
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 加载进行生成token的函数

		payload = jwt_payload_handler(user)  # 通过传用用户信息进行生成载荷
		token = jwt_encode_handler(payload)  # 根据载荷内部再拿到内部的header 再取到SECRET_KEY 进行HS256加密最后把加它们拼接为完整的token
		user.token = token

		return user
