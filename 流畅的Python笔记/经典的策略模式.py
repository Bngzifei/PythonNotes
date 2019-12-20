"""
符合模式并不表示做得对.

虽然设计模式与语言无关,但这并不意味着每一个模式都能在每一门语言中使用.

所用的语言决定了哪些设计模式可用.

若我们采用过程式语言,可能就要包括诸如"集成""封装"多态"的设计模式.相应地,
一些特殊的面向对象语言可以直接支持我们的某些模式.具体而言,Norvig建议在有
一等函数的语言中重新审视"策略","命令","模板方法"和"访问者"模式.通常,我们
可以把这些模式中涉及的某些类的实例替换成简单的函数,从而减少样板代码.


方法或者变量的命名:
	一定得言简意赅,能体现出大概意思
	变量得体现实际含义和对应的数据类型,比如案例id列表就应该起名为:case_ids_list,
	方法和函数的名字必须是  动宾结构.即 谓语 + 宾语的结构
	比如从json中获取案例信息,就应该起名为:get_case_info_from_json



重构"策略"模式:

	如果合理利用作为一等对象的函数,某些涉及模式可以简化,策略模式就是其中一
	个很好的例子.

"策略模式"的概述:
	
	定义一系列算法,把它们一一封装起来,并且使它们可以相互替换.本模式使得算法可以
	独立于使用它的客户而变化.

电商领域有个功能明显可以使用"策略"模式,即根据客户的属性或订单中的商品计算折扣.

	具体策略由上下文类的客户选择.在这个示例中,实例化订单之前,系统会以某种方式选择
	一种促销折扣策略,然后把它传给Order构造方法.具体怎么选择策略,不在这个模式的职责
	范围内.


"""


# 实现Order类,支持插入式折扣策略
from abc import ABC,abstractmethod
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
	"""上下文"""
	def __init__(self,customer,cart,promotion=None):
		self.customer = customer
		self.cart = list(cart)
		self.promotion = promotion

	def total(self):
		"""订单总额"""
		if not hasattr(self,"__total"):
			self.__total = sum(item.total() for item in self.cart)
		return self.__total

	def due(self):
		"""应付款"""
		if self.promotion is None:
			discount = 0
		else:
			discount = self.promotion.discount(self)

		return self.total() - discount

	def __repr__(self):
		fmt = "<Order total:{:.2f} due: {:.2f}>"
		return fmt.format(self.total(),self.due())



class Promotion(ABC):
	"""策略:抽象基类"""

	@abstractmethod
	def discount(self.order):
		"""返回折扣金额(正值)"""

# 第一个具体策略
class FidelityPromo(Promotion):
	"""为积分为1000或以上的顾客提供5%折扣"""

	def discount(self,order):
		return order.total() * .05 if order.customer.fidelity >= 1000 else 0


# 第二个具体策略
class BulkItemPromo(Promotion):
	"""单个商品为20个或以上时提供10%折扣"""

	def discount(self,order):
		discount = 0
		for item in order.cart:
			if item.quantity >= 20:
				discount += item.total() * .1
		return discount


# 第三个具体策略

class LargeOrderPromo(Promotion):
	"""订单中的不同商品达到10个或以上时提供7%折扣"""

	def discount(self,order):
		distinct_items = {item.product for item in order.cart}
		if len(distinct_items) >= 10:
			return order.total() *.07
		return 0


"""
说明:注意,在示例中,把Promotion定义为抽象基类,这么做事为了适应@abstractmethod
装饰器,从而明确表明所用的模式.

在Python3.4中,声明抽象基类最简单的方式是子类化abc.ABC.从Python3.0到Python3.3,
必须在class 语句中使用metaclass=关键字(例如,class Promotion(metaclass=ABCMeta):)

"""










