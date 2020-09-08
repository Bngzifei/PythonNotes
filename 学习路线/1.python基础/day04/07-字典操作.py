# dict1 = {"name": "zhang", "age": 15,'gender':'male'}  # 这个在第一行,后面的注释就会变成绿色
# """增加元素"""
# dict1["height"] = 1.7  # key不存在就是增加,存在就是修改
# print(dict1)
# """删除元素"""
# del dict1["gender"]  # 删除指定key对应的键值对,无返回值
# print(dict1)
#
# name = dict1.pop("name")  # 删除指定key对应的键值对,并且把删除的value返回,pop()本来是删除最后一个,但是因为字典是无序的,所以必须指定key,否则会报错
# print(name)


# a = 10
# del a  # 提前销毁了a NameError: name 'a' is not defined
# print(a)  # 没有变量保存的就回收了

"""清空"""
dict1 = {"name": "zhang", "age": 15, 'gender': 'male'}
dict1.clear()  # 清空
# print(dict1)
# # 常用pop,因为可以有返回值
#
# """修改元素"""
# dict1["name"] = "74"  # 修改key对应的value
# print(dict1)
# dict1.setdefault("name1", "lisi")  # 如果key存在,什么也不做,key不存在就增加键值对
# print(dict1)
dict2 = {'height': 175, "boy": True, "name": "liskk"}
# key存在就是修改(因为key如果存在的话新添加的key对应的value会覆盖掉原来的value),不存在就增加键值对
dict1.update(dict2)
# print(dict1)
# """查询元素"""
# 查询的方法均有返回值
dict1 = {"name": "zhang", "age": 15,'gender':'male'}
name = dict1["name"]  # 获取指定key的value,如果获取的key不存在,报错
#
# name = dict1.get("name1")  # 获取指定key的value,如果获取的key不存在,不会报错,返回None
# print(name)
"""
视图对象/可视对象:dict_keys(['name', 'age']),减少内存的占用.

Python2中keys获取到的就是列表[],Python3修改成了视图对象,目的是为了减少内存的占用.数据类型变了,更加省内存空间了.(版本升级肯定是越来越好,不能变差了)

1.查看内部结构 2.支持for循环遍历 3.支持if in语句 4.没有增.删.改(类似元组) 5.可以把它转换成高级变量类型
"""
# import sys
#
# print(sys.getsizeof(print('we')))  # 就是print()输出了we之后光标跳到了下一行.接着输出16
# print(sys.getsizeof(print('we',end='\t')))  # 而这里是print()输出we之后光标跳到了we同一行的后面两个字符的位置,加we和后面两个空格的位置一共是4个字符位置.
# sys:系统模块,getsizeof()获取占用的字节位长度
"""查看内存占用"""
# import sys
# dict1 = {"name": "zhang", "age": 15,'gender':'male'}
# keys = dict1.keys()  # 获取字典中所有的键
# list1 = list(keys)  # 转换成list形式
#
# # print(sys.getsizeof(keys))  # 占用48个字节
# # print(sys.getsizeof(list1))  # 占用104个字节
"""字典.keys:获取所有的key"""
dict1 = {"name": "zhang", "age": 15,'gender':'male'}
keys = dict1.keys()  # 获取字典中所有的键
for key in keys:
	print(key)
print(keys)  # 输出的是:dict_keys(['name', 'age'])
"""字典.values:获取所有的value"""
dict1 = {"name": "zhang", "age": 15,'gender':'male'}
values = dict1.values()  # 获取出字典中所有的值,返回的也是视图对象
for value in values:
	print(value)
print(values)
"""字典.items:获取所有的key-value键值对"""
dict1 = {"name": "zhang", "age": 15,'gender':'male'}
items = dict1.items()  # 获取出所有的键值对,视图对象,里面是一个元组类型,且元组的个数是固定的,所以可以使用解包
print(items)
for item in items:
	print(item)

for key,value in dict1.items():  # 解包
	print(key)
	print(value)

for ele in dict1:  # 遍历字典默认取到的是key,这种最好用,最常用
	print(dict1[ele])  # 通过key来取到value


import sys
it = dict1.keys()  # 获取所有key
print(sys.getsizeof(it))  # 占用少,叫视图对象

it1 = list(it)
print(sys.getsizeof(it1))  # 占用的内存字节多

values = dict1.values()  # 所有值
print(values)  # dict_values(['zang', 15])

items = dict1.items()  # 所有key-value键值对
print(items)  # dict_items([('name', 'zang'), ('age', 15)])
print(type(items))  # <class 'dict_items'>
for key, value in dict1.items():
	print(key)
	print(value)
for ele in dict1:  # 遍历默认是key
	print(dict1)
	print(dict1[ele])
