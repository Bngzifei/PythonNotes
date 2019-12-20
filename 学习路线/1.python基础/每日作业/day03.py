"""
练习题2
列表的基本应用

要求：

1.从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母

2.从键盘获取5个学生的名字，然后随机抽出一名学生去打扫卫生

3.老师分配办公室的应用练习

	输入办公室个数
	输入老师的个数
	然后将了老师分配到办公室，保证每个办公室至少一个，如果
4.名片管理器v2.0

在上一版本的基础上，增加可以添加多个名片的功能
可以打印所有名片的功能
可以删除名片的功能
"""

"""1.代码:"""
# name_list = []  # 创建一个空列表,用来存储输入的5个学生姓名
# # 这个循环是先执行的
# for i in range(5):  # 循环5次,输入5个学生姓名,可以表示索引
# 	name = input('输入学生姓名:')
# 	name_list.append(name)  # 将输入的name添加到name_list中
#
# 	#记着:字符串类型的数据类型和list列表一样,自带索引属性,可以直接使用角标进行取值操作
# 	# 记得先实现功能,然后再合并成精简的那种
# print(name_list)  # 输出整个name_list
# # 下面这个循环一定是后执行的
# for name2 in name_list:
# 	print(name2[1])  # 输出每个学生的第二个字母

"""2.代码"""
# import random  # 导入随机数包
# name_list = []  # 创建一个空列表,用来存储输入的5个学生姓名
#
# # 这个循环是先执行的
# for i in range(5):  # 循环5次,输入5个学生姓名,可以表示索引
# 	name = input('输入第 %d 个学生姓名:' % (i + 1))
# 	name_list.append(name)  # 将输入的name添加到name_list中
#
# # 记着:字符串类型的数据类型和list列表一样,自带索引属性,可以直接使用角标进行取值操作
# # 记得先实现功能,然后再合并成精简的那种
# print("输入的学生列表为:%s" % name_list)  # 输出整个name_list
# # # 下面这个循环一定是后执行的
# index1 = random.randint(0, 4)
# print("索引值:%d" % index1)
# print("抽中的学生名字为:%s" % name_list[index1])
"""3.老师分配办公室代码"""

# 随机组合的意思
# import random
# while True:
# 	num1 = int(input('请输入教室的个数:'))
# 	num2 = int(input('请输入老师的个数:'))
# 	if num2 >= num1:
# 		break
# 	print('老师数小于教室数,不符合要求,请重新输入')
#
# school = []  # 表示学校,list类型,用来装教室,[]表示一个空教室
# tea_list = []  # 老师列表,用来装输入的老师姓名
#
# for i in range(num1):
# 	school.append([])  # 将教室逐一添加到教室组中
#
# for j in range(num2):
# 	name = input('请输入老师姓名:')
# 	tea_list.append(name)
#
# print("学校是: %s " % school)
# print("老师列表是:%s" % tea_list)
#
# # 优先保证每个教室都有一个老师,所以是从school[0]开始到school[2]都添加一个随机的老师,并且老师数目-1
# for off in school:
# 	index2 = random.randint(0, len(tea_list) - 1)
# 	teacher = tea_list.pop(index2)  # 利用pop()有返回的特性
# 	off.append(teacher)
# # 保证了每个教室不为空的情况下,继续分配剩下来的老师.
# for name in tea_list:
# 	index1 = random.randint(0, len(school) - 1)
# 	school[index1].append(name)  # 直接添加,不再需要老师-1,因为老师此时是有序的被分配完.
#
# print("分配结束后：", school)
# i = 1
# for off in school:
# 	print("办公室%d的人数为:%d" % (i, len(off)))
# 	i += 1
# 	for name in off:
# 		print('%s' % name, end=' ')
# 	print('\n')
# 	print('-' * 20)

"""8个人分配到3个办公室"""
# import random
#
# offices = [
# 	[], [], []
# ]
# names = ['武沛齐', '李大申', '张学良', '冯玉祥', '阎锡山', '孙立人', '戴安澜', '蒋中正']  # 8个老师
#
# # 办公室索引0,1,2随机生成
#
# for name in names:
# 	index = random.randint(0, 2)
#
# 	offices[index].append(name)  # 将8个人中的某一个随机添加到某个办公室
# # 到这里就分配完成
# # 获取办公室信息	,i是办公室的编号
# i = 1
# for tempNames in offices:
# 	print('办公室%d的人数为:%d' % (i, len(tempNames)))
# 	i += 1
# 	for name in tempNames:
# 		print('%s' % name, end=' ')
# 	print('\n')  # 换行进行输出
# 	print('-' * 20)  # 分隔线
# a = []
# b = []
# c = int(input('输入个数:'))
# for i in range(c):
# 	a.append(b)
# print(a)
# import random
# # 办公室数量默认是0
# room_nums = 0
# # 教师数量默认是0
# teacher_nums = 0
# while True:
#     # 办公室个数
#     r_nums = input("请输入办公室的个数：")
#     # 老师的个数
#     t_nums = input("请输入老师的个数：")
#
#     # 如果教师数目大于等于办公室数目，才退出循环，并赋值给room_nums、teacher_nums
#     # 否则重新输入
#     if int(r_nums) <= int(t_nums):
#         room_nums = int(r_nums)
#         teacher_nums = int(t_nums)
#         break
#     print("教室数低于办公室数，请重新输入")
#
# # 创建办公室列表，即创建一个嵌套列表
# rooms = []
# while room_nums>=1:
#     rooms.append([])
#     room_nums -= 1
#
# # 创建老师列表，并添加老师
# teachers = []
# while teacher_nums>=1:
#     teacher_nums -= 1
#     teachers.append("teacher%d"%(teacher_nums+1))
# # 开始安排办公室
# # 1.先随机选出三位老师，依次放到办公室中
# for room in rooms:
#     # 随机选出一名老师，注意teachers长度会变
#     index = random.randint(0,len(teachers)-1)
#     # pop方法弹出一个元素，并列表中删除
#     teac = teachers.pop(index)
#     room.append(teac)
#
# # 2.将剩下的老师，再随机分配
# for teacher in teachers:
#     room_index = random.randint(0, len(rooms)-1)
#     rooms[room_index].append(teacher)
# print("分配结束后：", rooms)

"""
有10个球分别3红、3蓝、4白，现需要将这10个球放入这3个盒子，要求每个盒子至少有一个白球，请用程序实现
"""
import random
red = [1, 2, 3]
blue = [4, 5, 6]
white = [7, 8, 9, 10]
hezi = [[], [], []]
red.extend(blue)  # 记得是list1.extend(list2),然后输出list1
# print()  # 有误
# print(red)
for i in hezi:
	index3 = random.randint(0,len(white) - 1 )  # 因为每次循环之后这里的len()会减小
	# pop()方法弹出一个元素,并在white表中删除
	print(index3)
	h = white.pop(index3)
	i.append(h)  # 是盒子组中的每个盒子添加弹出的那个

# 将剩下的一个white(不知道具体是哪个)随机的添加到盒子中(这里面只有盒子组的长度不会变化,一直都是长度为3)
for j in white:
	index4 = random.randint(0,2)
	hezi[index4].append(j)
for k in red:
	index5 = random.randint(0,2)
	hezi[index5].append(k)
print(hezi)