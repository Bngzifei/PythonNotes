# from m1 import t # m1/t1  路径其实就是一个字符串类型


'm1.t'  # 路径其实就是一个字符串类型

# module_t = __import__('m1.t1')  # test1 导入的过程就是执行这个导入的文件
# 不管套了多少层,最后拿到的是最外层的模块名
# print(module_t)  # <module 'm1' (namespace)>
# module_t 就是 m1 这个包
# module_t.t1.test1()  # test1

# m = __import__('test')  # hello world,导入的过程就是执行这个文件的过程

# print(m)  # <module 'test' from 'F:\\黑马Python20期就业班\\oldboy\\test.py'>

# _test2() 也可以导入
# from m1.t1 import test1,_test2
#
# test1()
# _test2()

# 以字符串形式导入
import importlib
m = importlib.import_module('m1.t1')  # 就是我想要的那个文件
print(m)  # <module 'm1.t1' from 'F:\\黑马Python20期就业班\\oldboy\\m1\\t1.py'>
m.test1()  # test1
m._test2()  # test2()

# 注意:模块也是一个对象,对象具有__init__()方法,所以在建立一个包的时候,
# 包里面也会有一个__init__.py文件, 初始化文件
# 动态导入模块的过程也是一个文件对象实例化的过程
