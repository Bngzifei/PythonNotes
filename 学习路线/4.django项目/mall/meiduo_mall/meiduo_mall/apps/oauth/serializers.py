from django_redis import get_redis_connection
from rest_framework import serializers
from users.models import User
from .models import OAuthQQUser
from .utils import check_save_user_token


class QQAuthUserSerializer(serializers.Serializer):
	"""qq登录:创建用户序列化器"""
	access_token = serializers.CharField(label='操作凭证')
	mobile = serializers.RegexField(label='手机号', regex=r'^1[3-9]\d{9}$')
	password = serializers.CharField(label='密码', max_length=20, min_length=8)
	sms_code = serializers.CharField(label='短信验证码')

	def validate(self, attrs):
		# 1.校验access_token
		access_token = attrs.get('access_token')
		# 2.获取身份凭证  因为access_token之前已经经过加密,所以这里需要进行解密才能获取到
		openid = check_save_user_token(access_token)
		if not openid:
			raise serializers.ValidationError('无效的access_token')

		# 3.将openid放在校验字典中
		attrs['openid'] = openid

		# 4.检验短信验证码
		mobile = attrs['mobile']
		sms_code = attrs['sms_code']
		redis_conn = get_redis_connection('verify_codes')
		real_sms_code = redis_conn.get('sms_%s' % mobile)
		if real_sms_code.decode() != sms_code:
			raise serializers.ValidationError('短信验证码错误')

		try:
			# 5.如果用户存在,检查用户密码
			user = User.objects.get(mobile=mobile)
		except User.DoesNotExist:
			# 6.如果用户不存在
			pass
		else:
			# 5.1 用户存在的情况下,校验密码
			password = attrs.get('password')
			if not user.check_password(password):  # 校验密码
				raise serializers.ValidationError('密码错误')

			# 将认证后的user放进校验字典中.
			attrs['user'] = user
		# 注意这里的缩进,否则就会没有结束,这个函数就没有返回值.这种错误已经犯了很多次了,必须接受教训了.
		return attrs

	def create(self, validated_data):
		"""新增用户"""
		# 获取校验的用户
		user = validated_data.get('user')

		if not user:
			# 用户不存在,新增
			user = User.objects.create_user(
				username=validated_data.get('mobile'),
				password=validated_data.get('password'),
				mobile=validated_data.get('mobile'),
			)

		# 将用户绑定openid
		OAuthQQUser.objects.create(
			openid=validated_data.get('openid'),
			user=user
		)

		# 返回用户数据.因为在绑定之后要做状态保持,做载荷的时候需要使用user
		return user
