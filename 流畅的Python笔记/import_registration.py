import Python何时执行装饰器


"""
输出:
running register(<function f1 at 0x0080C348>)
running register(<function f2 at 0x0080C390>)

由此说明,函数装饰器在导入模块时(说明装饰器是在被装饰的函数定义时立即生效的)
立即执行.而被装饰的函数只在明确调用时运行.这突出了Python程序员所说的导入时
和运行时之间的区别.
"""
#输出
#[<function f1 at 0x0078C348>, <function f2 at 0x0078C390>]
print(Python何时执行装饰器.registry)