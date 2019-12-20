# 此文件作为celery启动的入口.启动入口文件
# 在入口文件做三件事:
# 1.创建celery客户端 Celery()
# 2.加载celery配置:配置异步任务存放的位置
# 3.把异步任务添加到任务队列中
# 可以都写在这里,但是为了将来的维护,都会分开写

from celery import Celery



# 为celery使用django配置文件进行设置
import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'meiduo_mall.settings.dev'


# 1.创建celery客户端: celery = Celery()
# 括号中的meiduo_sz20只是一个别名,不写也可以,无实际意义
celery_app = Celery('meiduo_sz20')

# 2.加载配置    终端运行的时候需要加这个路径.   包名.config
celery_app.config_from_object('celery_tasks.config')


# 3.注册任务  celery_tasks.sms:目录写死了,只能到这里.包.文件名
# celery_app.autodiscover_tasks('celery_tasks.sms')
# 注意:这里的任务有多个,一定要把任务添加到列表中[].上面的写法就是错误的
# ['celery_tasks.sms']:表示自动监测celery_tasks里面的sms发短信模块的耗时任务.[]形式表明还可以添加其他的异步任务
celery_app.autodiscover_tasks(['celery_tasks.sms','celery_tasks.email','celery_tasks.html'])




# 调试:注释法,替换法,排除法,压缩法




