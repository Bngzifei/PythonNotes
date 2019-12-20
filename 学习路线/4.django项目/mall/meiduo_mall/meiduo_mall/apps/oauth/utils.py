from itsdangerous import TimedJSONWebSignatureSerializer as TJSSerializer, BadData
from django.conf import settings
from .import constansts




def check_save_user_token(access_token):
	"""
	解密:校验保存用户数据的access_token
	:param access_token: 用户的access_token
	:return: openid or None
	"""

	serializer = TJSSerializer(settings.SECRET_KEY,expires_in=constansts.SAVE_QQ_USER_TOKEN_EXPIRES)

	try:
		data = serializer.loads(access_token)
	except BadData:
		return None
	else:
		return data.get('openid')







def generate_save_user_token(openid):
	"""
	加密openid
	:param openid: 明文的openid
	:return: 返回加密后的openid
	"""

	# 创建序列化器,指定秘钥和过期时间
	serializer = TJSSerializer(settings.SECRET_KEY,expires_in=constansts.SAVE_QQ_USER_TOKEN_EXPIRES)


	data = {'openid':openid}
	# 对openid进行签名.返回签名之后的bytes类型字符串
	token = serializer.dumps(data)
	# 将bytes数据解码成正常的字符串
	return token.decode()

