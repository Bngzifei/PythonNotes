"""
1-100 之间数字累加求和
1 + 2 + 3 .....+ 100
不能用数学公式做,使用循环
result = result + 1
result = result + 2
result = result + 3
result = result + 4
...
result = result + 100


重复有规律--->使用循环
"""
"""

i = 1
result = 0  # 用来记录结果,不能放到while循环体里面
while i <= 100:  # 循环执行了100遍,循环次数是:while i<= 100 条件的尾部值-初始值+1
	result += i
	i += 1
	print(result)  # 每次都输出结果
print('------------')
print(result)  # 只输出一次最后的结果

"""



"""
偶数相加: 优化代码,尽量减少计算机的运行步骤,比如初始值设为2,减少一次循环的步骤.不用if判断语句,直接进行数学意义的运算实现偶数的求和实现
2 ** 0.5 :开方运算
"""
i = 2
result = 0  # 用来记录结果,不能放到while循环体里面

while i <= 10:
	# if i % 2 == 0:
	# 	result += i
	result += i
	i += 2
	print(result)  # 每次都输出结果,一共循环了5次
print('------------')
print(result)  # 只输出一次最后的结果




