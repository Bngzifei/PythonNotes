"""一.元组是自动组包的默认类型"""
a = 10, 20  # 如果把多个值赋值给一个变量时,它会自动把多个数据组包成元组
print(a)  # (10,20)
print(type(a)) # tuple
tuple1 = (10, 20, 30)  # ValueError: too many values to unpack (expected 2)
a, b, c = tuple1  # 如果一个元组赋值给多个变量时,如果元组中元素个数和变量数一致,会自动赋值给每个变量,解包,拆包
print(a)
print(b)
print(c)
组包是应用最多的地方
# a = 10  # 20
# b = 20  # 10
#
# """第一种"""
#
# temp = a
# a = b
# b = temp
# print(a)
# print(b)
# """不能用中间变量"""
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)
# """要求,不使用中间变量交换a,b的值: 第三种(Python独有)"""
# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)

"""场景2:字符串格式"""
price = 7.5
weight = 8.0
tuple1 = (price, weight)
print("单价:%.2f,重量:%.1f" % (price, weight))
print("单价:%.2f,重量:%.1f" % tuple1)
"""场景3:保证数据的安全性"""
list1 = [10, 20, 30]
# 类型转换转换 成元组
tuple1 = tuple(list1)
print(tuple1)
# 元组也可以转换成列表
"""字符串转换"""
# a = str(1.5)
# print(a)
