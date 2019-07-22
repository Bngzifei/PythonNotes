print()  # 查看注释:光标放到该函数上面,win:ctrl + q  mac:ctrl+j 查看文本注释

"""函数的文档注释"""

"""
作用:增加代码的可读性
win: ctrl + q
mac: 
ctrl + 点击函数:进入函数
"""


def func_sum():
	"""此函数是一个求和函数"""  # 只能在第一行 且是多行注释(就是三对双引号)的形式
	result = 1 + 2
	print(result)


func_sum()
