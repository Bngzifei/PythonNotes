# coding:utf-8
"""
使用具名元组记录一个城市的信息

1.创建一个具名元组需要两个参数,一个是类名,另一个是类的各个字段的名字.
后者可以是由数个字符串组成的可迭代对象,或者是由空格分隔开的字段名组成
的字符串.

2.存放在对应字段里的数据要以一串参数的形式传入到构造函数中.(注意,元组的
构造函数只接受单一的可迭代对象)

3.你可以通过字段名(以.的方式获取)或者下标位置(以索引的方式获取)来获取一
个字段的信息.


除了从普通元组那里继承来的属性之外,具名元组还有一些自己专有的属性.
其中最有用的:_fields类属性,类方法_make(iterable)和实例方法_asdict()



1._fields属性是一个包含这个类所有字段名称的元组

2.用_make()通过接受一个可迭代对象来生成这个类的一个实例,它的作用跟City(*delhi_data)
是一样的.

3._asdict()把具名元组以collections.OrderedDict的形式返回,我们
可以利用它来把元组里的信息友好地呈现出来.(就是为了改变一下输出的形式)

"""


from collections import namedtuple

City = namedtuple("City","name country population coordinates")
tokyo = City("Tokyo","JP",36.933,(35.689722,139.691667))
print(tokyo)
print(tokyo.name)
print(tokyo.country)
print(tokyo.population)
print(tokyo.coordinates)
print("---------------")
print(tokyo[0])
print(tokyo[1])
print(tokyo[2])
print(tokyo[3])
print("#################")
print(City._fields)  # 元组的字段名

LatLong = namedtuple("LatLong","lat long")  # 定义类名:LatLong  两个属性:lat long
delhi_data = ("Delhi NCR","IN",21.935,LatLong(28.613889,77.208889))  # 定义一个元组(可迭代)
delhi = City._make(delhi_data)  # 就是起到一个解包的作用,等价于*delhi_data
print(delhi)
print("1111111111111")
print(LatLong(28.613889,77.208889))
print("00000000000")
print(delhi._asdict())

for key,value in delhi._asdict().items():  # 为了更好地输出,为了打印出来更好看一点.
	print(key + ":",value)
