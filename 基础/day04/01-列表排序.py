# list1 = [2, 3, 1, 4]
# # key 用来指定排序规则
# # reverse 控制升降序
# list1.sort()  # 默认是升序
# print(list1)
# list1 = [2,3,1,4]
# list1.sort(reverse=True)
# print(list1)
#
# list2 = ["5", 2, 1, "4", 3]
# list2.sort(key=int)  # 让列表中元素在比大小时,按整数类型比较,只是在比较过程中将"5"这个字符 当成数字5
# print(list2)
#
# list3 = ["zhangsan", "lisi", "wangwu"]
# list3.sort(key=len)
# print(list3)
# list3.sort(key=len, reverse=True)  # 按照字符串长度比较大小,让列表中的元素以字符串长度排序
# print(list3)
# list1.reverse()  # 让列表中的元素进行反转,倒置
# print(list1)


























import keyword

print(keyword.kwlist)