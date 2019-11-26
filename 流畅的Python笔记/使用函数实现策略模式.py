"""
在经典实现方式中,每个具体的策略都是一个类,而且都只定义了一个方法,即discount.
此外,策略实例没有状态(没有实例属性).你可能会说,它们看起来像是普通的函数---的
确如此.

下面的示例是对经典实现方式的重构.把具体策略换成了简单的函数,而且去掉了Promo
抽象类.

"""
from collections import namedtuple

Customer = namedtuple("Customer","name fidelity")

class LineItem:

	def __init__(self,product,quantity,price):
		self.product = product
		self.quantity = quantity
		self.price = price

	def total(self):
		return self.price * self.quantity

class Order:

	def __init__(self,customer,cart,promotion=None):
		self.customer = customer
		self.cart = list(cart)
		self.promotion = promotion

	def total(self):
		if not hasattr(self,"__total"):
			self.__total = sum(item.total() for item in self.cart)
		return self.__total

	def due(self):
		"""应付金额"""
		if self.promotion is None:
			discount = 0
		else:
			discount = self.promotion.discount(self)

		return self.total() - discount

	def __repr__(self):
		fmt = "<Order tota:{:.2f} due:{:.2f}>"
		return fmt.format(self.total(),self.due())

# 下面三个函数就是具体的策略
def fidelity_promo(order):
	"""为积分为1000或以上的顾客提供5%的折扣"""
	return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
	"""单个商品为20个或以上时提供10%折扣"""
	discount = 0
	for item in order.cart:
		if item.quantity >= 20:
			discount += item.total() *.1
	return discount

def large_order_promo(order):
	"""订单中的不同商品达到10或以上时提供7%折扣"""
	# 集合推导式:直接从列表(或可迭代对象)转为了集合
	distinct_items = {item.product for item in order.cart}
	if len(distinct_items) >= 10:
		return order.total() * .07
	return 0

"""
说明:计算折扣只需调用self.promotion()
没有抽象类
各个策略都是函数.

说明:
	 值得注意的是,策略对象通常是很好的享元(flyweight).

	 享元:
		享元是可共享的对象,可以同时在多个上下文中使用.共享是推荐的做法.这样不必在
	 每个新的上下文中使用相同的策略时不断新建具体策略对象,从而减少消耗.

	 在复杂的情况下,需要具体策略维护内部状态时,可能需要把"策略"和"享元"模式结合起来.
	 但是,具体策略一般没有内部状态,只是处理上下文中的数据.此时,一定要使用普通的函数,别去
	 编写只有一个方法的类,再去实现另一个类声明的单函数接口.函数比用户定义的类的实例轻量.
	 而且无需使用"享元"模式,因为各个策略函数在Python编译模块时只会创建一次.普通的函数也是
	 "可共享的对象,可以同时在多个上下文中使用".


找出模块中的全部策略:
	
	在Python中,模块也是一等对象,而且标准库提供了几个处理模块的函数.Python文档是这样说明
	内置函数globals的.

	globals():

		返回一个字典,表示当前的全局符号表.这个符号表始终针对当前模块.(对函数或方法来说,是指定义它们的模块,
		而不是调用它们的模块)

"""

# 内省模块的全局命名空间,构建promos列表
promos = [globals()[name] for name in globals() if name.endswith("_promo") and name != "best_promo"]

def best_promo(order):
	"""选择可用的最佳折扣"""
	return max(promo(order) for promo in promos)

"""
inspect.getmembers函数用于获取对象(这里是promotions模块)的属性.第二个参数是可选的判断条件(一个布尔值函数).
我们使用的是inspect.isfunction,只获取模块中的函数.

动态收集促销折扣函数更为显示的一种方案是使用简单的装饰器

"""

promos = [func for name,func in
 inspect.getmembers(promotions,inspect.isfunction)]


def best_promo(order):
	"""选择可用的最佳折扣"""
	return max(promo(order) for promo in promos)