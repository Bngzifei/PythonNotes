# __all__是一个字符串list,就是[str1,str2,...]的形式,也可以是一个元组,(str1,str2,...)，
# 用来定义模块中以 from XXX import *  导包时需要对外导出的成员(成员可以是一个类,函数,全局变量或者常量),
# 即需要暴露的接口，但它只对  import *  的导包方式作用，对  from XXX import XXX 的导包方式不起作用.


# 例子:

# 这里只允许导包的时候导出下面的三个成员变量
__all__ = ("x", "y", "test")

x = 2
y = 9
z = 6


def test():
    print("test")
