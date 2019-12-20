from django_redis import get_redis_connection
from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView  # 导入新增视图
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.views import ObtainJSONWebToken

from . import serializers
from .models import User
from .serializers import CreateUserSerializer, UserBroweHistorySerializer
from . import constants
from goods.models import SKU
from goods.serializers import SKUSerializer
from carts.utils import merge_cart_cookie_to_redis


# Create your views here.
# 9.合并购物车
class UserAuthorizeView(ObtainJSONWebToken):
	"""重写JWT_token认证类,目的为了让购物车合并,搭上账号登录的顺风车"""

	def post(self, request, *args, **kwargs):
		response = super().post(request, *args, **kwargs)

		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
			user = serializer.object.get('user') or request.user

			merge_cart_cookie_to_redis(request, response, user)  # 必须注意:这里的实参的位置必须和函数的形参位置一致.否则会报错

		return response


# POST: browse_histories/
# 8.用户浏览历史记录
class UserBroweHistoryView(CreateAPIView):
	"""保存用户浏览记录"""
	# 指定序列化器进行数据的校验
	serializer_class = UserBroweHistorySerializer
	# 指定只有登录用户才能呢个访问此接口
	permission_classes = [IsAuthenticated]

	def get(self, request):
		"""查询用户浏览记录:就是在用户中心可以看到浏览记录"""
		# 获取user_id
		user_id = request.user.id
		# 获取链接到redis对象
		redis_conn = get_redis_connection('history')
		# 查询出redis中当前登录用户存储的浏览记录				存的时候截取了一下,索引乱了
		sku_ids = redis_conn.lrange('history_%s' % user_id, 0, -1)
		# 保存sku模型对象
		sku_list = []
		# 遍历sku_id:通过sku_id取出每一个sku模型对象
		for sku_id in sku_ids:
			sku = SKU.objects.get(id=sku_id)
			sku_list.append(sku)

		# 调用序列化器实现输出:序列化器序列化操作  传一个列表,告诉它是一个many=True
		serializer = SKUSerializer(sku_list, many=True)
		return Response(serializer.data)


# 7.用户地址新增/修改标题/修改地址/查询所有地址/删除
class AddressViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
	"""
	用户地址:视图集搭配mixin扩展实现
	"""
	# 1.指定序列化器
	serializer_class = serializers.UserAddressSerializer
	# 2.指定权限
	permission_classes = [IsAuthenticated]

	# POST /addresses/
	def create(self, request, *args, **kwargs):
		"""
		新增地址
		"""
		# 增加一个逻辑:对用户地址数量进行判断:是否超过20个
		count = request.user.addresses.count()
		if count >= constants.USER_ADDRESS_COUNTS_LIMIT:
			return Response({'message': '保存地址数据已达到上限'}, status=status.HTTP_400_BAD_REQUEST)  # 400:就是请求有问题

		return super(AddressViewSet, self).create(request, *args, **kwargs)

	# GET /addresses/
	def list(self, request, *args, **kwargs):
		"""用户地址列表数据"""

		# 1.指定查询集
		query_set = self.get_queryset()
		# 2.指定序列化器
		serializer = self.get_serializer(query_set, many=True)
		# 3.获取当前用户
		user = self.request.user  # 在视图中获取用户就是request
		return Response({
			'user_id': user.id,
			'default_address_id': user.default_address.id,  # 注意这里,少了个id就无法进行序列化操作了
			'limit': constants.USER_ADDRESS_COUNTS_LIMIT,
			'addresses': serializer.data,
		})

	def get_queryset(self):
		"""注意:这里必须返回用户地址,否则无法指定返回值,程序报错"""
		return self.request.user.addresses.filter(is_deleted=False)  # 把逻辑删除的进行过滤

	# delete /addresses/<pk>/
	# 注意单词拼写:是destroy,不是destory.注意o和r的顺序
	# def destory(self,request,*args,**kwargs):
	def destroy(self, request, *args, **kwargs):
		"""删除地址"""

		address = self.get_object()

		# 进行逻辑删除
		address.is_deleted = True
		address.save()

		# 删除成功,返回204状态码
		return Response(status=status.HTTP_204_NO_CONTENT)

	# put /addresses/pk/status/
	# 自定义put方法之后,需要使用装饰器进行设置,自定义方法才会生效
	@action(methods=['put'], detail=True)
	def status(self, request, pk=None):
		"""设置默认地址"""
		address = self.get_object()
		request.user.default_address = address
		request.user.save()
		return Response({'message': 'OK'}, status=status.HTTP_200_OK)

	# put /addresses/pk/title/
	# 需要请求体参数 title
	@action(methods=['put'], detail=True)
	def title(self, request, pk=None):
		""""""
		# 1.获取地址对象
		address = self.get_object()
		# 2.指定序列化器
		serializer = serializers.AddressTitleSerializer(instance=address, data=request.data)
		# 3.校验数据
		serializer.is_valid(raise_exception=True)
		serializer.save()
		# 最后肯定也是返回一个序列化后的数据,当然在这之前需要进行反序列化操作,校验数据,存储到数据库
		return Response(serializer.data)


# url(r'^emails/verification/$', views.VerifyEmailView.as_view()),
# 6.验证激活链接
class VerifyEmailView(APIView):
	"""验证激活链接"""

	def get(self, request):

		# 1.提取token
		token = request.query_params.get('token')
		if not token:
			return Response({'message': '缺少token'}, status=status.HTTP_400_BAD_REQUEST)

		# 2.验证token参数:提取user. 注意:这里本来就是获取user本身,如果传个self,那么你获取user又是在干啥?
		# 因为传了self就是user本身,那么就不会存在获取user这种操作
		user = User.check_verify_email_token(token)
		if not user:
			return Response({'message': 'token无效'}, status=status.HTTP_400_BAD_REQUEST)

		# 3.修改要验证用户邮箱的email_active字段为true,完成验证
		user.email_active = True
		user.save()

		return Response({'message': 'OK'})


# 5.更新邮箱
class EmailView(UpdateAPIView):
	"""更新邮箱:因为只是在原有用户模型对象中新增一个邮箱,这是更新,不是创建/新增"""

	# 1.指定序列化器
	serializer_class = serializers.EmailSerializer

	# 2.验证是否登录
	permission_classes = [IsAuthenticated]

	# 3.重写get_objects(self)方法,返回用户详情模型对象
	def get_object(self):
		return self.request.user


# 4.用户详细信息
class UserDetailView(RetrieveAPIView):
	"""用户详细信息:当然应该是retrieve单一视图了"""

	# 1.指定序列化器
	serializer_class = serializers.UserDetailSerializer

	# 2.用户身份认证:是否是登录用户.登录才有权限访问
	permission_classes = [IsAuthenticated]

	# 3.重写get_objects(self),返回用户详情模型对象
	def get_object(self):
		return self.request.user


# 3.手机号
class MobileCountView(APIView):
	"""判断手机号是否已存在:手机号数量是否为0"""

	def get(self, request, mobile):
		# 查询数据库中此手机号的数量
		count = User.objects.filter(mobile=mobile).count()
		data = {
			'mobile': mobile,
			'count': count,
		}

		return Response(data)


# 2.用户名
class UsernameCountView(APIView):
	"""判断用户名是否已存在:用户名数量是否为0 """

	def get(self, request, username):
		# 查询数据库中此用户名的数量
		count = User.objects.filter(username=username).count()
		data = {
			'username': username,
			'count': count,
		}
		return Response(data)


# 1.注册
class UserView(CreateAPIView):
	"""注册:
	因为在这里只是一个新增功能,
	所以使用GenericView和CreateMixin扩展的合体->CreateAPIView
	来实现即可
	"""
	serializer_class = CreateUserSerializer
