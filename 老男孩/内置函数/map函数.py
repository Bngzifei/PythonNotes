num1 = [1, 2, 10, 5, 3, 7]
num2 = [1, 52, 12, 56, 3, 7]


# l1 = []
# for item in num1:
# 	l1.append(item ** 2)
# print(l1)
def add_one(x):
	return x + 1


# # lambda x: x-1
def red_one(x):
	return x - 1


def mi(x):
	return x ** 2


def map_test(list1, func):  # 记得这里func是传了一个函数名
	l1 = []
	for item in list1:
		res = func(item)  # 利用func函数处理列表中的每个元素
		l1.append(res)
	
	return print(l1)


map_test(num2, mi)  # 这样就实现了功能也封装出来的效果了.
map_test(num2, lambda x: x ** 2)  # 这样就实现了功能也封装出出来的效果了.
map_test(num2, add_one)
map_test(num2, lambda x: x + 1)
map_test(num2, red_one)
map_test(num2, lambda x: x - 1)
# 内置的map函数非常精简,值得研究,直接传一个功能函数名,一个可迭代的数据类型进去就可以
map(red_one, num2)  # 注意:在py2中map处理数据之后的结果就是一个list列表py3是一个迭代器,
# 需要加list进行转化
msg = 'sdsjshdhfvdf'
res = map(lambda x: x.upper(), msg)
print(list(res))

# res = map(lambda x:x - 9, num1)
# print('内置函数map,处理结果', res)
# # for i in res:
# # 	print(i)
# print(list(res))
# 注意:map(func,iter1,iter2) 里面的func为函数名,iter1,iter2为可迭代类型的数据
# 所谓可迭代类型的数据就是能够使用for循环去遍历.学过的数据类型中只有list列表,tuple元组,str字符串是可迭代类型
# 其他的字典dict,int,float不是可迭代类型.主要还是看这个数据类型是不是有序,能够使用for循环进行有序的遍历
