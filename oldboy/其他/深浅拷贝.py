# s = [1, 'alex', 'alvin']
# s1 = [1, 'alex', 'alvin']
#
# s1[0] = 2  # 修改,独立的不影响s
#
# print(s)
# print(s1)

"""copy()"""

# s = [1, 'alex', 'alvin']
# s2 = s.copy()
# s2[0] = 0
#
#
# print(s)
# print(s2)


# s = [[1, 2], 'alex', 'alvin']
# s3 = s.copy()
# s3[1] = 'linux'  修改字符串的时候没变化
# s3[0] = 20
# s3[0][1] = 3  # 修改列表的时候变了,说明s和s3之间存在关联性,s和s3之间不是两份独立的内存地址
# print(s3)
# print(s)


"""赋值:存的是内存地址,不是具体的数据值,赋值也是把内存地址传给变量,变量就是一个盒子,用来装内存地址"""
# a = 1
# b = a
#
# print(id(1))
# print(id(a))
# print(id(b))
# b = 2
# print(id(b))

"""浅拷贝只会拷贝第一层,字典列表都是一样的 容器类型的数据复制就是浅拷贝,你改我也改."""
# a = [[1, 2], 3, 4]
# # a[0] ---> [1,2] 的内存地址是一个列表的地址
# # b = a.copy()  # 浅拷贝  等价于 b = a[:]
# b = a[:]
# b[1] = 'abc'
# print(a)  # a 不变
# print(b)
# b[0][1] = 'abc'
# print(a)  # a 不变
# print(b)  # b 变化

"""示例:"""
import  copy
husband = ['xiaoli', 123, [15000, 9000]]

wife = husband.copy()  # 浅拷贝
wife[0] = '你大爷'
wife[1] = 589

husband[2][1] -= 5000
# print(wife)
# print(husband)

# wife = husband  # 都会变
#
# wife[0] = '你大爷'
# wife[1] = 589
#
# husband[2][1] -= 5000
# print(wife)
# print(husband)
"""浅拷贝:只复制第一层,深拷贝:递归的,全部都复制无论有多少层,全部都会复制"""
# xiao = copy.copy(husband)  # 浅拷贝
# xiao[0][1] = '1234'  # TypeError: 'str' object does not support item assignment,字符串是不可变类型,和元组一样,第一次创建之后的值就不能再次赋值了.
# xiao[2][0] -= 300
# print(xiao)
# print(husband)  # 不变,[]里面的会和xiao一样,存的是一个容器的内存地址,容器的内存地址不会变,但是里面的数据是可以被修改的


xiao = copy.deepcopy(husband)
xiao[0] = '1234'
xiao[2][0] -= 300
print(xiao)  # 只是修改自己的
print(husband)  # 原来的数据不会变,深拷贝,递归的全部拷贝来,独立的一份,不会共享一份数据的内存地址
