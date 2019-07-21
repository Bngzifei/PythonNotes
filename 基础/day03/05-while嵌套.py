"""
while嵌套
输出5行*

"""
# i = 1
# while i<=5:
# 	print('*' * i)
# 	i += 1

"""
默认会加换行符\n

print('*')
print('*')
print('*')

print('*\n')
print('*',end='')
print('*')
print('*',end='888')
"""
# print('*',end='')
# print('*',end='')
# print('*',end='')
# print()


# row = 1
# while row <= 5:
#
# 	col = 1
# 	while col <= row:  # row 这里是实现col < 5 中的5效果
# 		print('*', end='')
# 		col += 1
#
# 	print()
# 	row += 1


# 遇到每一行输出相对应的*,即行数和输出内容的个数一致,或者存在某种规律时,就是套用这种循环体的格式,最明显的就是九九乘法表的实现

#  循环嵌套时外层循环执行一次,内层循环会执行若干次
#  外循环控制行数,内循环控制列数  即外循环控制一共有几行,内循环控制每一行有几个东东(列)

# row = 1
# while row <= 9:
#
# 	col = 1
# 	while col <= row:
# 		print('%d * %d = %d' % (col, row, (col * row)), end='\t')
# 		col += 1
#
# 	print()
# 	row += 1

"""
* 倒置过来实现
外行,内列:即外部的大循环是控制行的实现效果,内部的小循环是控制列的实现效果

row = 1
while row <= 5:

	col = 5
	while col >= row:  # row 这里是实现col < 5 中的5效果
		print('*', end='')
		col -= 1  # 列数,这里用来表示*的个数

	print()  # 控制光标,使其跳转到下一行
	row += 1  # 行数,实现从1到5,一共5行
	
	
"""

# for row in range(1,6,1):
# 	for col in range(6,1,-1):
# 		if col > row:
# 			print('*',end='')
# 	print()
#
# for row in range(1, 10, 1):
# 	for col in range(9, 0, -1):
# 		if col > row:
# 			print('%d * %d = %d' % (row, col, row * col),end='\t')  # 如果不加end='\t',输出的效果就是直接跳到下一行,有了end='\t'之后就是光标在原来字符结尾处右移4个字符的位置,横向制表符的作用.
# 	print()
"""倒置的九九乘法表"""

"""
row = 1
while row <= 9:  # 一共9行

	col = 9
	while col >= row:  # row 这里是实现col < 5 中的5效果
		print('%d * %d = %d' % (row,col,row * col), end='\t')  # \t 是4个字符位,以下能对齐纯属意外.
		col -= 1  # 列数,这里用来表示*的个数

	print()  # 控制光标,使其跳转到下一行
	row += 1  # 行数,实现从1到5,一共5行


"""

"""
num1 = int(input('输入周一~周日(使用数字1-7分别代表):'))

if num1 == 1:
	print('周一')
elif num1 == 2:
	print('周二')
elif num1 == 3:
	print('周三')
elif num1 == 4:
	print('周四')
elif num1 == 5:
	print('周五')
else:
	print('周末')



"""

# row = 1
# while row <= 5:
#
# 	col = 5
# 	while col >= row:  # row 这里是实现col < 5 中的5效果
# 		print('*', end='')
# 		col -= 1  # 列数,这里用来表示*的个数
#
# 	print()  # 控制光标,使其跳转到下一行
# 	row += 1  # 行数,实现从1到5,一共5行

"""
要求:

编写代码模拟用户登陆。要求：用户名为python，密码123456，如果输入正确，打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入。
username = 'python'
password = '123456'

i = 1
while i:
	username1 = input('输入用户名:')
	password1 = input('输入密码:')

	if username1 == username and password1 == password:
		print('欢迎光临')
		break  # break 和 continue均是放到if条件块里面去
	elif username1 == username and password1 != password:
		print('密码错误,请检查')
	elif username1 != username and password1 == password:
		print('用户名错误,请重新输入')
	else:
		print('用户名和密码均错误')
"""

"""
记得逻辑要严谨:各种情况要区分清楚.1.密码错名对2.密码对,名错3.用户名和密码都错4.用户名和密码均对
输入用户名:1
输入密码:5
用户名和密码均错误
输入用户名:python
输入密码:5
密码错误,请检查
输入用户名:8
输入密码:123456
用户名错误,请重新输入
输入用户名:python
输入密码:123456
欢迎光临

"""

"""
使用while、if来完成剪刀石头布程序，要求，当玩家第3次获胜时才退出游戏，否则继续玩

就是将循环终止条件设定为获胜的次数,不要想多了.

import random

win_times = 0
while win_times < 3:
	player = int(input('请出拳 石头(1)/剪刀(2)/布(3):'))
	computer = random.randint(1,3)
	print(computer)
	if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
		win_times += 1
		print('渣渣电脑,老子赢了 %d 次!!!' % win_times)
	elif player == computer:
		print('不行,再来一局')
	else:
		print('厉害炸了,我输了...')

"""

"""
设计“过7游戏”的程序, 打印出1-100之间除了含7和7的倍数之外的所有数字。

for i in range(1,101):
	if i % 7 != 0:
		print(i)
或者:
i = 0
while i < 100:
	i += 1
	if i % 7 == 0:  # 这么设计的目的是跳过i+1=7,但是打印输出的是i,这样设计就实现了将7和7的倍数剔除的效果
		continue
	else:
		print(i)   # 打印的是7之前的那个数字,或者7的整数倍-1的数字,成功避免7陷入死循环无法跳出来.逻辑上的
"""
# i = 0
# while i <= 99:
#  i += 1
#  if i % 7 == 0 or i % 10 == 7 or i//10 == 7:
#      continue
#  else:
#      print(i)

"""
使用while，完成以下图形的输出
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    
一共是9行,9列

i=1
while i <= 9:
    if i<=5:
        print(' '*(5-i),'*'*(2*i-1))
    else:
        print(' '*(i-5), '*'*(2*(10-i)-1))
    i+=1




row = 1
while row <= 9:
	if row <=5:
		print(' ' * (5 - row) + '*' * (2 * row - 1) + ' ' * (5 - row) )
	else:
		print(' ' * (row - 5) + '*' * (19 - 2 * row) + ' '  * (row - 5) )
	row += 1
	
	      
"""
row = 1
while row <= 9:
	if row <=5:
		print(' ' * (5 - row) + '*' * (2 * row - 1) + ' ' * (5 - row) )
	else:
		print(' ' * (row - 5) + '*' * (19 - 2 * row) + ' '  * (row - 5) )
	row += 1


"""

# 吴杰积 09:29:18

就是将两个三角形程序拼接在一起
i = 1
while i <= 5:
    j = 5
    while i <= j:
        print(" ", end="")
        j -= 1
    k = 1
    while k <= (2*i-1):
        print("*", end="")
        k += 1
    print("")
    i += 1

x = 1
while x <= 4:
    y = 1
    while y <= (x+1):
        print(" ", end="")
        y += 1
    z = 7
    while z >= (2*x-1):
        print("*", end="")
        z -= 1
    print("")
    x += 1


"""
