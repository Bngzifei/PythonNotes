# coding:utf-8

"""
OrderedDict是dict的子类,其最大特征是,它可以"维护"添加key-value的
顺序.简单来说,就是先添加的key-value对排在前面,后添加的key-value对
排在后面.

由于OrderDict能维护key-value对的添加顺序,因此即使两个OrderedDict中
的key-value对完全相同,但只要他们的顺序不同,程序在判断他们是否相等时也
依然会返回fasle

例如:
"""
from collections import OrderedDict

# 创建OrderedDict对象
dx = OrderedDict(b=5,c=2,a=7)
print(dx)
print(type(dx))

d = OrderedDict()
# 向OrderDict中添加key-value对
d["python"] = 89
d["python"] = 88
d["c++"] = 87
d["swift"] = 97
d["kotlin"] = 41
d["go"] = 78

# 遍历OrderedDict的key-value对
for k,v in d.items():
    # fotmat的用法:就是在""里面用关键字来占位,format参数写关键字=实际的值  这种写法
    print("key是{key},value是{value}".format(key=k,value=v))
"""
上面的程序首先创建了OrderedDict对象,接下来程序向其中添加了4个key-value对,
OrderedDict完全可以"记住"它们的添加顺序.运行该程序,可以看到如下输出结果:
"""
print(type(d.items()))
print(type(d.keys()))
print(type(d.values()))

"""
正如前面所说的,两个OrderedDict中即使包含的key-value对完全相同,但只要他们的顺序不同,
程序也依然会判断出两个OrderedDict是不相等的.例如如下程序:

"""

# 创建普通的dict对象
my_data =  {"python":45,"swift":78,"kotlin":89,"go":78}
# 创建基于key排序的OrderedDict(基于xxx:就是以xx为基准,按xxx大小来排)
# 注意这里的lambda排序规则:因为my_data.items()是一个key-value的形式,
# 注意:在python2中my_data.items()是列表类型,在python3中是视图对象类型,
# 但是用法和python2一样.所以在这里key=lambda t:t[0],
# 这里的t就是my_data.items()的返回值
print("--------------")
print(len(my_data.items()))
print(my_data.items())
print("--------------")

# 创建基于key排序的OrderedDict
d1 = OrderedDict(sorted(my_data.items(),key=lambda t:t[0]))
print(d1)
print(sorted(my_data.items(),key=lambda t:t[0]))
print(type(my_data.items()))

# 这么使用是错误的
# print(my_data.items()[0])


# 创建基于value排序的OrderedDict
d2 = OrderedDict(sorted(my_data.items(),key=lambda t:t[1]))
print(d2)
print(d1 == d2)


"""
上面程序先创建了一个普通的dict对象,该对象中包含4个key-value键值对;接下来程序分别
使用sorted()函数对my_data(dict对象)的items进行排序:d1是按key排序的;d2是按value
排序的,这样得到的d1,d2两个OrderedDict中的key-value对是一样的,只不过熟悉怒不同

运行上面程序，可以看到如下输出结果：
OrderedDict([('Go', 25), ('Kotlin', 43), ('Python', 20), ('Swift', 32)])
OrderedDict([('Python', 20), ('Go', 25), ('Swift', 32), ('Kotlin', 43)])
False



从上面的输出结果可于看到.虽然两个OrderedDict所包含的key-value对完全相同,但由于它们的
顺序不同,因此程序判断它们不相等.

此外,由于OrderedDict是有序的,因此python为其提供了两个方法:

popitem(last=True)：默认弹出并返回最右边（最后加入）的 key-value 对；如果将 last 参数设为 False，则弹出并返回最左边（最先加入）的 key-value 对。
move_to_end(key, last=True)：默认将指定的 key-value 对移动到最右边（最后加入）；如果将 last 改为 False，则将指定的 key-value 对移动到最左边（最先加入）。


"""

from collections import OrderedDict

d = OrderedDict.fromkeys("abcde")

# 将b对于的key-value对移动到最右边(最后加入)
d.move_to_end("b")
print(d.keys())
# odict_keys(['a', 'c', 'd', 'e', 'b'])

d.move_to_end("b",last=False)

print(d.keys())
# odict_keys(['b', 'a', 'c', 'd', 'e'])

# 弹出并返回最右边(最后加入)的key-value对
print(d.popitem()[0])
# 弹出并返回最左边(最先加入)的key-value对
print(d.popitem(last=False)[0])


"""
运行上面程序，可以看到如下输出结果：
odict_keys(['a', 'c', 'd', 'e', 'b'])
odict_keys(['b', 'a', 'c', 'd', 'e'])
e
b

"""


"""
通过上面的输出结果可以看出,使用OrderedDict的mobe_to_end()方法
可以方便地将指定的key-value对移动到OrderedDict的任意一端.
而pop


"""
