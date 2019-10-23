"""
Python的富比较方法包括__lt__、__gt__、__le__、__ge__、__eq__和__ne__六个方法，
分别表示：小于、大于、小于等于、大于等于、等于和不等于，对应的操作运算符为:<、>、<=、>=、==和!=。那么是否象普通数字运算一样，
这些符号之间存在关联关系呢？如“小于等于”是否就包含了“小于”？比较符号之间有必须的包含关系吗?本次对富比较方法__eq__和__ne__之间的关系进行分析：

Python建议__eq__和__ne__之间是非的关系(就是互斥,取反,逆运算的关系)，__ne__的方法实现时就应该调用__eq__取反来完成,
但如果开发者不遵循该要求实际上也是可以的。


案例分析：
1、如果开发者Pyhon在自定义类中实现了__eq__和__ne__这两个方法，则“==”和“!=”的两个对象比较分别调用了这两个方法进行比较。代码如下：

"""


class Car():
    def __init__(self, carname, oilcp100km, price):
        self.carname, self.oilcp100km, self.price = carname, oilcp100km, price

    def __eq__(self, other):
        """就是判等运算"""
        print("execute __eq__")
        return self.price == other.price

    def __ne__(self, other):
        """就是不相等判断"""
        print("execute __ne__")
        return self.price != other.price


car1, car2, car3, car4 = Car('爱丽舍', 8, 10), Car(
    '凯美瑞', 7, 27), Car('爱丽舍', 8, 10), Car('途观', 12, 27)

cc = car1 == car2
print(cc)
cc1 = car1 != car2
print(cc1)
cc2 = car2 == car4
print(cc2)


"""
输出结果:
execute __eq__
False
execute __ne__
True
execute __eq__
True

"""


"""
2、如果开发者Pyhon在自定义类中实现了__eq__方法，未实现__ne__方法，则“==”和“!=”都是__eq__方法，
调用的两个对象比较都调用__eq__方法进行比较，不过后者是对__eq__取反。代码如下：

"""

print("---------------------------")


class Car():
    def __init__(self, carname, oilcp100km, price):
        self.carname, self.oilcp100km, self.price = carname, oilcp100km, price

    def __eq__(self, other):
        """就是判等运算"""
        print("execute __eq__")
        return self.price == other.price


car1, car2, car3, car4 = Car('爱丽舍', 8, 10), Car(
    '凯美瑞', 7, 27), Car('爱丽舍', 8, 10), Car('途观', 12, 27)

cc = car1 == car2
print(cc)
cc1 = car1 != car4  # 不过后者是对__eq__取反,实现的效果和__ne__是一样的(ne:就是 not equal 的缩写)
print(cc1)


"""

3、如果开发者Pyhon在自定义类中实现了__ne__方法，未实现__eq__方法，则“!=”调用__ne__方法，而eq则调用系统内置的“==”对应的方法，
老猿初步分析应该是调用“is”，还没求证。代码如下：

"""

print("************************")


class Car():
    def __init__(self, carname, oilcp100km, price):
        self.carname, self.oilcp100km, self.price = carname, oilcp100km, price

    def __ne__(self, other):
        """仅实现了不等"""
        print("execute __ne__")
        return self.price != other.price


car1, car2, car3, car4 = Car('爱丽舍', 8, 10), Car(
    '凯美瑞', 7, 27), Car('爱丽舍', 8, 10), Car('途观', 12, 27)

cc = car1 == car3  # 判断相等,会去调用系统内置的"=="对应的方法,不是判等,是判断 id 是否一致的  is  机制
print(cc)
cc1 = car1 != car3  # 相等成立,不等取反为False
print(cc1)
