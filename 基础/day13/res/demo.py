list1 = [10, 20, 30, 40, 50]

# 不要对一个列表同时进行遍历和增删元素
# for element in list1:
#     print(element)
#     if element == 30 or element == 40:
#         list1.remove(element)
# print(list1)

temp_list = []
# 先遍历列表，记录下需要增删的元素
for element in list1:
    if element == 30 or element == 40:
        temp_list.append(element)

# 遍历完列表，再对需要增删的内容进行逐一处理
for temp_element in temp_list:
    list1.remove(temp_element)
print(list1)