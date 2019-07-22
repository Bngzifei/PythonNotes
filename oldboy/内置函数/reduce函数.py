"""

reduce()函数:在py2中直接使用就行,在py3中需要从模块中导入才能使用
就是将一个列表中的元素经过处理 合到一起,最终得到一个元素

map()函数是将一个列表经过处理,最后得到的还是这个列表,只是这个列表中的元素经过了一定的处理

filter()是将一个列表中的某些元素进行筛选过滤,剔除掉不符合条件的元素,最终得到的还是这个列表,列表中的元素是符号条件的.



需求:
"""

# from functools import reduce


# num_l = [4, 2, 3, 100]

# res = 0
# for num in num_l:
# 	res += num
# print(res)

# def reduce_test(list1):
# 	res = 0
# 	for num in list1:
# 		res += num
# 	return res
#
# print(reduce_test(num_l))

# def func(x, y):
# 	return x * y
#
#

# def reduce_test(func1, list1, init=None):
# 	if init is None:
# 		res = list1.pop(0)
# 	else:
# 		res = init
# 	for num in list1:
# 		res = func1(res, num)
# 	return res
#
#
# # print(reduce_test(func, num_l))
# print(reduce_test(lambda x, y: x * y, num_l,20))

from functools import reduce
num_l = [4, 2, 3, 100]

print(reduce(lambda x, y: x + y, num_l, 7))
