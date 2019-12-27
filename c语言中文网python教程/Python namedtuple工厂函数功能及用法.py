# Python namedtuple工厂函数功能及用法

"""
namedtuple()是一个工厂函数,使用该函数可以创建一个tuple类的子类,该子类可以为tuple的
每个元素都指定字段名,这样程序就可以根据字段名来访问namedtuple的各个元素了.当然,
如果有需要,程序依然可以根据索引来访问namedtuple的各个元素.

namedtuple是轻量级的,性能很好,其并不比普通tuple需要更多的内存.namedtuple函数的
语法格式如下:
namedtuple(typename,field_names,*,verbose=False,rename=False,model+None)

关于该函数参数的说明如下:
1.>typename:该参数指定所创建的tuple子类的类名,相当于用户定义了一个新类.

2.>field_names:该参数是一个字符串序列,如["x","y"].此外field_names也可以直接使用
单个字符串代表所有字段名,多个字段名用控股,逗号隔开,如"x y"或"x,y"任何有效地Python
标识符都可以作为字段名(不能以下划线开头.)有效地表示符可由字母,数字,下划线组成,但不能
以数字,下划线开头,也不能是关键字(如 return global pass raise等)

3.>rename:如果将该参数设置为True,那么无效的字段名将会被自动替换为位置名.例如指定
["abc","def","ghi","abc"],它将会被替换为["abc","_1","ghi","_3"],这是因为def字段名
是关键字,而abc字段名重复了.

4.>verbose:如果该参数被设置为True,那么当该子类被创建之后,该类定义就会被立即打印出来.


5.>module:如果设置该参数,那么该类将位于该模块下,因此该自定义类的__module__属性
将被设为该参数值.


下面程序示范了使用namedtuple工厂函数来创建命名元组

"""

from collections import namedtuple


# 定义命名元祖类:Point  x和y就是在后面进行一个占位的作用
Point = namedtuple("Point", ["x","y"])

# 初始化Point对象,即可用位置参数,也可用命名参数
p = Point(11,y=22)

# 像普通元组一样用根据索引访问元素
print(p[0]+p[1])  # 33


# 执行元组解包,按元素的位置解包
a,b = p
print(a,b)


# 根据字段名访问元素
print(p.x + p.y)
print(p)
print(type(p))



"""
上面程序先创建了一个命名元组Point,它是tuple的子类,因此程序即可以使用
命名参数的方式设置元组成员,也可以使用索引的方式设置元组成员.

在创建了Point对象之后,Point就代表一个命名元组,程序既可以使用普通元组的方式
来访问元组的成员,也可以使用字段名来访问元组的成员.

除上面介绍的用法之外,Python还未命名元组提供了如下方法和属性:
1.>_make(iterable):类方法.该方法用于根据序列或可迭代对象创建命名元组对象

2.>_asdict():将当前命名元组对象转换为OrderedDict字典

3.>_replace(**kwargs):替换命名元组中一个或多个字段的值

4.>_source:该属性返回定义该命名元组的源代码.

5.>_fields:该属性返回该命名元组中所有字段名组成的元组.
"""

my_data = ["East","North"]
print("---------------")
# 创建命名元组对象
p2 = Point._make(my_data)  # Point(x='East', y='North')
print(p2)

# 将命名元组对象转换成OrderedDict
print(p2._asdict())  #  # OrderedDict([('x', 'East'), ('y', 'North')])

# 替换命名元组对象的字段值
p2._replace(y="South")
print(p2)

# 输出p2包含的所有字段(就是所有的key,类似字典中的key,
# 或者数据库中的字段,就是一个占位的作用)
print(p2._fields)  # ('x', 'y')

Color = namedtuple("Color", "red green blue")

# 再次定义命名元组类,其字段由Point的字段加上Color的字段
Pixel = namedtuple("Pixel", Point._fields + Color._fields)
# 创建Pixel对象,分别为x,y,red,green,blue字段赋值
pix = Pixel(11,22,128,255,0)
print(pix)  # Pixel(x=11, y=22, red=128, green=255, blue=0)
