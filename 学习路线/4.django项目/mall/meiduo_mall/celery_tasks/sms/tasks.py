# 注意这个文件名必须是tasks,因为celery里面写死了
from celery_tasks.main import celery_app
from .yuntongxun.sms import CCP
from . import constants


# 使用装饰器装饰一个函数,使其成为一个异步任务.
# 并且指定任务的别名是send_sms_code.别名没有其他意义,只是因为默认的任务名称很长,不方便使用
@celery_app.task(name='send_sms_code')
def send_sms_code(mobile,sms_code):
	"""发送短信"""
	CCP().send_template_sms(mobile,[sms_code, constants.SMS_CODE_REDIS_EXPIRES // 60],1)