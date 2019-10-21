from foo import *   # 从foo.py文件中导入__all__元组中指定的成员变量

from foo import z   # 直接从foo.py文件中导入z成员变量


print("x:", x)
print("y:", y)
print("z:", z)


print("test:", test)

"""
可以看到终端直接输出:
说明 对from XXX import XXX 的导包方式不起作用  

x: 2
y: 9
z: 6
test: <function test at 0x00D216F0>
[Finished in 0.1s]

"""