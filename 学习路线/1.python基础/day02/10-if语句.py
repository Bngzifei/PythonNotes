# # 整数可以转到小数,小数不可以转到整数
# # ValueError: invalid literal for int() with base 10:literal
# literal: 文字的,无夸张的
# # 英 ['lɪt(ə)r(ə)l]  美 ['lɪtərəl]
# # adj. 文字的；逐字的；无夸张的
# age = int(input('年龄:'))
#
# # if可以单独存在,但else必须依赖if的存在
# # 意思就是else出现时必须有if
# if age >= 18:  # if后为True才会执行
# 	print('可以进来玩玩')  # python中的代码是通过缩进的方式来控制是否是一个整体的代码块
# else:
# 	print('回家作业')  # 当if的条件返回False时就会执行
#
# 一旦出现if 意味着需要判断的最少是2中对立的情况,为了避免出现逻辑错误,最好写一个if,后面就紧跟一个else,不管有没有用.等到最后了再去决定是否采用else

5
# age = int(input())  # 这里进行int类型转换之后,如果age是0,输出不成立,否则就输出成立
age = input()  # 如果这里什么也不输入,输出 不成立.如果随便输入一个字符(包括空格键) ,则输出成立.因为input()默认输入的数据均是字符串,所以可以用来判断输入的内容是否是空的.(即啥也没输入就输出不成立)
if age:  # 可以直接进行数值判定,非零和零的区别
	print('成立')
else:
	print('不成立')