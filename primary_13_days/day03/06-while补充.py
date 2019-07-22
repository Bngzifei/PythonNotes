# str1 = 'sdf\''
# print(str1)
"""
\r 会覆盖掉上一个内容  r:replace  代替的意思

\t 横向制表符, 位置固定为4个字符  t:table 表格的意思
"""

# print('124\t5')
# print('1234\t\t5')
# print('123456789')


row = 1
while row <= 5:

	col = 1
	while col <= row:  # row 这里是实现col < 5 中的5效果
		if row == 2:
			break  # 只会结束本次循环,不会结束外层循环
		print('*', end='')
		col += 1

	print()
	row += 1
