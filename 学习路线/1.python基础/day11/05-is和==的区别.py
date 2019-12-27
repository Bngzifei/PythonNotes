list1 = [1, 2]
list2 = [1, 2]
# list2 = list1
#
if list1 == list2:  # == 是比较数据
	print('yes')
else:
	print('no')

# list2 = list1

# 判断是不是为True False None 尽量用 is   因为这些都是对一个地址进行比较判断,因为判断地址要快
if list1 is list2:  # is 是比较两边的内存地址是否一样
	print('yes')
else:
	print('no')
