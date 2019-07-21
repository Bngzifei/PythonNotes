"""
给定一个包括 n 个整数的数组<就是list列表> nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

1.>就是找最近的三个数,然后返回这三个数的和

2.>找三个数,求和,这个  和 - target 的差 最小
"""
# import math

# nums = [-1, 2, 1, -4]
# target = 1
# nums.append(target)
# list2 = sorted(nums)
# print(list2)
# print('目标数的索引是:', list2.index(target))
# a1 = list2.index(target) + 1
# b1 = list2.index(target) - 1
# sum1 = list2[a1] + list2[b1]
# print('最近的两个数的和是:', sum1)
# b2 = list2.index(target) - 2
# a2 = list2.index(target) + 2
# print(list2[a2])
# print(list2[b2])
#
# if abs(list2[b2]) <= abs(list2[a2]):  # 绝对值小的离的近
# 	sum2 = sum1 + list2[b2]
# else:
# 	sum2 = sum1 + list2[a2]
#
# print('最后的和是:', sum2)

from itertools import combinations  # 导入组合模块

nums = [-1, 2, 1, -4]
target = 1
list1 = []
list2 = []
list3 = []

# 一个组合
for i in combinations(nums, 3):  # 返回一个可迭代对象
	# res = ''.join(i)  # 这是字符串拼接
	list2.append(i)  # 添加可迭代对象
# print(list2)

for j in list2:
	g = list(j)
	list3.append(g)
print(list3)


def zuixiao(zuhe):
	dict1 = {}
	for i in zuhe:
		# print(i)
		sum1 = sum(i)
		d = abs(sum1 - target)
		dict1[d] = i
	print('最小距离是:', d)
	key = sorted(list(dict1.keys()))[0]
	return print('对应的三个数是:',dict1[key])


zuixiao(list3)


# def three_count(nums):
# 	# for _ in range(2):
# 	for item in nums:
#
# 		index = random.randint(0, len(nums) - 1)  # 随机索引
# 		list1.append(nums[index])
# 		nums.pop(index)
# 		if len(nums) == 1:
# 			break
# 		# print('3个元素的列表是;', list1)
# 		# print('原来的列表是:', nums)
# 	print('3个元素的列表是:', list1)
# 	return list2.append(list1)
# three_count(nums)
# list2.append(three_count(nums))
# print(list2)
# while True:
# 	list2.append(three_count(nums))
# 	print(list2)

# def zuhe_sange(list1):
# 	"""三个元素的组合情况"""
# 	list2 = []
# 	for i in list1:
# 		if len(list2) == 3:
# 			break
# 		list2.append(i)
# 		# index = list1.index(i)
# 		# list1.pop(index)
# 	print(list2)
# zuhe_sange([-1, 2, 1, -4])
#



# print('3个元素的列表是;', list1)

# for j in range(4):
# 	list2.append(list1)
# print(list2)
