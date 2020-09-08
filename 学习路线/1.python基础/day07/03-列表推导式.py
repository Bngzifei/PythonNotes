"""
列表推导式:生成列表只要一行代码.以表达式的方式来快捷的生成一个列表数据的一种表达式(效率提高了,但是可读性变差了)
格式:[计算公式 for ] 计算公式那肯定是一个字符串了
先执行for的,然后执行计算公式,再丢到[]列表中

列表推导式的应用场景,是对列表中的数据进行过滤(留下想要的数据,剔除不要的)
"""

list1 = [(i+1) for i in range(1,101)]
print(list1)
# 执行顺序是: 1.for --> 2.if --> 3.i**2
list1 = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(list1)



"""生成列表  列表中有10个'666' """
# 推导式不一定使用i,不一定使用range.灵活的很啊
list1 =['666' for i in range(10)]
print(list1)

list1 = ['zhangsan', 'lisi', 'wangwu']
list2 = [name for name in list1 if len(name) > 5]
print(list2)

# 递归就是死循环