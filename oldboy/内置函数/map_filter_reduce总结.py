"""

map()处理序列中的每个元素,得到的结果是一个'列表',该列表中元素个数和位置与原来一样
序列:可迭代的数据类型(能使用for循环遍历的就是)

filter():遍历序列中的每个元素,判断每个元素,得到一个布尔值,如果是true,则留下来,最终结果是一个列表(迭代器)

reduce():处理一个序列,把序列进行合并操作


"""

people = [
	{'name': 'alex', 'age': 1000},
	{'name': 'alex1', 'age': 10000},
	{'name': 'alex11', 'age': 100000},
	{'name': 'alex111', 'age': 10}

]

print(list(filter(lambda x: x['age'] < 15, people)))
print(filter(lambda x: x['age'] < 15, people))
print(list(enumerate(['1', '9', '3'])))
