"""
石头1剪刀2布3 猜拳游戏

import random  # 导入生成随机数模块
同行的注释时: #号和代码之间是2个空格,#号和注释内容之间是1个空格 这是PEP8的编码格式规范
"""
import random  # 导入生成随机数模块

# print(random.randint(1,3))  # 生成1,2,3其中的某一个 以后的才是左闭右开,前小后大,只能生成整数 区间: 数学意义上的()是开区间 ,[]是闭区间.取值规则是:取闭不取开.这里的random.randint(n,m)实际上是n<= 所取得值 <= m.原因是内置函数写死了.


player_num = int(input('请出拳 石头(1)/剪刀(2)/布(3):'))
computer_num = random.randint(1, 3)  # 可以在这里直接对一个变量进行随机数值的赋值运算.

if ((player_num == 1 and computer_num == 2) or
		(player_num == 2 and computer_num == 3) or
		(player_num == 3 and computer_num == 1)):
	print('胜利!')
elif player_num == computer_num:
	print('平局.')
else:
	print('输了...')
