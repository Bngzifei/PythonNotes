"""
用函数实现一个判断用户输入的年份是否是闰年的程序。

提示：
1.能被400整除的年份
2.能被4整除，但是不能被100整除的年份
以上2种方法满足一种即为闰年

"""

# def runnian1(nian):
# 	"""能被400整除的"""
# 	if nian % 400 == 0:
# 		print('是闰年')
#
#
# def runnian2(nian):
# 	"""能被4整除,但不能被100整除"""
# 	if nian % 4 == 0:
# 		if nian % 100 != 0:
# 			print('是闰年')
# 		else:
# 			print('不是闰年')
# 	else:
# 		print('不是闰年')
#
#
# def main(nian):
#
# 	if runnian1(nian) or runnian2(nian):
# 		print('闰年')
#
#
# main(1900)  # 1000不是闰年 1900也不是

"""
使用函数求前20个斐波那契数列。

提示：
斐波那契数列：1,1,2,3,5,8,13,21...即: 起始两项均为1，此后的项分别为前两项之和。

"""

# def feibo_sum(num):
# 	# n = int(input('输入个数:'))
# 	c = [1, 1]
# 	for i in range(num):  # i从0开始,到19截止,和索引值吻合,刚好来表示索引
# 		a = c[i] + c[i + 1]
# 		c.append(a)
# 	print(c)
#
#
# feibo_sum(20)

"""
老师分配办公室的应用练习

将办公室的个数，和老师的个数作为参数传递给函数

把最后的结果作为返回值返回

"""


def school(n):
	"""空教室添加到学校的功能"""
	school = []
	# n = int(input('输入教室数目:'))
	for i in range(n):
		school.append([])  # TODO 对教室逐一添加
	# print(school)
	return school


def teachs(m):
	"""将老师添加到一个空列表"""
	teachs = []
	# m = int(input('输入老师个数:'))
	for i in range(m):
		name = input('输入老师姓名:')
		teachs.append(name)
	# print(teachs)
	return teachs


# teachs(4)

def fenpei1(schools, teachers):
	"""分配老师到教室,保证每个教室都有一个"""
	import random
	for jiao in schools:
		index1 = random.randint(0, len(teachers) - 1)
		name = teachers.pop(index1)
		jiao.append(name)
	for teacher in teachers:
		index2 = random.randint(0, len(schools) - 1)
		schools[index2].append(teacher)
	return print("分配结果是:%s" % schools)


def main(n, m):
	if n <= m:
		a = school(n)
		b = teachs(m)

		return fenpei1(a, b)
	else:
		print('输入的数据不合法,请重新输入')


main(3, 8)  # [['3', '7'], ['5', '1', '2', '4'], ['8', '6']]


# def panduan(n, m):
# 	while True:
# 		if len(school(n)) < len(teachs(m)):
# 			panduan(n,m)
# 		else:
# 			print('输入的数据不合法,老师数目应该大于教室数目,请重新输入数据')
# 			break
#
#
# def main(n, m):
# 	"""主函数"""
# 	school(n)
# 	teachs(m)
# 	panduan(n, m)
# 	return fenpei1(school(n),teachs(m))

# teach_num1 = teachs(lao_nums).__len__()
#
# jiao_num1 = school(jiao_nums).__len__()
#
# # 先安排教室,以保证每个教室有一个
# for i in range(jiao_num1):
# 	index1 = random.randint(0, teach_num1)  # q代表教室数目,r代表老师数目
# 	# print("index1: %d" % index1)
# 	name = teachs(lao_nums).pop(index1)
# 	# print(name)
# 	school(jiao_nums)[i].append(name)
#
# # 安排剩下的老师,这时候老师列表已经发生了变化
# for j in range(jiao_num1 - teach_num1):
# 	index2 = random.randint(0, jiao_num1)  # 把剩下的老师(从0开始,有序的)随机添加到某个教室
#
# 	school(jiao_nums)[index2].append(teachs(lao_nums)[j])

# return print('分配结束后:%s' % school(jiao_nums))

# a = school(3)
#
# b = teachs(8)

# fenpei1(school(3),teachs(8))

# fenpei1([[],[],[]],['q','w','e','r','t','y','u'])

# def fenpei2(num1,num2):
# 	a = school(num1)
# 	b = teachs(num2)
# 	fenpei1(a,b)
# 	return
