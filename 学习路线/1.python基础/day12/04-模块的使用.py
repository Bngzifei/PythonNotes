"""模块的导入方式:

任何一个.py都可以作为模块使用,但是想要正常导入,模块名不能以数字开头.

"""
"""第一种:"""
# 同时可以导入多个模块
import module, sys, math  # 导入模块的全部内容,  格式:import 模块名

#
# # 使用模块:可以使用模块中的函数,全局变量,类,类中的方法.  # 使用格式: 模块名.xx
#
# dog1 = module.Dog()
# dog1.eat()
# print(__name__)

"""第二种:

优点,可以进行局部导入,并且使用时不用在前面加模块名
缺点:如果导入多个模块时,如果多个模块中有同名内容,后面导入的模块名会覆盖前面的内容.

所以写名字的时候要长点.来避免重名.

"""
# 1>.可以导入多个模块
# def func1():
# 	print('xxxxx')
#
# from module,xxx,xxxx import func1,count
# func1()

# 2>.
from module import *  # 默认导入模块中的所有内容,__all__可以控制from 模块名 import * 导入方式的时候,所导入的内容.

# print(__name__)
# count
# Dog
# func1()


# import sys
# print(sys.path)  # 查询python 解释器导入模块的默认路径
# # 'C:\\Pyhton36\\lib\\site-packages'  第三方安装包的 存放路径.
# # 其他的模块文件都放到项目里面.
