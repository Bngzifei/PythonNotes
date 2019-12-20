"""8个老师随机分配到3个教室"""
import random

# 定义一个列表变量,表示老师
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # 每个老师只分配一次
# office1 = []
# office2 = []
# office3 = []
# 优先顺序:保证功能实现
school = [[], [], []]  # 表示学校,学校里面有3个小办公室
# 1.遍历老师列表
for name in teachers:  # 安排老师是有顺序的,name是从A开始一直到H的
	# index = random.randint(0,(len(school) - 1))  # 随机数直接从0开始产生,因为0代表了索引位置的起始位置,这样会少了一部计算
	# office = school[index]  # 获取某个办公室列表
	# office.append(name)  # 把老师添加到办公室中 警告信息提示类型推导不一致
	school[random.randint(0, len(school) - 1)].append(name)
print(school)

# 2.遍历学校列表,取出每一个办公室列表
i = 1  # 计数变量表示第几个办公室
for office in school:
	print("第%d个办公室有%d个老师" % (i, len(office)))
	i += 1
	# 2.1 遍历办公室的小列表,取出办公室中的每个老师
	for name in office:
		print(name)

# 外循环代表了行,内循环代表了列,下面的3行6列
# [['B'],
#  ['H'],
#  ['A', 'C', 'D', 'E', 'F', 'G']]
# 为了不让教室出现空的情况,需要加if进行判断,只要保证每个教室的长度<3就可以.即判断到有教室的长度为3时,就不再往这个教室添加老师
