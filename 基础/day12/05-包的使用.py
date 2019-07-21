"""
包:项目中的文件夹就是一个一个的包,使用包里面的文件的时候要加 包名.文件名

 ---->  就是项目文件夹里面的文件夹
"""
# 只能导入当前项目下的文件 ,否则就需要加包名

# import message.msg_send
#
# message.msg_send.func_send()  # 方式导入使用包里面的内容时, 格式: 包名.模块名.xxx
#


# from message.msg_send import *  # 方式2导入时,要加包名,使用的时候不加包名,模块名
# func_send()


# Python 3 中项目中的文件就是一个文件夹.

# Python 2 中想让文件夹中的模块能正常导入,需要在包中有一个__init__文件
