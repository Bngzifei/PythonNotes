# coding:utf-8
# age = int(input('今年多大了?'))
#
# if age >= 18:
# 	print('可以进网吧嗨')
# else:
# 	print('你还没长大回家写作业')


# num = int(input('请输入数字:'))
#
# if num:
# 	print('数字非零')
# else:
# 	print('数字是零')
#
# age = int(input('输入年龄值:'))
#
# if age >= 0 and age <= 120:
# 	print('年龄正确')
# else:
# 	print('年龄不正确')

# python_score = int(input('输入python成绩:'))
# c_score = int(input('输入c成绩:'))
#
#
# if python_score > 60 or c_score > 60:
# 	print('成绩合格')
# else:
# 	print('继续努力')

# # 设定初始值为真,默认都是本公司员工
# is_employee = True
#
#
# # 如果不是,则初值为假
# if not is_employee:
# 	print('非本司员工,勿入')


# holiday_name = input('输入节日:')
#
# if holiday_name == '情人节':
# 	print('看电影')
# 	print('买玫瑰')
# elif holiday_name == '平安夜':
# 	print('买苹果')
# 	print('吃大餐')
# elif holiday_name == '生日':
# 	print('买蛋糕')
# else:
# 	print('每天都是节日,没钱过了.....')


# has_ticket = True
# knife_llength = 2
#
# # 首先检查是否有票,如果有,才允许进行安检
# if has_ticket:
# 	print('有票,可以开始安检...')
# 	# 安检时,需要检查刀的长度,判断其是否超过20厘米,超过20的不允许上车
# 	if knife_llength >= 20:
# 		print('想坐牢啊,不能携带%d厘米长的刀上车' % knife_llength)
# 	# 没超过20的,安检通过
# 	else:
# 		print('安检通过,旅途愉快!')
#
# # 如果没有车票,不允许进门
# else:
# 	print('大哥,先花钱买票啊')


# import random
# player = int(input('请出拳 石头(1)/剪刀(2)/布(3):'))
#
# # 电脑初值设为石头(1),等下再加随机数处理
# computer = 1
# computer = computer + random.randint(0,2)
# print(computer)
# if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
# 	print('渣渣电脑,老子赢了!!!')
# elif player == computer:
# 	print('不行,再来一局')
# else:
# 	print('厉害炸了,我输了...')

# i = 1
#
# while i <= 100000:
# 	print('媳妇儿,错了')
# 	i+=1

# 求和
# i = 1
# sum = 0
# while i<101:
# 	sum= sum + i
# 	i += 1
#
# print('0~100之间的累积和为:%d'%sum)

# 求偶数之和
# i = 1
# sum = 0
# while i<101:
# 	if i%2 ==0:
# 		sum= sum + i
# 	i += 1
#
# print('0~100之间的累积和为:%d'%sum)

# i = 0
# #满足i==3的时候,彻底跳出循环
# while i < 10:
# 	if i == 3:
# 		break
# 	print(i)
# 	i += 1
#
# print('over')


# 就是剔除某个满足条件的元素,实现while的循环筛选
# i = 0
# while i<10:
# 	if i == 7:
# 		i += 1
# 		continue
# 	print(i)
#
# 	i += 1


# 九九乘法表
#
# row = 1
# while row <= 5:
# 	# 打印和行数相等的*
# 	print('*' * row)
# 	row += 1

#
# row = 1
# while row <= 9:
# 	col = 1
# 	while col <= row:
# 		print('*',end='')
# 		col += 1
# 	print('')
# 	row += 1



# row = 1
# while row <= 9:
# 	col = 1
# 	while col <= row:
# 		print('%d * %d = %d' % (col,row,row * col),end='\t')
# 		col += 1
# 	print('')
# 	row += 1

# name_list = ['张珊','历史','王五']
# print(name_list[2])

# import keyword
# print(keyword.kwlist)

# i是索引,索引从0开始,到len()-1为止
# i = 0
# name_list = ['111','222','333']
# list_count = len(name_list)
# while i < list_count:
# 	name = name_list[i]
# 	print(name)
# 	i += 1

# for 循环
# name_list = ['111','222','333']
# for name in name_list:
# 	print(name)

# schoolName = [
# 	['清华大学','北京大学','南开大学'],
# 	['复旦大学','上海交通大学','同济大学'],
# 	['南京大学','东南大学','南京航空航天大学'],
# 	['武汉大学','华中科技大学','中国地质大学'],
# ]
#
# for i in schoolName:
# 	print(i)

# schoolName = [
# 	['清华大学','北京大学','南开大学'],
# 	['复旦大学','上海交通大学','同济大学'],
# 	['南京大学','东南大学','南京航空航天大学'],
# 	['武汉大学','华中科技大学','中国地质大学'],
# ]
#
# i = 0
# for  i in len(schoolName):
# 	print(schoolName[i])
# 	i += 1
# TypeError: 'int' object is not iterable   for语句替换成while循环就行


# schoolName = [
# 	['清华大学','北京大学','南开大学'],
# 	['复旦大学','上海交通大学','同济大学'],
# 	['南京大学','东南大学','南京航空航天大学'],
# 	['武汉大学','华中科技大学','中国地质大学'],
# ]
#
# i = 0
# while i < len(schoolName):
# 	print(schoolName[i])
# 	i += 1

#
# 组合:将8个人随机分配到3个办公室即可
# import random
#
# offices = [
# 	[], [], []
# ]
#
# names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#
# # 办公室索引0,1,2随机生成
#
# for name in names:
# 	index = random.randint(0, 2)
# 	# 将8个人中的某一个随机添加到某个办公室
# 	offices[index].append(name)
# # 到这里就分配完成
# # 获取办公室信息	,i是办公室的编号
# i = 1
# for tempNames in offices:
# 	print('办公室%d的人数为:%d' % (i, len(tempNames)))
# 	i += 1
# 	for name in tempNames:
# 		print('%s' % name, end='')
# 	print('\n')
# 	print('-' * 20)

# info_tuple = ('张珊',18,1.75)
# print(info_tuple[2])
#
# info_tuple = (50)
# print(info_tuple[0])
#
# TypeError: 'int' object is not subscriptable,据此可见(50)是一个整型,(50,)是一个元组
#
#
# info_tuple = (50,)
# print(info_tuple[0])


# info_tuple = ('zzz',18,1.75)
# info_tuple[0] = 'list'
# TypeError: 'tuple' object does not support item assignment
# Tuple（元组）与列表类似，不同之处在于元组的 元素不能修改
#
# info = 10,20
# print(type(info))
# 出现警告:no newline at end of file
# 在程序最后再加一行即可,enter键
# portal:入口,出孔

# info = 10,20
# print(type(info))
#
#
# a = 10
# b = 20
# a,b = b,a

# 格式字符串，格式化字符串后面的 () 本质上就是一个元组
# info = ('zhangsan', 18)
# print('%s的年龄是%d' % info)

# #元组和列表之间的转换
# list1 = [10,11]
# tuple1 = tuple(list1)
# list2 = list(tuple1)
#
# print(type(list1))
# print(type(tuple1))
# print(type(list2))

# 字典dict
# xiaomi = {
# 	'name':'小米',
# 	'age':18,
# 	'gender':'男',
# 	'height':1.75
# }
#
# #取出对应key的value值
# print(xiaomi['name'])
# print(xiaomi['age'])
# print(xiaomi['gender'])
# print(xiaomi['height'])

# card_list = [
# 	{
# 		'name':'张珊',
# 		'qq':'1234',
# 		'phone':'110'
#
# 	},
#
# 	{
# 		'name':'历史',
# 		'qq':'3453',
# 		'phone':'119'
# 	}
# ]
# print(card_list)
# print(card_list[0])
# print(card_list[1])

# 字符串  指定区间是左闭右开,取左不取右
# num_str = '0123456789'
# print(num_str[2:5])
# print(num_str[-2:])
# print(num_str[:])
# # 隔1个取
# print(num_str[::2])
# # 从1开始隔一个取一个
# print(num_str[1::2])
# # 2到-1
# print(num_str[2:-1])
# # 字符串逆序,两个::就是倒序的表示方式
# print(num_str[::-1])
# print(num_str[::-8])#这是啥,怎么理解???

# # print([1,2]+[3,4]) list拼接
# #输出list中元素*4
# print(['Hi!']*4)
# ['Hi!', 'Hi!', 'Hi!', 'Hi!']

#
# students = [
# 	{
# 		'name':'阿土',
# 		'age':20,
# 		'gender':True,
# 		'height':1.7,
# 		'weight':75.0
# 	},
#
# 	{
# 		'name':'小美',
# 		'age':19,
# 		'gender':False,
# 		'height':1.6,
# 		'weight':45.0
#
# 	}
# ]
#
#
# find_name = '阿土'
# for stu_dict in students:
# 	print(stu_dict)
#
# 	if stu_dict['name'] == find_name:
# 		print('找到了')
# 		#如果已经找到,直接退出循环,就不需要再对后续的数据进行比较
# 		break
# 	else:
# 		print('没有找到')
# print('循环结束')

# num1 = int(input('输入周一~周日(使用数字1-7分别代表):'))
#
# if num1 == 6 or num1 == 7:
# 	print('周末')
# else:
# 	print('不是周末')

# num1 = int(input('输入周一~周日(使用数字1-7分别代表):'))
#
# if num1 == 6 or num1 == 7:
# 	print('周末')
# elif num1 == 1:
# 	print('工作日')
# elif num1 == 2:
# 	print('工作日')
# elif num1 == 3:
# 	print('工作日')
# elif num1 == 4:
# 	print('工作日')
# elif num1 == 5:
# 	print('工作日')
# else:
# 	print('错误')

# heigh = float(input('身高(cm):'))/100
# weight = float(input('体重(kg):'))
#
# BMI = weight/(heigh**2)
#
# print('BMI=%.1f' % BMI)
#
# if BMI < 18.5:
# 	print('过轻')
# elif 18.5 <= BMI < 25:
# 	print('正常')
# elif 25 <= BMI < 28:
# 	print('正常')
# elif 28 <= BMI <= 32:
# 	print('正常')
# elif BMI > 32:
# 	print('正常')
# else:
# 	print('错误')

# num1 = float(input('请输入第一个数:'))
#
# a = input('输入运算符(+ - * /):')
#
# num2 = float(input('请输入第二个数:'))
# if a == '+':
# 	print('他们的和为:%.2f' % (num1 + num2))
# elif a == '-':
# 	print('他们的差为:%.2f' % (num1 - num2))
# elif a == '*':
# 	print('他们的积为:%.2f' % (num1 * num2))
# elif a == '/':
# 	print('他们的商为:%.2f' % (num1 / num2))
"""
循环遍历:
遍历:就是从头到尾依次从列表中取出每一个元素
Python中为了提高列表的遍历效率,专门提供了for循环实现遍历
Python中的for循环本质是迭代器.(可以进行逐次推导的意思)
"""

"""while循环遍历列表list"""
# # while循环实现列表的遍历
# i = 0
# name_list = ['zhangsan', 'lisi', 'wangwu']
# while i <= len(name_list) - 1:
# 	name = name_list[i]
# 	print(name)
# 	i += 1

"""for循环遍历list"""
# name_list = ['zhangsan', 'lisi', 'wangwu']
# for name in name_list:
# 	print(name)

"""字典dict"""

"""
dictionary(字典)
用来存储多个数据,通常用于存储描述一个物体的相关信息

字典用{} 定义
字典使用键值对存储数据键值对之间使用,号分隔
key-value模型

键 key 是索引
值 value 是数据
键 和 值 之间使用 : 分隔
值 可以取任何数据类型，但 键 只能使用 字符串、数字或 元组
键必须是唯一的

字典没有索引,是无序的,存储的数据类型也不一样.为了方便描述,人为的给他加入一个索引的概念

"""

"""字典常用操作"""

# 定义字典
# xiaoming = {
# 	'name': '小明',
# 	'age': 18,
# 	'gender':True,
# 	'height':1.75
# }
# # 取出key键对应的值
# # print(xiaoming['name'])  # 输出小明
#
# """增加"""
# # 直接添加索引位置添加key,然后对其进行赋值
# xiaoming['school_nums'] = '20130610110110'
# print(xiaoming['school_nums'])
#
# """删除指定的键值对"""
# # del xiaoming['age']
# #
# # print(xiaoming['age'])  # 对应KeyError: 'age' 删除age 键和其对应的value值之后,会出现这样的报错.提示信息是key键值错误
#
#
# # pop()  # 删除指定键值对,返回被删除的value值
# # age = xiaoming.pop('age')
# # print(age)
#
# # 字典.clear  # 清空字典
# # print(xiaoming.clear())  #执行clear() 操作之后就是将所有数据删除,返回 None
#
# """修改"""
# # 意思就是对其中的key 键进行重新赋值
# xiaoming['age'] = 19
# print(xiaoming['age'])  # 输出19,将原来的age=18改为19,重新赋值即可
# """查询"""
# print(xiaoming['age'])  # 查询某个指定key的值
#
# # 字典.items()  # 实现遍历字典的功能,获取所有的key - value
# # print(xiaoming.items())
#
# for key in xiaoming:  # 取出字典中的每个value的key
# 	print(key)

# 输出为:
# name
# age
# gender
# height
# school_nums

"""字符串"""

# 就是一串字符,是编程语言中用来表示文本的数据类型
# 可以使用索引获取一个字符串中指定位置的字符,索引计数从0 开始,意思就是字符串默认自带索引
# 可以使用for循环遍历字符串中每一个字符

# 因为大多数编程语言都是使用""来定义字符串,所以我们在今后的编程过程中也遵循这个传统
#
# str = "Hello Python"
# i = 0
# while i< len(str):
# 	print(str[i])
# 	i += 1  # 千万不要忘记了这边的计数+1,每次这里都会遗漏
#

# 不要忘记for循环就是为了支持list列表这种结构的数据,这里就是将字符串作为一个list列表进行处理
# str = "Hello Python"  # 字符串中的 空格也会进行取值输出
# for i in str:
# 	print(i)

"""字符串切片slice"""
# 切片 -> slice ,翻译成另外一个解释更好理解:一部分
# 切片 使用索引值 来限定范围,根据步长 从原序列中取出一部分元素组成新序列
# 切片 方法适用于 字符串.列表.元组. 这些数据类型的步长是固定值 记住: 没有字典
# 字符串就是一个list列表
# 步长就是等差数列中的公差d
# 字符串[开始索引:结束索引:步长]
"""
注意：

1.指定的区间属于 左闭右开 型 [开始索引, 结束索引) 对应 开始索引 <= 范围 < 结束索引
	从 起始位开始，到 结束位的前一位 结束（不包含结束位本身)
2.从头开始，开始索引 数字可以省略，冒号不能省略
3.到末尾结束，结束索引 数字和冒号都可以省略
4.步长默认为 1，如果元素连续，数字和冒号都可以省略

取不到最后一个
"""
"""索引的顺序和倒序"""
# 在 Python 中不仅支持 顺序索引，同时还支持 倒序索引
# 所谓倒序索引就是 从右向左 计算索引
# 最右边的索引值是 -1，依次递减
# 注意：如果 步长为负数,
# 并省略了开始索引，则开始索引表示最后一位
# 并省略了结束索引，则结束索引表示第一位

# str = "Hello Python"
# print(len(str))
# # print(str[12])  # IndexError: string index out of range 原因就是:最后一个字符的索引值=len(str) - 1 所以会出现字符串索引值越界的报错
# print(str[len(str) - 1])
"""演练需求"""
# 截取从 2 ~ 5 位置 的字符串
# 截取从 2 ~ 末尾 的字符串
# 截取从 开始 ~ 5 位置 的字符串
# 截取完整的字符串
# 从开始位置，每隔一个字符截取字符串
# 从索引 1 开始，每隔一个取一个
# 截取从 2 ~ 末尾 - 1 的字符串
# 截取字符串末尾两个字符
# 字符串的逆序（面试题）

# str = "HelloPython"
# print(str[2:6])
#
# print(str[2:])
#
# print(str[:6])
#
# print(str[:])
#
# print(str[::2])  # 原来的步长是1 ,现在需要跳一个,所以设置步长+1 = 2
#
# # 倒序切片
# # -1 表示倒数第一个字符
# print(str[-1])
#
# print(str[2:])
#
# print(str[-2:])
#
# print(str[::-1])  # 逆序排列 输出 nohtyPolleH,只有-1的时候是这样,如果-2 则会按照步长为2的情况进行逆序输出
#
# print(str[::-2])
#
# print(str[::--1])  # 正序排列 输出 HelloPython

"""
输出为:
lloP
lloPython
HelloP
HelloPython
Hloyhn
n
lloPython
on
nohtyPolleH
nhyolH
HelloPython

"""

"""公共语法"""
# 1.Python内置函数:
# 2.切片:
# 切片 使用 索引值 来限定范围，从一个大的 字符串 中 切出 小的 字符串
# 列表 和 元组 都是 有序 的集合，都能够 通过索引值 获取到对应的数据
# 字典 是一个 无序 的集合，是使用 键值对 保存数据
# 3.运算符:
# in 在对 字典 操作时，判断的是 字典的键
# in 和 not in 被称为 成员运算符
# 注意：在对 字典 操作时，判断的是 字典的键
# 4. for ... else...
#
# for 变量 in 集合:
#
# 	循环体代码
# else:
# 	没有通过
# 	break
# 	退出循环，循环结束后，会执行的代码

"""for...else:应用场景"""
# 在迭代遍历 嵌套的数据类型时，例如: 一个列表包含了多个字典
# 需求：要判断 某一个字典中 是否存在 指定的 值(value)
# 如果 存在，提示并且退出循环
# 如果 不存在，在 循环整体结束 后，希望 得到一个统一的提示

# students = [
# 	{"name": "阿土",
# 	 "age": 18,
# 	 "gender": True,
# 	 "height": 1.7,
# 	 "weight": 75.0
# 	 },
#
# 	{"name": "小美",
# 	 "age": 28,
# 	 "gender": False,
# 	 "height": 1.65,
# 	 "weight": 45.0
# 	 }
# ]
#
# find_name = "阿土1"  # 是value
#
# for stu_dict in students:
# 	# print(stu_dict)  # 输出列表元素->两个字典类型
#
# 	# 判断当前遍历的字典中姓名为find_name
# 	if stu_dict['name'] == find_name:  # key - value 键值对
# 		print('找到了')
# 		break  # 找到了的情况下直接终止循环.不再对后续数据进行比较
#
# else:  # 否则直接输出没有找到.记住这里是和for一起的else,而不是和if.
# 	print('没有找到')
#
# print('循环结束')

"""函数"""
# 所谓函数,就是把具有独立功能的代码块组织为一个整体,在需要的时候调用
#
# 函数的使用步骤:
# 1.定义函数--在函数中编写代码,实现功能
# 2.调用函数--执行编写的代码
#
# 函数的作用:
# 在开发程序时,使用函数可以提高编写的效率以及代码的重用

"""函数的定义"""

# def 函数名():
# 	函数封装的代码
# 	...
#
# 1.def 是英文define的缩写
# 2.函数名称应该能够简单明确的表达函数功能,见名知义
# 3.函数名称的命名:
# 	由数字.字母.下划线组成
# 	不能以数字开头
# 	不能与关键字重名

"""函数的调用"""
# 函数名()  即可完成

"""函数演练"""

"""
需求:

编写一个打招呼 say_hello 的函数，封装三行打招呼的代码
在函数下方调用打招呼的代码

"""
# name = '小南国'
#
# # 解释器知道这里定义了一个函数,会跳过这个函数的定义,直到调用的时候才回来执行它
# def say_hello():
# 	print('hello 1')
# 	print('hello 2')
# 	print('hello 3')
#
# print(name)
# # 只有在调用函数时,之前定义的函数才会被执行
# # 函数执行完成后,会重新回到之前的程序执行过程中,即按照之前的执行顺序继续进行后续的代码
# say_hello()
#
# print(name)

"""函数执行过程"""
# 2.1 PyCharm的单步调试
#
# F8 Step Over 可以单步执行代码，会把函数调用看作是一行代码直接执行
# F7 Step Into 可以单步执行代码，如果是函数，会进入函数内部
# 用 单步执行 F8 和 F7 观察以下代码的执行过程
#
# 定义好函数之后，只表示这个函数封装了一段代码而已
# 如果不主动调用函数，函数是不会主动执行的

# 能否将 函数调用 放在 函数定义 的上方？
#
# 不能！
# 因为在 使用函数名 调用函数之前，必须要保证 Python 已经知道函数的存在
# 否则控制台会提示 NameError: name 'say_hello' is not defined (名称错误：say_hello 这个名字没有被定义)

"""函数的文档注释"""
# 在开发中,如果希望给函数添加注释,应该在定义函数的下方,使用连续的三对引号
# 在连续的三对引号之间编写对函数的说明文字
# 在函数调用的位置,使用快捷键Ctrl + Q 可以查看函数的说明信息
# inter: 推断.推理

# def func_sum():
# 	"""求和 1 + 2"""
# 	sum_num = 1 + 2
# 	print(sum_num)
#
# func_sum()

# 注意:因为函数体相对比较独立,函数定义的上方,应该和其他代码(包括注释)保留两个空行

# 快捷键 Ctrl + / 注释代码时候,不需要使用鼠标了,只要光标所在行即可实现对其进行注释

"""函数的参数"""

# 演练需求
#
# 开发一个 sum_2_num 的函数
# 函数能够实现 两个数字的求和功能

# def sum_2_num():
# 	"""两个整数求和"""
# 	num1 = int(input('输入第一个数字(整数):'))
# 	num2 = int(input('输入第二个数字(整数):'))
# 	sum1 = num1 + num2  # 这里不能使用sum,sum是关键字
# 	# 这里记得使用格式化字符%进行输出显示
# 	print("%d + %d = %d" % (num1,num2,sum1))
#
# sum_2_num()

"""参数的概念"""
# 函数的参数:可以传递给函数内部,增加函数的通用性
# 	1.在函数内部,把参数当作变量使用,进行需要的数据处理
# 	2.函数调用时,按照函数定义的参数顺序,把希望在函数内部处理的数据,通过参数传递

"""设置函数的参数"""

# 1.在函数名的后面的小阔号()内部填写参数
# 2.多个参数直接使用,分隔

# def sum_2_num(num1, num2):
# 	sum1 = num1 + num2
# 	print("%d + %d = %d" % (num1, num2, sum1))
#
# # 标准化代码格式记得使用快捷键 Shift + Alt + F (F是Format:使格式化的意思)
# # 既然定义的时候有参数,那么在调用函数的时候一定有参数,不要理解错了
# sum_2_num(1, 2)

"""形参和实参"""
# 1.形参:定义函数时设置的参数,是用来代替真实数据的,在函数内部作为变量使用
# 2.实参:调用函数时设置的真实数据,会被传到函数内部,即实参会赋值给形参,也就是:形参 = 实参
"""形参的作用域"""

# a = 5
#
# def test1(a):  # 这里的a是一个形参,就是一个变量.不是上面的a
# 	a += 1
# 	print("%d" % a)
# test1(2)  # 3 这里的2是实参,将会赋值给形参a 即a = 2 进行下面的运算
# print("%d" % a)  # 5 这里的a是上面的那个变量,不是形参.

# 1. 形参的作用域(就是起作用的范围):只在定义函数的代码中,一旦超出该范围再使用该形参名,则使用的是同名的自定义变量
# 2. 编程中应该尽量避免函数的形参和同一个文件的变量名同名

"""函数的返回值"""
# 4.1概念
# 	1.开发中,有时候会希望一个函数执行结束后,告诉调用者一个结果,以便调用者对具体的结果做后续的处理
#	2. 返回值是函数给调用方提供的结果
# 4.2 设置返回值
# 1.在函数中使用return关键字可以返回结果
# 2.调用函数一方,可以使用变量来接收函数的返回结果
# def sum_2_num(num1,num2):
# 	"""对两个数字进行求和运算"""
# 	return num1 + num2
#
# sum1 = sum_2_num(4,8)  # 变量sum1来接收函数的返回值
# print("结果是:%d" % sum1)

"""4种函数的类型"""

# 函数根据有没有参数,有没有返回值,可以相互组合,一共有4种

"""函数的高级"""
"""
局部变量:就是在函数内部定义的变量def ()里面的那些变量->形参
不同的函数,可以定义相同名字的局部变量.但是各自使用各自的,相互之间不会产生影响
局部变量的作用域只在函数内部
局部变量的目的:是存储需要临时保存的数据(实参->形参的过程).桥梁作用.传递



全局变量:
在函数外部定义的变量叫做全局变量
全局变量能够在所有的函数中进行访问

函数内修改全局变量:
函数内赋值变量时,默认为定义并赋值局部变量
赋值后获取的也是局部变量的值
如果在函数内部修改全局变量,那么就需要使用global进行声明,否则出错




"""

# 局部变量:
# def test1():
# 	a = 20
# 	print('%d' % a)
#
#
# def test2():
# 	a = 30
# 	print('%d' % a)
#
#
# test1()
# test2()

# 全局变量:
# a = 100
#
#
# def test1():
# 	print(a)
#
#
# def test2():
# 	print(a)
#
#
# test1()
# test2()

# a = 10
# def test():
# 	a = 5
# 	print('函数内a:%d' % a)
# test()
# print('函数外a:%d' % a)
# 输出:
# 函数内a:5
# 函数外a:10

# global 修改全局变量
# a = 10
#
#
# def test():
# 	global a  # 声明a是全局变量,意思就是函数外部的a和函数内部的a一样了,有关系了.不声明就没关联
# 	a = 5  # 修改全局变量
# 	print('函数内a:%d' % a)
#
#
# test()
# print('函数外a:%d' % a)

"""函数返回值"""

"""
多个return:
一个函数中可以有多个return语句,但是只要有一个return 语句被执行,那么这个函数就会结束

多个返回值:

当返回多个数据时,自动组包成元组
使用多个变量接收返回值(有多个返回值时),python会自动将元组拆包成单个数据


"""

# 多个return
# def is_even_num(num):
# 	"""判断奇偶数"""
# 	if num % 2 == 0:
# 		return True
# 	else:
# 		return False

# 多个返回值
# def func2():
# 	return 1, 1.5
#
#
# a = func2()  # 返回值多个,接收变量一个,就组成了元组
# print(a)  # 元组
#
#
# a, b = func2()  # 元组自动解包(变量个数和元组的元素个数相等)
# print(a)
# print(b)
#
#
# a = 1,1.5,'hello'  # 自动组包(多个数据赋值给一个变量,自动组包成元组类型)
# print(a)
# print(b)

"""可变参数:kwargs

kwargs:可以接收不存在的关键字参数
定义时需要在变量名前面添加2个*
这种 可变参数 会将 不存在的关键字参数包装成字典

"""

# def sum_num(a, b, *args, **kwargs):
# 	print(a)
# 	print(b)
# 	print(args)
# 	print(kwargs)
#
# # (3, Ellipsis)  # Ellipsis:是省略的意思,代表了...
# sum_num(1, 2, 3, ..., mm=5, nn=6)  # 输出的kwargs是{'mm': 5, 'nn': 6},是把一个对应关系进行输出
# # args 是将关键字参数后面的所有参数全部接收

"""传递可变参数:


"""

# def sum_num(a, b, *args, **kwargs):
# 	print(a)
# 	print(b)
# 	print(args)
# 	print(kwargs)
# 	test(*args, **kwargs)
#
#
# def test(*args, **kwargs):
# 	print(args)
# 	print(kwargs)
#
#
# sum_num(1,2,3,4,mm = 5,nn = 6)

# 输出结果是:
# 1
# 2
# (3, 4)
# {'mm': 5, 'nn': 6}
# (3, 4)
# {'mm': 5, 'nn': 6}

"""引用:
在python中:

1.可以使用id函数查看引用的是否为同一个内存空间,如果返回值相同,说明引用的是同一个

2.值 是靠引用来传递的


"""
# a = 1
# b = a
#
# print(id(1))  # 1的id也是1908367584
# print(id(a)) # 输出id 1908367584
# print(id(b))  # 输出的id 是1908367584,和a的相同,说明引用的是同一个,均是1


"""模块:
模块 就好比是工具包,要想使用这个工具包中的工具,就需要导入(import)这个模块

每一个以扩展名.py结尾的Python源代码文件都是一个模块

在模块中定义的全局变量,函数都是模块能够提供给外界直接使用的工具

"""

"""
学生名片管理系统:
步骤:
1.框架搭建
2.新增名片
3.显示所有名片
4.查询名片
5.查询成功后修改.删除名片
6.能够直接运行

2.1 搭建名片管理系统框架结构
	1.准备文件,确定文件名,保证能够在需要的位置编写代码
	2.编写主运行循环,实现基本的用户输入和判断

2.2 文件准备:
	1.新建cards_main.py保存 主程序代码
		程序的入口
		每一次启动名片系统都通过main这个文件启动
	2.新建cards_tools.py保存名片的所有功能函数
		将对名片的 新增.查询.修改.删除 等功能 封装在不同的函数中
pass:
	pass 就是 一个空语句,不做任何事情,一般用作占位语句
	目的是为了保持程序结构的完整性

TODO注释:
	在# 后跟上TODO,用来标记需要去做的工作

"""

"""set(集合) list tuple
set:集合类型

set.list.tuple 之间可以相互转换

使用set 可以快速的完成对list中的元素去重复的功能

"""

"""列表推导式:






"""
# # 基本方式
# a = [x for x in range(7)]
# print(a)
#
# a = [x for x in range(2,3)]
# print(a)

# 在循环中使用if

# a = [x for x in range(3,10) if x % 2 == 0]
# print(a)

# 两个for循环
# a = [(x,y) for x in range(1,3) for y in range(3)]
# print(a)
# # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

"""练习:
请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
"""
# 分组:而且是list
# a = [x for x in range(1, 101)]
# print(a)
# b = [a[x: x + 3] for x in range(0, len(a), 3)]
# print(b)


# print([x for x in range(0, 101, 3)])

# print(i)

"""匿名函数:

用lambda(就是一个希腊字母)关键词能创建小型匿名函数.这种函数是因为省略了用def声明函数的标准步骤,因此被称作匿名函数.

lambda函数的语法只包含一个语句:
lambda[参数1,[,参数2,...参数n]]:表达式

lambda函数能接收 任何数量 的 参数 但是只能返回一个 表达式 的值

匿名函数不能直接调用print()函数,因为lambda需要的是一个表达式
"""
# sum = lambda arg1, arg2: arg1 + arg2
#
# # 调用sum函数
# print('Value of total:%d' % sum(10, 100))  # Value of total:110
# print('Value of total:',sum(100, 20),sep='')  # Value of total:120
# # 这样子是sep=''为关键字参数设置分隔符为空,sum(100,20)是普通参数.普通参数必须放到关键字参数前面

""" 应用场合:函数作为参数传递"""

# def fun(a, b, opt):
# 	print('a = %d' % a)
# 	print('c = %d' % b)
# 	print('result = %d' % opt(a, b))  # 记得%d占位符
#
#
# fun(1, 2, lambda x, y: x + y)  # lambda x,y:x + y 就是一个表达式,最终的结果是一个值(表达式也可以是)
# a = 1
# c = 2
# result = 3

# 可以被调用(callable)的意思是定义之后的值是否可以被修改.比如字符串定义之后就没法改动了
#
# stus = [
# 	{'name': 11, 'age': 23},
# 	{'name': 12, 'age': 73},
# 	{'name': 13, 'age': 13}
# ]
#
# # stus.sort(key=lambda x: x['name'])  # 关键字参数
# stus.sort(key=lambda x: x['age'])  # 关键字参数
# print(stus)
# 输出:
# [{'name': 11, 'age': 23}, {'name': 12, 'age': 73}, {'name': 13, 'age': 13}]

# [{'name': 13, 'age': 13}, {'name': 11, 'age': 23}, {'name': 12, 'age': 73}]



# TypeError: 'str' object is not callable

# str = '15666'
# str[0] = 5555  TypeError: 'str' object does not support item assignment

"""递归函数:
如果一个函数在内部调用其本身,这个函数就是递归函数
阶乘:
递归函数一般都需要一个条件判断来打破死循环,否则会导致到达最大嵌套次数,程序报错


"""

# def step_num(num):
# 	if num > 1:
# 		return num * step_num(num - 1)  # 就是这里继续调用了step_num()这个函数本身
# 	else:
# 		return 1


# print(step_num(6))

"""文件操作介绍:
文字.图片.音频,视频等等

作用:就是把一些数据存储起来,可以让程序在下一次执行的时候直接使用,而不必重新制作一份,省时省力.

"""

"""文件的打开与关闭:
Python:使用open()函数,可以打开一个已经存在的文件,或者创建一个新文件
格式:open(文件名,访问模式)


示例如下:
f = open('test.txt','w)

访问模式:

w:打开一个文件只用于写入.如果该文件已经存在,则将其覆盖,如果该文件不存在,则创建新文件

r:以只读方式打开文件.文件的指针将会放在文件的开头,.这是默认模式

a:打开一个文件用于追加.如果该文件存在,文件指针将会放在文件的结尾.也就是说,新的
内容将会被写入到已有内容之后.如果该文件不存在,创建新文件进行写入.

rb:以二进制格式打开一个文件用于只读.文件指针将会放在文件的开头.这是默认模式

wb:以二进制格式打开一个文件只用于写入.如果该文件已存在则将其覆盖.如果该文件不存在,创建新文件

ab:以二进制格式打开一个文件用于追加.如果该文件已存在,文件指针将会放在文件的结尾.也
就是说,新的内容将会被写入到已有内容之后.如果该文件不存在,创建新文件进行写入.

关闭文件:close()函数


f = open('test.txt', 'w')  # 新建一个文件,文件名为test.txt
f.close()  # 关闭这个文件

"""

"""写数据(write):
使用write()函数可以完成向文件写入数据

f = open('test.txt','w')  # w模式下:如果文件不存在就创建,如果存在就先清除原来的文件数据,然后重新写入数据
f.write('hello world,I am here!')
f.close()

"""

"""读数据:

使用read(num)可以从文件中读取数据,num表示要从文件中读取的数据长度(单位是字节).
如果没有传入num,那么就表示读取文件中所有的数据(就是要读取多少数据的意思)

注意:如果open()是打开一个文件,那么可以不用写打开的模式,即只写
open('test.txt)

如果使用read()读了多次,那么后面读取的数据就是从上次读完后的位置开始的(可以理解为光标此时在前面那次读完的位置,从这里开始读)

"""

# f = open('test.txt', 'r')
#
# content = f.read(5)
#
# print(content)  # hello
#
# print('-' * 30)
#
# content = f.read(5)
#
# print(content)   #  worl
#
# content = f.read(5)
#
# print(content)  #d,I a
#
# f.close()

# 记得,号,空格也算是一个字符
# hello world,I am here!hello world,I am here!
# f = open('test.txt','r')
# content = f.read()  # 如果没有传入num,那么就表示读取文件中所有的数据
#
# print(content)
#
# f.close()

"""按照行方式读取数据:readlines

和read()没有参数的时候一样,readlines可以按照行的方式把整个文件中的内容进行一次性读取,并且返回的是一个列表,其中的每一行的数据为一个元素.







"""

# f = open('test.txt', 'r')
# content = f.readlines()
# print(type(content))  # <class 'list'>
#
# i = 1  # i是一个标识行数的作用
#
# for temp in content:
# 	print('第%d行:%s' % (i, temp))
# 	i += 1
#
# f.close()



"""读数据:readline

一次只能读一行.





"""

# f = open('test.txt','r')
#
#
# content = f.readline()
# print('第一行:%s' % content)
#
# content = f.readline()
# print('第二行:%s' % content)
#
# f.close()

# 第一行:hello world1,I am here!hello world,I am here

# 第二行:hello world2,I am here!hello world,I am here!

"""制作文件的备份:

要求:输入文件的名字,然后程序自动完成对文件进行备份

"""
# # 提示输入文件
# oldFileName = input('输入要拷贝的文件名字:')  # 这里必须输入文件的后缀名,格式是:输入要拷贝的文件名字:test.txt
#
# # 以只读的方式打开文件
# oldFile = open(oldFileName, 'rb')
#
# # 提取文件的后缀
# fileFlagNum = oldFileName.rfind('.')  # find()函数返回的是一个数字,表示从右开始计数的索引(索引值仍然是从左开始计的那种0->len()-1正索引,不是负索引)
# if fileFlagNum > 0:
# 	fileFlag = oldFileName[fileFlagNum:]  # fileFlag是文件的后缀名
# # 组织新的文件名字
# newFileName = oldFileName[:fileFlagNum] + '[副本]' + fileFlag  # 添加文件的后缀名
#
# # 创建新文件
# newFile = open(newFileName, 'wb')
#
# # 把旧文件中的数据,一行一行的进行复制到新文件中
# for lineContent in oldFile.readlines():
# 	newFile.write(lineContent)
#
# # 关闭文件
# oldFile.close()
# newFile.close()


# str = '1122'
# print(str[:3])


"""文件的定位读写:
1.获取当前读写的位置:文件名.tell()



"""

# f = open('123.txt','r+')  # 写模式
# # f.write('hello world')  # 正在写入(指的是将原有内容擦除,然后写入新的数据)
#
# content = f.read()  # 正在读取,相互冲突了
# print(content)  # 打印不出内容?

# 打开一个已经存在的文件,读和取都是需要文件在打开的状态下才能进行
# f = open('test.txt', 'r')
# str = f.read(3)
# print('读取的数据是:', str)
# # 查找当前的位置
# position = f.tell()
# print('当前文件位置:', position)  # print()普通参数的运用
#
# str = f.read(3)
# print('读取的数据是:', str)
#
# position = f.tell()
# print('当前文件位置:', position)
#
# f.close()


# 读取的数据是: hel
# 当前文件位置: 3
# 读取的数据是: lo
# 当前文件位置: 6

"""定位到某个位置:

如果文件在读写的过程中,需要从另外一个位置进行操作的话,可以使用seek()函数
seek(offset,from)
	offset:偏移量
	from:方向
		0:表示文件开头
		1:表示当前位置
		2:表示文件末尾


"""
# 要求:位置设为 从文件开头,偏移5个字节

# 打开一个已经存在的文件
# f = open('test.txt','r')
# str = f.read(30)  # 读取30个字节
# print('当前读取的数据是:',str)
#
# # 查找当前位置
# position = f.tell()
# print('当前文件位置:',position)
#
# # 重新设置位置
# f.seek(0,2)  # 偏移量:就是偏移了多少的意思,这里表示从文件开始位置(0位置)偏移5个字节大小
#
# # 查找当前位置
# position = f.tell()
# print('当前文件位置:',position)
#
# f.close()


# 当前读取的数据是: hello world1,I am here!hello w
# 当前文件位置: 30
# 当前文件位置: 182    f.seek(0,2) 这是从末尾开始计数,偏移量为0,实际就是文件最末尾的位置.

# 报错了:io.UnsupportedOperation: can't do nonzero end-relative seeks
# Python3中非二进制文件在offset和whence中至少有一个参数必须设置为0,Python2中没有 这个限制

# str = 'hello world1,I am here!hello world,I am here!hello world2,I am here!hello world,I am here!hello world2,I am here!hello world,I am here!hello world2,I am here!hello world,I am here!'
# print(len(str))


"""预习:文件.文件夹的相关操作:
文件重命名:os模块中的rename()可以完成对文件的重命名操作

格式:rename(需要修改的文件名,新的文件名)

"""
# rename() 不会删除原来的 renames()则会把旧的文件删除
# import os
# os.renames('tree1.txt','tree.txt')



"""删除文件:
os中的remove()可以完成对文件的删除操作
remove(待删除文件名)

"""
# # remove()删除
# import os
# os.remove('test[副本].txt')

"""创建文件夹:

os.mkdir()
"""
# import os
# os.mkdir('张飒')


"""获取当前目录:

os.getcwd()

"""
# import os
#
# print(os.getcwd())  # E:\黑马Python21期基础班\Python基础班\Python基础第一天

"""改变默认目录:

os.chdir('目录名')

"""
# import os
# os.chdir('张飒')
# print(os.getcwd())
# E:\黑马Python21期基础班\Python基础班\Python基础第一天\张飒

"""获取目录列表:


os.listdir()

输出的数据类型是一个列表
"""
# import os
#
# print(os.listdir('E:\黑马Python21期基础班\Python基础班'))
# ['.idea', 'HMCards', 'Python基础第一天', 'Python基础第七天', 'Python基础第三天', 'Python基础第二天', 'Python基础第五天', 'Python基础第六天', 'Python基础第四天', '名片管理系统', '每日作业', '练习', '飞机大战']


# ['hello.py', 'prepare_语法_函数.py', 'prepare_面向对象.py', 'tree.txt', '张飒']


"""删除文件夹:

os.rmdir('张飒')
"""
# import os
# os.rmdir('张飒')


"""应用:批量修改文件名:



"""
# import os
#
# path = input('输入需要批量修改文件名的文件夹名称:')
# # 跳转路径
# os.chdir(path)
# # 获取当前的绝对路径
# full_path = os.getcwd()
# print(full_path)
# # print(os.listdir())
# # 遍历目标文件夹
# for subpath_name in os.listdir():
# 	new_file_name = '[附件]' + subpath_name
# 	# 给每个文件改名
# 	os.rename(subpath_name, new_file_name)
