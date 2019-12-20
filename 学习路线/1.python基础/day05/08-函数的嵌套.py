print('函数嵌套:')
"""函数嵌套"""

"""
函数的定义和函数的调用,在执行代码时,必须先执行函数的定义,才能正常的执行它的调用
函数的定义和调用,指的是执行顺序,不是书写顺序.即下面的实例中当调用func2()时,遇到func1()函数部分,计算机会自动去查找(与func1()func2()的书写顺序无关)func1()函数是否定义过,所以func1()写到func2()后面也不会有影响.


"""

# def func2():
#
# 	print("func2开始")
#
# 	func1()
#
# 	print("func2结束")
#
#
# def func1():
# 	print("func1开始")
#
# 	print("func1结束")
#
#
# func2()

"""输出* :"""

"""
新函数:不要破坏原来的函数
各自独立

"""


def print_line(count, char):
	"""输出一行任意数量的任意图案"""
	print(char * count)


# count1:一行的个数,char1:输出的单个字符 n:输出的行数
def print_lines(count1, char1, n):
	"""输出多行图案"""
	i = 1
	while i < n:
		print_line(count1, char1)
		i += 1


print_lines(5, "$", 12)  # 记得和形参的位置对应.意思就是每行输出5个$,一共12行
# print_lines(10, "#", 13) # 意思就是每行输出10个#,一共13行
