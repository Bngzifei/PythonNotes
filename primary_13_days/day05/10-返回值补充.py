print('---------')
"""
注意点一:
1.不要在return同一个缩进的后面去直接去写代码,因为执行不到. return有结束函数运行的作用.
break:在if里面也是一样的道理(同一个缩进).if里面和break(continue也一样)同一个缩进的后续代码不会被执行(break终止执行后续代码,终止循环continue终止执行后续代码)
"""


# def func1():
# 	print('lll')
# 	return 'hello'  # 当函数中一旦执行到return就相当于函数执行完成了
# 	print('hh')  # 注意颜色不同了,变成了深黄色,意味着这里编写的代码出问题了,表示这里的代码不会被执行到,无效代码
#
#
# func1()

"""
注意点二:
2.return 后面可以一个值都不返回,或者同时返回多个值

return 后面啥也没有时候 -> 作用:返回值.提前结束函数

def func1():
	return


func1()


"""

# def func1():
# 	return 10,20  # 返回多个值,组包.元组
#
# func1()

"""注意点三:
可以在一个函数中使用多个return(配合if..else..使用),
否则只执行第一个return.
只会执行到一个(return结束函数的作用)


"""

# def even_num(a):
# 	if a % 2 == 0:
# 		return 'ou'
# 	else:
# 		return 'ji'
#
#
# print(even_num(11))

ret = 10
print('')
print('11', '333', 222)  # 可以输出多个值
