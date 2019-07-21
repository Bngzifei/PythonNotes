print('--------------------import导入:在内存中发送了什么?------------------------')
"""
1.>模块的搜索路径
导入指定路径下的模块
	1.修改sys.path变量<特点:程序重启后失效,临时的>
	2.修改环境变量 PYTHON_PATH
	Ubuntu下面:vim ~/.bashrc   export PYTHONPATH=$PYTHONPATH:/home/python/Desktop
	CentOS下面:
	  vim ~/.bash_profile  export PYTHONPATH=$PYTHONPATH:/home/python/Desktop
	保存退出,<Ubuntu>刷新: source ~/.bashrc ,CentOS刷新: source ~/.bash_profile
	新开一个终端执行import 模块就可以.
	
	
2.>import导入过程:先后顺序如下:
	1.>sys.modules 模块中搜索是否有  locals()/globals() 查看,返回值 是一个字典类型  表示已经导入的模块 <Python自动导入,常用,提高效率>
	2.>sys.path 中搜索是否有 <系统中模块文件可能存在的路径> 导入模块的搜索路径
		sys.path是一个list列表类型
		sys.path.append(指定路径) 这种导入是临时的,只要程序退出就失效了.
		sys.path一部分来自PATHONPATH环境变量
	PS:在导入的时候,在内存里面完完整整复制了一个模块,本地有一个对象,和模块的名字是一样的,引用指向了这个模块
	会在内存中创建模块对象,会在当前程序中创建一个和模块名同名的对象,这个对象保存模块对象的引用.
	
	3.找到模块文件,创建模块对象
	4.>在当前作用域创建一个对象保存,模块对象的引用
		locals()查看本地名字空间当中的所有的名字
		创建模块对象,在本地作用域有一个和模块名重名的对象.
		globals()查看全局名字空间中的所有的名字
	5.通过这个对象可以使用模块中的所有,比如 threading.Thread
	
3. from B import A:
	只会把A导入到sys.path,不会把B导入 就是把模块B里面的东西拆分开了,各自导入
	所有的模块中的东西都是模块的属性.
	所以from 导入的都是属性

不同: import A:创建模块之后,import A在当前作用域创建一个名字为A的对象,用来保存模块对象的引用
from A import B: 在当前作用域创建名字为B的对象,用来保存模块对象里面的某个属性的引用

locals()  本地名字空间,返回值是一个字典类型
globals() 全局名字空间,返回一个字典

在局部就是局部,在全局就是全局,记住是当前作用域.
		
"""
# -------------------------------理解--------------------------------------->

# 不建议使用 from A import * 这种方式.
# import 方式在当前作用域创建和模块同名的对象,保存模块的引用

# from 方式在当前作用域创建和属性同名的对象,保存属性的引用


# 把模块当成一个整体对象,那么模块中的对象,函数变量方法等等都可以被当做模块的属性
# 因为可以使用模块.的方法进行调用

# 关键注意点:就是看导入了那些部分
# import 可以修改不可变类型的值
# from...import... 不可以修改不可变类型的值
# import  可以修改可变类型的值
# from ... import 可以修改可变类型的值

# 记住:只有from-import 导入的时候无法修改不可变类型的属性值.

"""
reload的作用:
import 模块只能导入一次,当再次导入的时候直接使用前面一次的导入的模块

py2:reload(模块名)
py3:from imp import reload
reload(模块名)
通过模块.属性去取值,即可

sys.modules直接去拿值,
reload会从磁盘中重新创建然后加载.
作用:从磁盘中重新加载模块,在内存中创建对象
在内存中重新建一个对象
"""


str1 = '1223'
print(str1.isalpha())  # 不是字母












































