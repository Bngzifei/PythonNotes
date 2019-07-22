"""递归
在函数中调用函数本身,默认递归就是一个死循环
在Python中最大递归次数是1000次,其他语言中没有限制


"""

# def func1(a):
# 	print(a)
# 	func1(a + 1)


# func1(1)  # 最大998  报错:RecursionError: maximum recursion depth exceeded while calling a Python object

# 一调用就是回来使用自己,第一次调用的程序一直没有走完
"""1*2*3*4

4*(4-1)*(3-1)*(2-1)

Alt + 1 :关闭/打开Pycharm的侧边栏


在使用递归时候,一定要在特定情况下返回一个具体的值,来结束递归
可读性很差


"""


# result = 1
# for i in range(4, 0, -1):  # 这样就将0排除掉了,因为取不到0
# 	result = result * i
# print(result)
# 性能不好,所以不建议使用,内存飙升.
# 一定要记得结束递归,记得设置条件结束自己调用自己


def func_step(num1):
	if num1 == 1:  # 一定要记得使用的时候递归的起始地方是否有一个return返回值
		return 1  # 在使用递归时候,一定要在特定情况下返回一个具体的值,来结束递归
	return num1 * func_step(num1 - 1)


re = func_step(9)
print(re)
