"""慎用eval()函数,因为如果将一个字符串转换回来,如果这个字符串原来是一个方法(函数),
那么在转换回方法之后会非常不安全,可能一不下心就执行了,然后程序的数据就有可能出问题.比如是一个删除的函数等等"""

# print(__import__('os').getcwd())
print(__import__('os').listdir())
# 字符串转成了方法
a = input('请输入:')
print(a)
print(type(a))  # <class 'str'>
print('-' * 30)
# b = eval(a)
print(eval(a))  # eval() 将字符串转回到原来的数据格式,比如原来是[]列表,就可以将str形式的[]列表. {}字典 ()元组 转换回 [].{}.() 即字符串形式的字典,列表等等再转换回 字典,列表
print(type(eval(a)))  # <class 'list'>
