# 写文件
with open(r'F:\黑马Python21期基础班\Crack_Wifi\dict.txt','w') as file:

	# 循环生成6位数字密码
	# rangeList = [0, 1, 2, 3, 4, 5 ,6, 7, 8, 9]
	for i in range(10000):
		a = '1994'+str(i).zfill(4)
		# print(a)
		file.write(a + '\n')
		file.flush()

print('生成完成!')
