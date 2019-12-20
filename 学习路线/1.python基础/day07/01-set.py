"""
set 无序集合
特点:没有索引, 里面的数据不会有重复
很少使用来表示数据

如果想让列表,元组中没有重复的元素可以把它们转换成set类型
不能转字典类型,因为格式不一样
set 格式:{元素1,元素2}

"""

# set1 = {1, 2, 33, 4, 4, 55}
# print(set1)
# print(type(set1))
# #
# list1 = [1, 23, 4, 5, 3, 66, 2, 333, 3, 3, 3]
# print(list1)
# set2 = set(list1)  # 影响了List的顺序
# print(set2)

# 作业:在不影响列表中元素的位置情况下把列表中的数据进行去重
# find()是字符串
# list1 = [2,3,2]
#
# list2 = [] # 保存没有重复的元素
#
# for element in list1:
# 	if element not in list2:
# 		list2.append(element)
# print(list2)

# 作业:在不影响列表中元素的位置情况下把列表中的数据进行去重
list1 = [2,3,2]

list2 = []  # 保存没有重复的元素
# index:查找列表中元素对应的索引位置
i = 0
while i < len(list1):
	element = list1[i]  # 取出指定索引的元素
	index1 = list1.index(element)  # 取出元素在列表中第一次出现的索引
	if i == index1:  # i是从0开始的有序的,如果地址相等,就添加这个地址对应的元素
		list2.append(element)
	i += 1
print(list2)
