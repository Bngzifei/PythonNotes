# 判断是不回文数，形如101这类的

# num = eval(input("输入一个三位数（100-999）之间："))
# # 先判断是不是三位数
# if (num // 100 > 0 and num // 100 < 10):  # 实际上num整除100后的值应该在1-9之间的整数,此处>0实际就是>=1，小于10实际就是<=9
# 	if (num % 10 == (num // 100)):  # num%10是提取个位数，num//100是提取百位数
# 		print("是回文数")
# 	else:
# 		print("不是回文数")
# else:
# 	print("输入数据不是三位数")

# from itertools import combinations  # 导入组合模块
#
# nums = [1,2,3,4]
# list1 = []
#
# # 一个组合
# for i in combinations(nums, 3):
# 	list1.append(i)
# print(list1)
# print(len(list1))

# print([[x, x + 1, x + 2] for x in range(1, 101, 3)])

# -----------------------------------------异常使用格式---------------------------------->
try:
	错误代码部分 / 或者是可能出错的部分
except Exception as e:
	print('未定义/属性错误/文件不存在...')  # 直接输出错误提示
else:
	pass  # 这里是正确代码部分
finally:
	pass  # 最终都会执行的部分
# 实际上使用while / if 进行条件判断也是一种异常处理机制,有时候可以将try...except 和 if这些合用,只要能达到效果

# 从上至下的代码执行顺序,所以我们可以在其中加不同类型的if来筛选符合条件的可能性,每一种可能性都是一个if的情况,只要能分清楚这种情况的
# 所属范围<即if所在的缩进>其他的不要多想

# ----------------------------写项目的步骤:----------------------------------------->
"""
1.>规划好项目文件夹,一般有core/bin/log/home/conf...等等.
2.>记得先写步骤,完了再去写每一步的具体实现
3.>如果在写具体实现的过程中遇到没有实现的方法,可以在其上一行定义这个方法,先使用pass占位,直接进行下面的实现.

命令终端连接数据库:
1.>IP,PORT
2.>用户名
3.>密码

"""
# import re
#
# s = 'asas\ndsds\n56\nopp'
# list1 = s.split('\n')
# print(s.split('\n'))
# ss = []
# for str1 in list1:
# 	s1 = str1[::-1]
# 	print(s1)
# 	ss.append(s1)
# 	print(ss)
# print(re.sub(',','\n',ss))


# import re
#
# s = 'assfsfwfw'
# s1=''
# for i in len(s):
# 	if i % 2 == 0:
# 		s[i].capitalize()
# 		i.join(s1)
# 	if  i % 2 == 1:
# 		s[i].capitalize()
# 		s[i].join(s1)

"""

is 和 == 的区别:
is 是根据地址<即id>进行判断
== 是根据值进行判断
单引号,双引号,三引号的区别

"""

# s='sdfsfdf'
# print(s[-5:-2])
# print(s[-2:-5:])  # 步长为1的情况下,前大后小,反了
# print(s[-2:-5:-1])  # 步长为1的情况下,前大后小,反了,dfs

# 完全平方数
import math

# x+100+168 = y * y
# x+268=y**2
# list1 = []
# for y in range(100):
# 	list1.append(y * y)
# 	for i in range(100):
# 		if (i + 268) in list1:
# 			print(i,y)

list1 = [2, 3, 4, 5, 6, 7, 8]
# l = len(list1)
# for i in range(l - 1):
# 	if list1[i] % 2 == 0:
# 		list1[i], list1[i + 1] = list1[i + 1], list1[i]
# 	else:
# 		pass
# list1.reverse()
#
# print(list1)

# filter(list1,lambda x:if )
