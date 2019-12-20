import random
import logging

from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import constants
# from meiduo_mall.libs.yuntongxun.sms import CCP
from celery_tasks.sms.tasks import send_sms_code
# 获取日志输出器
logger = logging.getLogger('django')


# -----------------------3.celery异步实现版本:---------------
"""
为什么选择使用APIView?
因为在这里不需要序列化操作和models模型类打交道,所以直接使用APIView操作即可.
"""
class SMSCodeView(APIView):
	"""发送短信视图"""

	def get(self, request, mobile):
		"""
		注意:只有使用了视图集,这里的方法中才是使用动作,而不是请求方法名
		路径:GET /sms_codes/(?P<mobile>1[3-9]\d{9})/
		:param request: Request类型的对象
		:param mobile: 手机号
		:return: Response
		"""

		# 连接redis. verify_codes是别名,默认别名是default,这里我们修改成verify_codes
		# 说明:这里没有必要使用管道,因为紧跟着下面就要使用如果使用管道,那么还需要手动的execute()推送一下
		redis_conn = get_redis_connection('verify_codes')
		# 注意:在这里一定是先获取send_flag验证码发送标记,先进行判断
		send_flag = redis_conn.get('send_flag_%s' % mobile)


		# 判断send_flag是否有值,没有就说明不是重复发送
		if send_flag:
			return Response({'message':'频繁发送短信,小心点!'},status=status.HTTP_400_BAD_REQUEST)




		# 1.生成短信验证码
		sms_code = '%06d' % random.randint(0, 999999)
		logger.info(sms_code)




		# 在这里创建管道:管道不会自动执行,需要手动推一下才能生效
		# 目的:减少redis的访问次数,提升性能
		pl = redis_conn.pipeline()








		# 存验证码
		pl.setex('sms_%s'%mobile,constants.SMS_CODE_REDIS_EXPIRES,sms_code)

		# 存标记:标识此号码已经发送过验证码  这里的1 是value.是key对应的值.
		pl.setex('send_flag_%s'%mobile,constants.SEND_FLAG_TIME_INTERVAL,1)

		# 手动执行:让管道中的命令一次性执行.这里的pl是一个列表.
		pl.execute()



		# 3.发送短信验证码 参数:to就是手机号,datas:就是有效时间,这里是300秒也就是5分钟,temp_id:短信验证码的模板id
		# CCP().send_template_sms(mobile, [sms_code, constants.SMS_CODE_REDIS_EXPIRES // 60], 1)


		# 格式:任务函数.delay(任务函数的参数)
		# 注意:这里是有延时delay的.因为celery异步任务塞进celery任务队列里面的时候,还没有执行,
		# 还需要等一下才能执行,否则你直接调用了send_sms_code()函数,那么异步任务就不会生效了.
		send_sms_code.delay(mobile,sms_code)
		return Response({'message': 'OK'})
















"""
因为对redis数据库进行读取操作是一个消耗性能的操作.所以在这里使用管道进行优化

60秒发送短信

"""
"""
因为发送短信是网络请求的操作,那么就会很耗时,如果长时间没有收到响应,
用户体验就很糟糕,所以需要使用异步操作实现发送短信
这里我们使用celery异步服务实现发送短信验证码部分
"""
# -----------------------2.同步阻塞版本:---------------
# class SMSCodeView(APIView):
# 	"""发送短信视图"""
#
# 	def get(self, request, mobile):
# 		"""
# 		注意:只有使用了视图集,这里的方法中才是使用动作,而不是请求方法名
# 		路径:GET /sms_codes/(?P<mobile>1[3-9]\d{9})/
# 		:param request: Request类型的对象
# 		:param mobile: 手机号
# 		:return: Response
# 		"""
#
# 		# 连接redis. verify_codes是别名,默认别名是default,这里我们修改成verify_codes
# 		# 说明:这里没有必要使用管道,因为紧跟着下面就要使用如果使用管道,那么还需要手动的execute()推送一下
# 		redis_conn = get_redis_connection('verify_codes')
# 		# 注意:在这里一定是先获取send_flag验证码发送标记,先进行判断
# 		send_flag = redis_conn.get('send_flag_%s' % mobile)
#
#
# 		# 判断send_flag是否有值,没有就说明不是重复发送
# 		if send_flag:
# 			return Response({'message':'频繁发送短信,小心点!'},status=status.HTTP_400_BAD_REQUEST)
#
#
# 		# 在这里创建管道:管道不会自动执行,需要手动推一下才能生效
# 		# 目的:减少redis的访问次数,提升性能
# 		pl = redis_conn.pipeline()
#
#
#
#
#
# 		# 1.生成短信验证码
# 		sms_code = '%06d' % random.randint(0, 999999)
# 		logger.info(sms_code)
#
#
# 		# 存验证码
# 		pl.setex('sms_%s'%mobile,constants.SMS_CODE_REDIS_EXPIRES,sms_code)
#
# 		# 存标记:标识此号码已经发送过验证码  这里的1 是value.是key对应的值.
# 		pl.setex('send_flag_%s'%mobile,constants.SEND_FLAG_TIME_INTERVAL,1)
#
# 		# 手动执行:让管道中的命令一次性执行.这里的pl是一个列表.
# 		pl.execute()
#
#
#
# 		# 3.发送短信验证码 参数:to就是手机号,datas:就是有效时间,这里是300秒也就是5分钟,temp_id:短信验证码的模板id
# 		CCP().send_template_sms(mobile, [sms_code, constants.SMS_CODE_REDIS_EXPIRES // 60], 1)
#
# 		return Response({'message': 'OK'})



























"""
# ------------简陋版:除了发短信之外,还需要对已经发送过验证码的手机号进行判断,
因为我们需要防止用户恶意暴力的刷验证码,这样会频繁的发送短信,损失很多.
方法:可以使用限流,但是在用户体验方面不是很好,因为如果一个用户在注册的时候可能卡顿或延时等原因造成用户误判,
用户再刷一次的时候就会直接提示用户需要过多久才能再刷验证码.交互不友好,所以,在这里我们采用标记的方式实现.
即给每一个已经发送过验证码的手机号进行标记.然后存到数据库中,在用户刷验证码的时候使用这个标记进行判断.
具体操作:
1.每次发送短信验证码时，在Redis数据库中记录⼀一个值，并设置该值的有效期为60s
2.在⽣生成短信验证码之前，尝试从Redis数据库中读取该值
3.读取结果
	1.存在  说明在60s内重复发送，直接return 响应400
	2.不存在 说明在60s内没有重复发送，继续执⾏后续逻辑

因为对redis数据库进行读取操作是一个消耗性能的操作.所以进行优化
"""

# -----------------------1.原始版:最直接的实现方式--------------
# class SMSCodeView(APIView):
# 	"""发送短信视图"""
#
# 	def get(self, request, mobile):
# 		"""
# 		注意:只有使用了视图集,这里的方法中才是使用动作,而不是请求方法名
# 		路径:GET /sms_codes/(?P<mobile>1[3-9]\d{9})/
# 		:param request: Request类型的对象
# 		:param mobile: 手机号
# 		:return: Response
# 		"""
#
# 		# 连接redis. verify_codes是别名,默认别名是default,这里我们修改成verify_codes
# 		redis_conn = get_redis_connection('verify_codes')
#
# 		# 1.生成短信验证码
# 		sms_code = '%06d' % random.randint(0, 999999)
# 		logger.info(sms_code)
#
# 		# 2.把短信验证码缓存到redis数据库中.格式: key 过期时间(单位是秒) value
# 		redis_conn.setex('sms_%s' % mobile,constants.SMS_CODE_REDIS_EXPIRES, sms_code)
#
# 		# 3.发送短信验证码 参数:to就是手机号,datas:就是有效时间,这里是300秒也就是5分钟,temp_id:短信验证码的模板id
# 		CCP().send_template_sms(mobile,[sms_code,constants.SMS_CODE_REDIS_EXPIRES // 60],1)
#
#
#
#
# 		return Response({'message': 'OK'})
