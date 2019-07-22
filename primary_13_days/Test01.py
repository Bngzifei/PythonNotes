"""
 编号:SJ003497本题分数:13分  *难度：
1.【代码题】
在Python3中编写程序，键盘录入1到12 ，对应输出该月份对应的季节 。如果输入的不是1到12，输出提示信息：
您输入的数据有误。

"""

# try:
# 	num = int(input('输入数字1-12:'))
# 	if num == 1:
# 		print('这是1月份,这个月是冬季')
# 	elif num == 2:
# 		print('这是2月份,这个月是冬季')
# 	elif num == 3:
# 		print('这是3月份,这个月是春季')
# 	elif num == 4:
# 		print('这是4月份,这个月是春季')
# 	elif num == 5:
# 		print('这是5月份,这个月是春季')
# 	elif num == 6:
# 		print('这是6月份,这个月是夏季')
# 	elif num == 7:
# 		print('这是7月份,这个月是夏季')
# 	elif num == 8:
# 		print('这是8月份,这个月是夏季')
# 	elif num == 9:
# 		print('这是9月份,这个月是秋季')
# 	elif num == 10:
# 		print('这是10月份,这个月是秋季')
# 	elif num == 11:
# 		print('这是11月份,这个月是秋季')
# 	elif num == 12:
# 		print('这是12月份,这个月是冬季')
# 	else:
# 		print('输入的数据不合法')
# except ValueError as error:
# 	print('输入的数据不合法')

"""
2.提示用户输入5个整数，依次存入到列表中，并且按照从大到小的顺序依次输出到终端上
"""
# # 详细版
# list1 = []
# for i in range(5):
# 	num = int(input('输入第%d个数字:' % (i + 1)))
# 	list1.append(num)
# # print('列表是:%s' % list1.sort(reverse=False))
# # print(sorted(list1, key=int, reverse=False))
# list1.sort(reverse=True)  # sort() 默认是升序
# print(list1)  # 输出的是list1
# 冒泡排序法:
# for m in range(4):  # 不能到5,需要保证有m+1 的存在
# 	if list1[m] < list1[m + 1]:
# 		temp = list1[m + 1]
# 		list1[m + 1] = list1[m]
# 		list1[m] = temp
# # print(list1)
# for m in range(3):
# 	if list1[m] < list1[m + 1]:
# 		temp = list1[m + 1]
# 		list1[m + 1] = list1[m]
# 		list1[m] = temp
# # print(list1)
# for m in range(2):
# 	if list1[m] < list1[m + 1]:
# 		temp = list1[m + 1]
# 		list1[m + 1] = list1[m]
# 		list1[m] = temp
# # print(list1)
# for m in range(1):
# 	if list1[m] < list1[m + 1]:
# 		temp = list1[m + 1]
# 		list1[m + 1] = list1[m]
# 		list1[m] = temp
# print('排序后的列表是:%s' % list1)

# # 嵌套版
# list1 = []
# for i in range(5):
# 	num = int(input('输入第%d个数字:' % (i + 1)))
# 	list1.append(num)
#
# print('列表是:%s' % list1)
#
# for i in range(4, 0, -1):
# 	for j in range(i):
# 		if list1[j] < list1[j + 1]:
# 			temp = list1[j + 1]
# 			list1[j + 1] = list1[j]
# 			list1[j] = temp
# print('排序后的列表是:%s' % list1)

"""
3.将字符串str1 =“abangsgjlgldsag”的去重结果保存在str2中并打印。

"""
# str1 = 'abangsgjlgldsag'
# list2 = []
# for i in range(len(str1)):  # 不使用len(str1) - 1 是因为range(n)取不到n,要想取到列表中的最后一个元素,就得索引值=len() - 1 + 1
# 	print(str1[i])
# 	if str1[i] not in list2:
# 		list2.append(str1[i])
# print(list2)
#
# str2 = ''
# for i in range(len(list2)):  # 保证能取到最后一个元素
# 	str2 += list2[i]
# print(str2)
"""
4.定义一个学生类，实例属性有name(姓名)，age（年龄），提示用户分别输入3个学生信息（姓名以及年龄），
根据用户输入的信息创建3个学生对象，将这3个学生对象存入列表，遍历列表删除年龄小于18岁的学生对象，
最后输出列表中剩余的学生信息

"""
#
# class Student:
# 	"""学生类"""
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# stu_list = []  # 学生列表
# for i in range(3):
# 	name = input('输入第%d个学生姓名:' % (i + 1))
# 	age = int(input('输入第%d个学生年龄:' % (i + 1)))
# 	student = Student(name, age)
# 	stu_list.append(student)
#
# # print(stu_list)
# templist = []  # 临时列表,用来存放准备删除的学生对象
# # 先遍历列表，记录下需要删除的元素
# for stu in stu_list:
# 	if stu.age < 18:
# 		templist.append(stu)
# # 遍历完列表，再对需要删除的对象进行处理
# for stu1 in templist:
# 	stu_list.remove(stu1)
# for i in range(len(stu_list)):
# 	print('第%d个学生姓名:%s' % (i + 1, stu_list[i].name))
# 	print('第%d个学生年龄:%d' % (i + 1, stu_list[i].age))

"""
5.
定义一个电影类。
 有以下4个实例属性：电影名称、价格、数量、票房（总价）
有以下实例方法：
1 获取电影的名称：get_name()；
2 获取价格：get_price()；
3 获取所卖出的数量：get_nums()
4.获取票房总价：get_money()
PS:票房总价=价格*数量
写好类以后，定义1个电影类对象，调用以上方法进行测试，并打印结果

"""


class Movie:
	"""电影类"""
	
	def __init__(self, name, price, nums):
		self.name = name
		self.price = price
		self.nums = nums
		self.money = None
	
	def get_name(self):
		return self.name
	
	def get_price(self):
		return self.price
	
	def get_nums(self):
		return self.nums
	
	def get_money(self):
		return self.price * self.nums
	
	def __str__(self):
		return '电影:%s,单价:%d,数量:%d,票房:%d' % (self.name, self.price, self.nums, self.price * self.nums)


movie1 = Movie('西红柿首富', 40, 200)

print(movie1.get_name())
print(movie1.get_nums())
print(movie1.get_price())
print(movie1.get_money())

print(movie1)
