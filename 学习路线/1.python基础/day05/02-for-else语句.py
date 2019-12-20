list1 = ["zhansan", "lisi1", 'ww']
# for name in list1:  # 运行2次,出现逻辑错误
# 	if name == 'lisi':
# 		print('找到')
# 	else:
# 		print("没有找到")

"""当for执行完成后,默认for后面的else都会执行一次,如果不想让for后面的else执行,在for里面写个break"""
for name in list1:  # 批量查找数据 if ... in...(判断有没有,True或False) 判断有没有我要的那个并返回(因为后续要用这个返回的)用for(break) else (判断有没有我要的那个)
	if name == 'lisi':
		print('找到')
	break
else:
	print('没找到')


# for ...else ... 是一个循环体内的.用于批量查找并返回一次提示信息
