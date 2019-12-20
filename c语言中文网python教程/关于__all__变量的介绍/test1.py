from foo import *

print("x:", x)
print("y:", y)
print("z:", z)  # NameError: name 'z' is not defined
# 可以看到foo.py 中的z成员变量无法通过 from foo import *
# 的方式导入到test1.py文件中进行调用

test()
