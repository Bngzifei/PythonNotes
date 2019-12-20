"""
__import__() 函数用于动态加载类和函数 。

如果一个模块经常变化就可以使用 __import__() 来动态载入。
语法
__import__ 语法：
__import__(name[, globals[, locals[, fromlist[, level]]]])
参数说明：
name -- 模块名



说明：

　　1. 函数功能用于动态的导入模块，主要用于反射或者延迟加载模块。

　　2. __import__(module)相当于import module



先定义两个模块mian.py和index.py，两个文件在同一目录下：


执行main.py，可以证实动态加载了index.py，__import__返回的模块也是index模块


3. __import__(package.module)相当于from package import name，如果fromlist不传入值，则返回package对应的模块，
如果fromlist传入值，则返回package.module对应的模块。


4. level参数，指定是使用绝对导入还是相对导入。 0(默认值)表示只执行绝对导入。

"""


