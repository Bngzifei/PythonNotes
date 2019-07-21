"""

存储多个数据,每个数据称之为元素
格式:[元素1,元素2...]
列表中尽可能存储同类型数据,且代表的含义要一致.实际上可以存储不同类型的数据
获取元素:列表[索引]
常用的标红:整理一下好复习

增.删.改.查



"""

list1 = ['11', '22', 18, 1.75, True]
print(type(list1))
print(list1[4])


l1 = list()
print(l1)




# IndexError: list index out of range
# print(list1[8])  索引超出list范围,报错

list1[0] = '你大爷'  # 修改元素的值
print(list1)


