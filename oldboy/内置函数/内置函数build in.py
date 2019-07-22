print('内置函数build in...')
"""
all():只能传入一个实参,比如一个列表,字典,int型等等
作用:只要这个数据类型中每一个元素不为0,None,''空字符串就返回boole值 True
但是,如果这数据类型是空,比如空列表,空字典,空的字符串,也返回True.

"""
# print(all([]))
# print(all(''))
# print(all({}))
# print(all([1, 2, 3]))
# print(all([1, 2, 3, 0]))
# print(all([1, 2, 3, 4, None]))
# print(all([1, 2, 3, 4, '']))

"""
any():有一个为真就返回True

"""

# print(any([0, '', 1]))  # True
# print(any([0, '', 0]))  # False
# print(any([0, '', ' '])) # True
# print(any([0, '', None]))  # False

"""
enumerate():返回一个可迭代序列中元素的索引值和对应的元素,组成一个元组序列.

"""
# print(list(enumerate({'1': 1, '2': 2})))  # [(0, '1'), (1, '2')]
# print(list(enumerate([1,5,7,9,0])))  # [(0, 1), (1, 5), (2, 7), (3, 9), (4, 0)]

"""
bin():将数字转换为二进制数值,只能接受传入的实参为数值类型
"""
# print(bin(5))  # 十进制转成二进制数值
# # print(bin('12'))  # TypeError: 'str' object cannot be interpreted as an integer
# print(bin(0xA))  # 16进制数字转成二进制  输出: 0b1010
# print(bin(0o7))  # 8进制数字转成二进制  返回 0b111

"""
bool():布尔运算
"""
# print(bool())  # False
# print(bool(None))  # False
# print(bool(0))  # False
# print(bool(''))  # False
# print(bool(' '))  # 空格符为True
# print(bool([]))  # False
# print(bool({}))  # False
# print(bool(1))  # True
# print(bool((1, 2)))  # True
# print(bool('111'))  # True

"""
bytes(): 将字符串转成二进制字节流,常用于网络中的数据流传输,文件的读写等等
一个汉字在utf-8的编码方式中占3个字节,而在gbk的编码方式中占用2个字节.

繁体字使用big5编码

gbk和gb2312的编码输出结果相同.window下一般采用gbk,因为更省内存资源

Python3中默认采用utf-8编码  encode()和decode()函数中无参数说明编码采用utf-8的编码格式

注意:编码解码必须一致,否则乱码

在内存和硬盘中都是Unicode的方式存储传输数据.
bytes也是二进制数据,bit是比特位

bytes:字节
bit:位
1个bytes占用8个bit位

网络中传输数据就是利用高低电压进行数据传输,就是常常看到的那种一闪一闪的灯亮和灯灭.

"""
# name = '李斌'
# print(bytes(name, encoding='utf-8'))  # 输入的字符串类型需要提供encoding的实参,来指定编码方式
# print(bytes(name, encoding='utf-8').decode())  # 输入的字符串类型需要提供encoding的实参,来指定编码方式
# print(bytes(name, encoding='gbk'))  # 输入的字符串类型需要提供encoding的实参,来指定编码方式
# print(bytes(name, encoding='gb2312'))  # 输入的字符串类型需要提供encoding的实参,来指定编码方式
# print(bytes(name, encoding='gb2312').decode('gbk'))  # 输入的字符串类型需要提供encoding的实参,来指定编码方式
# print(bytes(name, encoding='big5'))  # 输入的字符串类型需要提供encoding的实参,来指定编码方式
# print(bytes(b'ecer'))  二进制模式的字节流


"""
dir():输出数据类型/对象/函数 拥有的方法,列表形式输出
"""

# print(dir(int))  #  打印输出这些数据类型或者内置函数中有哪些方法
# print(dir(dict))  #
# print(dir(list))  #
# print(dir(str))  #
# print(dir(all('111')))  #

"""
divmod(参数1,参数2):两个参数,参数1%参数2,即参数1对参数2进行除法,输出(商,余数)
常用于页码的分隔显示
divmod(参数1,参数2):
参数1:总共的信息条数
参数2:一页展示的信息条数
参数1对参数2进行求余运算,得出(商,余数)

"""

# print(divmod(10, 4))  # (2, 2)
# print(divmod(10, 14))  # (0, 10)
# print(divmod(101, 4))  # (25, 1)

"""
eval():
1.把字符串中的数据结构提取出来.
	将字符串中的数据类型转回到原来的数据类型.比如'{}','[]'这种字符串中套有
一个字典或者列表的数据类型,经过eval()后可以变回原来的字典,列表类型.

2.把字符串中的表达式进行运算.
将一个表达式中的数学运算提取出来进行运算

"""

# dict1 = {'1': 1, '2': 2}
# dict1_str = str(dict1)
# print(dict1_str)  # {'1': 1, '2': 2}
# print(type(dict1_str))  # <class 'str'>
# print(eval(dict1_str))
# print(type(eval(dict1_str)))  # <class 'dict'>
#
# expresions = '1111111+2/3*4-(4**8)'
# print(eval(expresions))  # 1045577.6666666667


"""
hash(): 主要用于校验文件,防止文件在传输过程中遭到破坏.等等

可hash的数据类型是不可变数据类型,不可hash的数据类型是可变数据类型.

元组,字符串,整型,浮点型.都是不可变数据类型,可哈希的.

可变不可变:就是看定义之后这个数据类型的内部元素能不能被修改

实际上的代码就是一堆字符串,进入计算机系统后进行编码,转换成二进制文件进行执行

实际上只要是容器类型的数据类型,比如列表,字典,集合等等,都是不可哈希的
"""
# print(hash('1111111111111111111111'))  # 字符串类型,不可变数据类型,可哈希
# print(hash(11111111111111111))  # 整型 不可变数据,可哈希
# print(hash((1, 2, 3, 4)))  # 元组,不可变数据类型,可哈希

# print(hash([1, 2, 3, 34, 4]))  # 列表,可变数据,不可哈希
# print(hash({1: '1', 2: '2'}))  # 字典,可变数据,不可哈希
# print(hash({1,2,3,4,5})) # 集合,可变数据,不可哈希


# str1 = '11111'
# for i in str1:
# 	print(i)
# str1[1] = 1  # TypeError: 'str' object does not support item assignment,译为:字符串类型的对象不支持内部元素的重新赋值,重新定义
# print(str1)


# tuple1 = (1,2,3,4)
# tuple1[1] = 'op'  # TypeError: 'tuple' object does not support item assignment
# print(tuple1)


"""
help():查看帮助

"""

"""
print(help(abs))

输出:
abs(x, /)
    Return the absolute value of the argument.

None
"""

"""
bin():转换数字为二进制
hex():转换数字为16进制
oct():转换数字为8进制
"""
# print(bin(12))  # 0b1100
# print(hex(12))  # 0xc
# print(oct(12))  # 0o14


"""
isinstance(A,B):判断A是不是B的一个实例对象


"""

# print(isinstance(1, int))
# print(isinstance('12222', str))
# print(isinstance(1.000, float))
# print(isinstance([], list))
# print(isinstance({1,2}, set))
# print(isinstance((1, 2), tuple))
# print(isinstance({1: '1', 2: '2'}, dict))


"""
globals():全局变量

loacals():局部变量
"""
# name = '哈哈哈哈或'

# print(globals())
# print(__file__)  # F:/Python就业班/oldboy/内置函数build in.py
# print(locals())
# def test():
# 	age = 9
# 	print(globals())  # 只输出全局变量{'哈哈哈哈或'}
# 	print(locals())  # 输出局部变量  {'age': 9}
#
#
# test()


"""
max():取最大值
min():取最小值

高级用法:结合zip()使用,进行比较指定参数的大小

1.> max函数处理的是可迭代对象,相当于一个for循环取出每个元素进行比较,注意:不同数据类型之间不能进行比较


2.> 每个元素之间进行比较,是从每个元素的第一个位置依次比较,如果这一个位置分出大小,后面的都不需要进行比较了,
  直接得出这两个元素的大小.


"""

# print(max([1, 2, 3, 8, 9, 34]))
# print(min([1, 2, 3, 8, 9, 34]))



# age_dict = {'age111111111111': 18, 'age1': 20, 'age2': 58, 'age3': 70}
# age_dict = {'alex_age': 18, 'wupeiqi_age': 20, 'yuanhao_age': 58, 'haifeng_age': 70}

# print(max(age_dict.values()))
# # 默认比较字典的key
# print(max(age_dict))  # 按照key进行比较,根据ascii码表进行字符大小比较

# 字符串比较是一个一个字符去比较


# for item in  zip(age_dict.values(), age_dict.keys()):  # (18,'alex_age)
# 	print(item)

# print(max(zip(age_dict.values(), age_dict.keys())))  # (70, 'haifeng_age')
# print(list(max(zip(age_dict.values(), age_dict.keys()))))  # [70, 'haifeng_age']

# TypeError: 'dict_values' object is not callable
# print(max(age_dict, key=age_dict.values()))


# list1 = [
#
# 	(5,'g'),
# 	(7,'r'),
# 	(8,'e'),
# 	(9,'t'),
# 	(4,'j'),
# ]
# print(max(list1))  # (9, 't')

# l1 = ['a10','b12','c10']
# l11 = ['a10','a2','a10']
#
# print(max(l1))  # c10
# print(max(l11))  # a2  从每个字符串中的第一个元素a开始比较大小,到第二位就比较出大小了.所以是a2

# print(list(max(l1)))  # ['c', '1', '0']

# l2 = ['a10','b12','c10',12]  # 不同类型无法比较

# TypeError: '>' not supported between instances of 'int' and 'str'
# 意思是字符串和数字不能比较大小
# print(max(l2))

# 终极玩法:


# people = [
# 	{'name':'alex','age':123},
# 	{'name':'wupeiqi','age':25},
# 	{'name':'yuanhao','age':23},
# 	{'name':'linhaifeng','age':12}
#
# ]

# 意思就是for x in people,然后进行 x['age'],然后返回 x

# {'name': 'alex', 'age': 123}
# print(max(people,key=lambda x:x['age']))  # 字典类型无法比较大小

# 以上lambda函数实际实现的过程是:
# ret = []
# for item in people:  # 提取字典中的values放到一个新的列表中
# 	ret.append(item['age'])
# print(ret)
# print(max(ret))

"""
zip():拉链,左边对应右边

如果不是一一对应,反正就是左边能对应右边,能对应上的就行.对不上的不管

序列包括:元组,列表,字符串
"""

# print(zip([1, 2, 3, 3], ('1', '2', '3', '4')))  # <zip object at 0x000001B95111AF48> zip 生成一个对象
# print(list(zip([1, 2, 3, 3], ('1', '2', '3', '4'))))  # list转换成列表类型
# print(list(zip([1, 2, 3], ('1', '2', '3', '4'))))  # list转换成列表类型
# print(list(zip([1, 2, 3, 3], ('1', '2', '3'))))  # list转换成列表类型

# p = {'name': 'alex', 'age': 18, 'gender': 'male'}
# print(list(zip(p.keys(), p.values())))
# # [('name', 'alex'), ('age', 18), ('gender', 'none')]
# print(list(p.keys()))
# print(list(p.values()))

"""
chr(数字):输出数字对应的ascii码表中对应的字符

ord(字符):输出字符在ascii码表中对应的数字


"""

# print(chr(89))  # Y
# print(ord('Y'))  # 89


"""
pow(a,b): 输出a**b:就是a的几次方运算 
pow(a,b,c): 输出 a**b%c,就是a的b次幂然后对c进行求模(取余数)运算


"""

# print(pow(2,4))  # 16
# print(pow(2, 2, 3))  # 1
# print(pow(3, 2, 3))  # 0
# print(pow(4, 2, 3))  # 1


"""
reversed():反转

"""

# l = [1,2,3,4]
#
# # <list_reverseiterator object at 0x000001EF3A90E2B0>
# # 生成一个迭代器,是一个可迭代对象,可以使用for循环进行遍历
# print(reversed(l))
# print(list(reversed(l)))  # [4, 3, 2, 1]
# print(l)  # [1, 2, 3, 4]

"""
round(小数):四舍五入

"""
# print(round(9.74))


"""
set():集合
"""
# {'e', 'l', 'o', 'h'}
# print(set('hello'))


"""
slice():切片

"""
# l = 'hello'
# 记住:顾头不顾尾,硬编码,写死了
# print(l[3:5])

# s1 = slice(3,5)
# s2 = slice(1,4,2)  # 定义步长为 2
# print(l[s1])  # lo
# print(l[s2])  # el
# print(s2.start)
# print(s2.stop)
# print(s2.step)


"""
sorted():排序,本质就是在比较大小.只能同类型比较大小.不同类型无法比较
默认是从小到大进行排序输出.
输出的格式是一个列表类型

"""

# l = [3,2,5,7,8]
#
# # TypeError: '<' not supported between instances of 'str' and 'int'
# # l1  = [3,2,5,'e',7,8] 报错
# print(sorted(l))  # [2, 3, 5, 7, 8]


# people = [
# 	{'name':'alex','age':123},
# 	{'name':'wupeiqi','age':25},
# 	{'name':'yuanhao','age':23},
# 	{'name':'linhaifeng','age':12}
#
# ]

# print(sorted(people, key=lambda x: x['age']))
# [{'name': 'linhaifeng', 'age': 12}, {'name': 'yuanhao', 'age': 23}, {'name': 'wupeiqi', 'age': 25}, {'name': 'alex', 'age': 123}]


# name_dic = {
# 	'abuanhao':700,
# 	'alex':200,
# 	'wupeiqi':2100,
#
# }

# 按照key进行比较  ['abuanhao', 'alex', 'wupeiqi']
# print(sorted(name_dic))
# # 按照value进行比较  ['alex', 'abuanhao', 'wupeiqi']
# print(sorted(name_dic,key=lambda key:name_dic[key]))
#
#
# # 既要key,又要value  [(200, 'alex'), (700, 'abuanhao'), (2100, 'wupeiqi')]
# print(sorted(zip(name_dic.values(), name_dic.keys())))

"""
str():任意类型转化为字符串

"""

"""
sum():求和
"""

# l = [1,2,4]
# print(sum(l))  # 7
# print(sum(range(7)))  # 21


# 写程序就是在处理状态的变化


"""
type():判断数据类型

"""
# msg = '123'
#
# if type(msg) is str:
# 	msg = int(msg)
# 	res = msg + 1
# print(res)

"""
vars():如果没有参数,就是和locals()一样输出局部变量

如果有一个参数,就是输出一个对象的所有方法,并且以字典的形式输出.

"""

# def test():
# 	mas = 'dfvdfvfdvfd'
# 	print(locals())  # {'mas': 'dfvdfvfdvfd'}
#
# 	#如果没有参数,就是和locals()一样输出局部变量
# 	print(vars())  # {'mas': 'dfvdfvfdvfd'}
#
#
# test()

# 如果有一个参数,就是输出一个对象的所有方法,并且以字典的形式输出.
# print(vars(int))


"""
import 不能导入字符串类型文件

__import__(): 以字符串方式导入模块名


实际上是:import --> sys ---->__import__()

写程序就是写一堆字符串,操作系统最后都是去调用字符串了

"""

# import test  # 导入test模块
# test.say_hi()  # 模块名.函数名调用

# module_name = 'test'
# m = __import__(module_name)  # 导入字符串类型的文件名
# m.say_hi()  # 你好,世界!



# l = [1,2,3,4]
# print(list(map(lambda x: str(x), l)))
# print(list(map(str, l)))

# from functools import reduce
#
# l = [1,2,3,4,5]
# print(reduce(lambda x, y: x + y, l))

name = ['alex_sb', 'linhaifeng']

print(list(filter(lambda x: not x.endswith('sb'), name)))
