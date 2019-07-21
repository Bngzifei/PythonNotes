# dict1 = {
# 	'北京': {
# 		'昌平': {
# 			'回龙观': 1
# 		}
# 	},
#
# 	'上海': {
# 		'宝山': {
# 			'虹口': 2
# 		}
# 	}
# }

d1 = {}
list1 = []


while True:

	choice = input('输入c继续,输入q退出:')
	if choice == 'c':
		name = input('输入省级地名>>>:')
		d1[name] = {}  # 设置省级地名为key
		# print(d1)
		list1.append(d1)  # list1列表来保存字典
		# print(list1)
		temp = []  # 保存将要被删除的item
		# print(list1)
		for item in list1:
			name1 = input('输入%s的下一级地名:>>>' % name)
			name2 = input('输入%s的下一级地名:>>>' % name1)
			name3 = input('输入%s的下一级地名:>>>' % name2)
			temp.append(item)  # 将遍历完的item放到temp列表中
			item[name] = {}  # 给item[name]的下一级再次赋值{},二次字典
			item[name][name1] = {}
			item[name][name1][name2] = name3
		# print(list1)
		for item1 in temp:  # 逐一删除temp里面的item,即把遍历过的item删除
			list1.remove(item1)  # 记住,这里是list1原来的表中删除,不是在temp表里面删除
		# print(list1)
	elif choice == 'q':
		print(d1)
		break
	else:
		print('输入字符不合法,请重新输入')

# db = {}
# path = []
#
# while True:
# 	temp = db
# 	for item in path:
# 		temp = temp[item]
# 	print('当前节点的所有子节点:', list(temp.keys()), '\n')
#
# 	choice = input('1:添加节点;2:查看节点(Q退出/返回上一级B) \n>>>')
#
# 	if choice == '1':
# 		k = input('请输入要添加的子节点名称:')
# 		if k in temp:
# 			print('节点已添加')
# 		else:
# 			temp[k] = {}
#
# 	elif choice == '2':
# 		k = input('请输入要查看的子节点名称:')
# 		if k in temp:
# 			path.append(k)
# 		else:
# 			print('子节点名称错误')
# 	elif choice == 'b':
# 		if path:
# 			path.pop()
# 	elif choice.lower() == 'q':
# 		break
# 	else:
# 		print('输入数据不合法')

# str = '二'
# v1 = str.isnumeric()
# v2 = str.capitalize()
# v3 = str.isdigit()
# v4 = str.expandtabs()
# print(v1)
# print(v2)
# print(v3)
# print(v4)
