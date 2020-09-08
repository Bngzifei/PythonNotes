# -----------------------------------------------修改自由变量:了解即可---------------------------------->
def line(k, b):
	# data = [k]
	def line_in(x):
		# py3 提供的关键字 专门用来修改自由变量
		# 非本地变量  非本地不一定是全局变量,也可能是另外一个函数内部的内部变量<本地变量>
		nonlocal k
		# py2中没有这个关键字,只能将需要修改的变量放到列表中<间接>
		# data[0] += 1
		k += 1  # 不可变类型的k需要使用nonlocal 可变类型<就是[],{},字典等,>的不需要加nonlocal

		print('y = %d' % (k * x + b))

	return line_in


l1 = line(1, 1)
# l1(9)  # local variable 'k' referenced before assignment 本地变量在赋值之前被引用了

# ------------------------扩展: 查看闭包中的资自由变量的值--------------------------->

# print(l1.__closure__)
# # (<cell at 0x0000017096A086A8: int object at 0x00000000658460E0>,
# <cell at 0x0000017096A08708: list object at 0x00000170969D4C08>,
# <cell at 0x0000017096A086D8: int object at 0x00000000658460E0>)
# print(l1.__closure__[0].cell_contents)
# print(l1.__closure__[1].cell_contents)
# print(l1.__closure__[2].cell_contents)

"""
推荐的经典书籍：
《流畅的python》
《Python核心编程》 第二版  不要看第三版 

要求：硬着头皮看两遍

"""


def make_avg():
	data = list()

	def addnumber(value):
		data.append(value)
		total = sum(data)
		# print(data)  加print进行调试理解
		return total / len(data)

	return addnumber


# myavg = make_avg()
# print(myavg(100))
# print(myavg(200))
# -------------------------------------------可变类型与不可变类型----------------------------------------------------->
# str1 = 'lll'
# str1[0]=6  # TypeError: 'str' object does not support item assignment  变量创建之后它内部的元素不能二次赋值就是  不可变类型

list1 = [1, 2, 3]
list1[0] = 33  # 内部元素可以被二次赋值,就是可变类型
