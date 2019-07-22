"""

# self代表类创建出来的某个对象.在调用方法时,会将调用此方法的对象作为第一个实参传递给self,在方法中使用对象属性时,尽量使用self去操作属性


# self在方法外面时,无法使用.需要使用对象.



阶段性测试的时候,三短一长选长,三长一短选短
"""


class Dog:
	def eat(self):  #在方法中操作对象的属性时,尽量使用self.在类中操作对象的属性的时候也是这样.注意是在同一个类.
		# print('%s吃面包' % dog1.name)
		print('%s吃面包' % self.name)  # self:谁使用就是谁,self是一个特殊的形参.这里的self.name就是Dog类的属性,在创建对象之后对属性进行赋值.所以下面name='小花'


dog1 = Dog()
dog1.name = '小花'
dog1.eat()

dog2 = Dog()
dog2.name = '小白'
dog2.eat()  # 调用方法时,Python解释器会自动把调用此方法的对象作为第一个实参传递给self
