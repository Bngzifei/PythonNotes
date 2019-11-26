"""
本节讨论把函数视作对象相关的几个属性


1.>函数使用__dict__属性存储赋予它的用户属性.这相当于一种基本形式的注解.
一般来说,为函数随意赋予属性不是很常见的做法.

下面重点说明函数专有而用户定义的一般对象没有的属性.
计算两个属性集合的差集便能得到函数专有属性列表.
"""

# 列出常规对象没有而函数有的属性
class C:pass
obj = C()
def func():pass

print(sorted(set(dir(func)) - set(dir(obj))))
"""
输出:['__annotations__', '__call__', '__closure__', '__code__', 
'__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']


__globals__:函数所在模块中的全局变量

__kwdefaults__:仅限关键字形式参数的默认值

__name__:函数名称




Bobo是怎么知道函数需要哪个参数的呢?
	
	函数对象有个__defaults__属性,它的值是一个元组,里面保存着定位参数和关键字参数的默认值.
	仅限关键字参数的默认值在__kwdefaults__属性中.然而,参数的名称在__code__属性中,它的值是
	一个code对象引用,自身也有很多属性.
"""

print("**************>>>")

# 在指定长度附件截断字符串的函数
def clip(text,max_len=80):
	"""在max_len前面或后面的第一个空格处截断文本"""
	end = None
	if len(text) > max_len:
		space_before = text.rfind(" ",0,max_len)
		if space_before >= 0:
			end = space_before
		else:
			space_after = text.rfind(" ",max_len)
			if space_after >= 0:
				end = space_after
	if end is None:
		end = len(text)
	return text[:end].rstrip()