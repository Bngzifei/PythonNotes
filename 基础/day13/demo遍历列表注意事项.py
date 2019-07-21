list1 = [10, 20, 30, 40, 50]
# # 就是正在遍历的时候不要进行删除或者增加操作.
# # 不要对一个列表同时进行遍历和增删元素
# # for element in list1:
# #     print(element)
# #     if element == 30 or element == 40:
# #         list1.remove(element)
# # print(list1)
# 法1:
temp_list = []  # 专门把要删除的元素保存起来
# 先遍历列表，记录下需要增删的元素
for element in list1:
	if element != 30 and element != 40:  # 把要的留下
		temp_list.append(element)

# 遍历完列表，再对需要增删的内容进行逐一处理
for temp_element in temp_list:
	list1.remove(temp_element)
print(list1)


# 法2:
# i = 0
# while i < len(list1):  # 动态的取列表的长度,不能写死.
# 	ele = list1[i]
# 	if ele == 30 or ele == 40:
# 		list1.remove(ele)
# 	else:
# 		i += 1
# print(list1)
