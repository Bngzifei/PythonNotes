"""
前面实现的make_averager函数的方法效率不高.在前面示例中,我们把所有值
存储在历史数列中,然后在每次调用averager时使用sum求和.
更好的实现方式是,只存储目前的总值和元素个数,然后使用者两个数计算均值.


"""

# 计算移动平均值的高阶函数,不保存所有历史值,但有缺陷
def make_averager():
	count = 0  # 不可变类型
	total = 0  # 不不可变类型
	
	def averager(new_value):
		nonlocal count,total  # 使用nonlocal关键字使其可以重新绑定,成为自由变量
		count += 1  # 实际这里是给count 重新赋值了
		total += new_value
		return total / count

	return averager


avg = make_averager()
print(avg(10))

"""
问题是,当count是数字或任何不可变类型时,count += 1 语句的作用其实与count = count +1
一样.因此,我们在averager的定义体中为count赋值了,这会把count变成局部变量.total变量也
受这个问题影响.

当series = [] 的时候没遇到这个问题,因为我们没有给series赋值,我们只是调用series.append,
并把它传给sum和len.也就是说,我们利用了列表是可变的对象这一事实.

但是对数字,字符串,元组等不可变类型来说,只能读取,不能更新.如果尝试重新绑定,例如
count = count + 1(重新绑定其实就是赋值操作,=号左边的count和=号右边的count是不一样的
本质上是两个地址不同的对象),其实会隐式创建局部变量count,这样count就不
是自由变量了,因此不会保存在闭包中.

为了解决这个问题,Python3引入了nonlocal声明,它的作用是把变量标记为自由变量,即使在函数中为
变量赋予新值了,也会变成自由变量.如果为nonlocal声明的变量赋予新值,闭包中保存的绑定会更新.


如何对付没有nonlocal的Python2?

这种处理方式就是把内部函数需要修改的变量如count和total存储为可变对象(如字典或简单的实例),
并且把那个对象绑定给一个自由变量.



"""
