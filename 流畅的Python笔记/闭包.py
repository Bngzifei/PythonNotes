"""
在博客圈,人们有时会把闭包和匿名函数弄混.

在函数内部定义函数不常见,直到开始使用匿名函数才会这样做.而且,只有涉及嵌套函数时
才有闭包问题.因此,很多人是同时知道这个两个概念的.




其实,闭包指延伸了作用域的函数,其中包含函数定义体的引用.但是不在定义体中定义的非
全局变量.函数是不是匿名的没有关系,关键是它能访问定义体之外定义的非全局变量.
"""

class Averager():

	def __init__(self):
		self.series = []

	def __call__(self,new_value):
		self.series.append(new_value)
		total = sum(self.series)
		return total/len(self.series)


"""
Averager的实例是可调用对象:
初始化的时候不需要参数,但是只要 实例对象(调用__call__方法的参数)的时候就需要给__call__
方法中的参数指定了.
"""

# avg = Averager()

# print(avg(10))  # 10.0
# print(avg(11))  # 10.5
# print(avg(12))  # 11.0



# 计算移动平均值的高阶函数(函数内部定义新的函数)
def make_averager():
	# 注意:series是make_averager函数的局部变量,因为在这个函数的
	# 定义体中初始化了series: series = []
	series = []

	def averager(new_value):
		series.append(new_value)
		total = sum(series)
		return total/len(series)
	# 只要这里执行了return ,那么就意味着 定义的局部变量 series = []销毁内存数据了
	return averager

# 看看这个效果:调用make_averager函数实际就是调用averager的引用.
avg = make_averager()

# avg = averager 说明这里的avg就是averager函数,若想调用averager函数,
# 那么就需要  avg(new_value),所以:
print(avg(15))
print(avg(16))
print(avg(17))




"""
注意:这两个示例有共同之处:调用Averager()或make_averager()得到一个可调用对象avg,
它会更新历史值,然后计算当前均值.在第一个示例中,avg是Averager的实例,在第二个示例中,
它是内部函数averager.不管怎样,我们都只需调用avg(n),把n放入系列值中,然后重新计算
均值.


Averager类的实例avg在哪里存储历史值很明显:self.series实例属性.但是第二个示例中的
avg函数在哪里寻找series呢?

注意:series是make_averager函数的局部变量,因为在这个函数的
定义体中初始化了series: series = [].可是,调用avg(10)时,make_averager函数已经返回了,
而他的本地作用域也一去不复返了.



def averager(new_value):
	# 注意这里的series是自由变量
	series.append(new_value)
	total = sum(series)
	return total/len(series)


在averager函数中,series是自由变量(free variable)这是一个技术术语,指未在本地作用域中
绑定的变量.

averager的闭包延伸到那个函数的作用域之外,包含自由变量series的绑定


审查返回的averager对象,我们发现Python在__code__属性(表示编译后的函数定义体)中保存局部变量
和自由变量的名称.




"""


# 审查make_averager创建的函数
print(avg.__code__.co_varnames)  # ('new_value', 'total')
print(avg.__code__.co_freevars)  # ('series',) 查看自由变量是哪些


"""
series的绑定在返回的avg函数的__closure__属性中.avg.__closure__中的各个元素对应于
avg.__code__.co_freevars中的一个名称.这些元素是cell对象,有个cell_contents属性,保存着真正
的值.

这些属性的值如下所示:
"""

print(avg.__code__.co_freevars)  # ('series',)
print(avg.__closure__)  # (<cell at 0x0061CD10: list object at 0x002945D0>,)
print(avg.__closure__[0].cell_contents)  # [15, 16, 17]


"""
综上,闭包是一种函数,它会保留定义函数时存在的自由变量的绑定,这样调用函数时,虽然定义作用域不可用了,
但是仍能使用那些绑定.(就是找了个家伙来代替定义的那个变量,定义的变量不能用了,但是这个家伙还是可以使用的)

注意:只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量.


"""