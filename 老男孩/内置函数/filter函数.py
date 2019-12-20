"""
要求:过滤掉sb
"""
movie_people = ['sb_alex', 'sb_wupeiqi', 'linhaifeng', 'sb_yuanhao', 'sb_yuanhao1', '李斌']
movie_people1 = ['11111sb_alex', '1sb_wupeiqi', 'linhaifeng', 'sb_yuanhao', 'sb_yuanhao1', '李斌']


def filter_test(list1):
	l1 = []
	for p in list1:
		if not p.startswith('sb'):
			l1.append(p)
	return l1


print(filter_test(movie_people))
# filter(参数1,参数2)函数: 参数1是功能函数名,第二个参数是可迭代数据类型
print(list(filter(lambda x: not x.startswith('sb'), movie_people)))

# movie_people1 = ['alex_sb', 'wupeiqi_sb', 'linhaifeng', 'yuanhao_sb', 'yuanhao1_sb', '李斌']
#
#
# # def sb_show(n):
# # 	return n.endswith('sb')  # 判断以sb结尾的字符串.返回真
#
#
# def filter_test(func, list1):
# 	l1 = []
# 	for p in list1:
# 		if not func(p):  # 注意:这里的func是用来专门处理p的,否则就没意思了.
# 			l1.append(p)
# 	return l1
#
#
# # print(filter_test(sb_show, movie_people1))
# # print(filter_test(lambda x: x.endswith('sb'), movie_people1))
#
# # filter(参数1,参数2)函数: 参数1是功能函数名,第二个参数是可迭代数据类型
#
# print(filter(lambda x: not x.endswith('sb'),
# 			 movie_people1))  # <filter object at 0x000002355BD48588> 是一个内存地址,已经保存了filter生成的数据
# print(list(filter(lambda x: not x.endswith('sb'),
# 				  movie_people1)))  # <filter object at 0x000002355BD48588> 是一个内存地址,已经保存了filter生成的数据
# # 千万记得这里 lambda x: not x.endswith('sb') 中 x.endswith('sb') 这部分是bool类型,所以只能在这里进行取反操作,其他地方肯定不行
