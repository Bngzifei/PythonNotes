print('可变与不可变:')
"""
可变类型:存储空间中的数据可以被修改,并且内存地址不变,特点:对可变类型的数据进行修改操作时,不用接收新值  ---> 在银行原有账户再存300万
	列表.append() = 号左边不用新的变量来接收.即 o = 列表.append()这种格式有误.
列表和字典

不可变类型:存储空间的数据不能被修改 特点:对不可变进行操作时,一般都需要接收新值
新的字符串 = 字符串
.replace()

元组和字符串即其他的数值(int.float.boole)类型  接收新值替换掉

"""
# list1 = [1, 2]
# print(id(list1))  # 本该以16进制展示,2829954001928
# list1.append(3)
# print(id(list1))
#
# def func1():
# 	pass
#
#
# # print(func1)  # <function func1 at 0x00000292E4A72E18>
# dict1 = {"m":2}
# print(id(dict1))
# dict1['n'] = 30
# print(id(dict1))


str1 = 'hello'
print(id(str1))  # 2720803889312
str2 = str1.replace('l', 'z')
str1 = str1.replace('l', 'z')  # str1重新赋值了,新值覆盖旧值,指向另外一个内存地址了
print(id(str1))  # 2720803889704
print(str2)  # hezzo
print(id(str2))  # 2720803891104
