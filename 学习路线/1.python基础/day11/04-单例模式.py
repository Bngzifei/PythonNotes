"""

单例模式:一种套路.单个实例对象.创建一次就是一个实例对象.通过这种模式创建出来的实例是同一个.同一个内存地址.类似列表的创建不同对象,操作其中一个,另外一个也会跟着变化
不同的功能模块里面,使用的是同一个对象.很多.py文件里面,多个地方使用同一个实例对象.最常见的就是建立数据库的连接,每个.py文件都是连同一个数据库,建立的连接一般也是同一个.

数据共享:单例,只有一个真正的实例,地址只有一个

购物车模型,不同店铺里 添加食品,添加鞋子,但是还是同一个账户的购物车.

模式:根据实际开发设计的过程总结出来的.

单例: 创建出来的地址是同一个

核心:object的new方法和init只执行一次.

单例的核心思想:就是让object的new方法只能调用一次,后面都是把第一次创建好的实例对象返回.让init方法中定义的实例属性的代码只执行一次.

目的:实现数据共享

object的new方法只调用一次,init方法中定义属性的代码也只调用一次.

应用示例:

1.Python的logger就是一个单例模式，用以日志记录
2.Windows的资源管理器是一个单例模式
3.线程池，数据库连接池等资源池一般也用单例模式
4.网站计数器

"""


class UserInfo:
    __instance = None  # 类属性  此属性来保存创建好的实例对象.设置成私有属性 __不让外部修改
    __has_init = False  # 类属性  默认还未初始化

    def __new__(cls, *args, **kwargs):
        # print(cls)  # <class '__main__.UserInfo'>  隐藏了这个过程# UserInfo.__new__(UserInfo)  # 当前类
        # obj = object.__new__(UserInfo)  # 创建的是UserInfo对象,所以设置成了静态方法,让我们自己去手动控制传递的类对象.默认是调用的自己的.父类被重写了

        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  # 保证只会创建一次.一定要是cls的属性来接收object创建的类对象.

        # 创建的是UserInfo对象,所以设置成了静态方法,让我们自己去手动控制传递的类对象.默认是调用的自己的.父类被重写了

        return cls.__instance  # 这样就只会创建一次.这里不能缩进到if里面,否则第2个就是None

    def __init__(self):  # 2次

        if UserInfo.__has_init is False:  # 一直都是类属性__has_init
            self.name = '超哥'
            print(self)
            # print(UserInfo)
            UserInfo.__has_init = True  # True: 设置成 已经初始化  类属性

        # if self.__has_init is False:  #  使用self就会生成一个和类属性同名的实例属性. 所以这里不要这么写.这样的self就是实例对象在访问类属性__has_init了.(因为实例对象是可以访问类属性的.)
        # 	print(self)
        # 	self.name = '超哥'
        # 	self.__has_init = True  # 已经初始化 这样self代表的实例对象就不是类对象.这样赋值操作就是直接给实例对象创建了一个和类属性同名的实例属性值.第一次可以访问,第二次之后就不一定了.


        # UserInfo.__new__(UserInfo)  #  就是递归了,死循环


user1 = UserInfo()
user2 = UserInfo()
user3 = UserInfo()

user4 = UserInfo()
user5 = UserInfo()
user6 = UserInfo()

# print(UserInfo.__has_init)
# print(user1.__has_init)
user1.name = '小5小小超'
user2.name = '小4小小超'
user3.name = '小3小小超'
user4.name = '小2小小超'
user5.name = '小1小小超'


# print(user1)  # 2个
# print(user2)
# print(user3)  # 2个
# print(user4)
# print(user5)  # 2个
# print(user6)
# print(user2.name)



def singleton(cls):
    """单例类装饰器"""
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton