"""
# eval() 转换为数值,这种按住ctrl键后鼠标左键点击进入后的函数均显示builtins.py的形式,表示这是一个Python内置函数 函数是公共的,方法私有的,是一个面向对象的私有的概念.要区分清楚 .
"""
price = eval(input('请输入单价:'))
weight = eval(input('请输入重量:'))

# price_str = input('请输入单价:')
# weight_str = input('请输入重量:')

# price = float(price_str)  # 把字符串转换成浮点类型
# weight = float(weight_str)  # 类型转换时,本尊是不变的,只是生成一个新的数据
# print(type(price))
# print(type(price_str))
money = price * weight

# print(moneny)   print() 可以先写money,再写点 .,  Pycharm会自动出现提示,然后写成上述模样.只有print()这个函数有这个功能.
# print(money)

print('总价为:%.2f' % money)



