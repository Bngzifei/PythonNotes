# elif 一般有超过两种及两种以上的执行结果时,需要使用elif
# 在一个条件语句中,必须要有if ,且if只能有一个,elif可以有一个或多个,但其依赖于if,多个elif,1个else
# elif 在if 和 else的中间
holiday_name = input('节日名称:')

if holiday_name == '情人节':
	print('玫瑰')
elif holiday_name == '平安夜':
	print('苹果')
elif holiday_name == '生日':
	print('蛋糕')
else:
	print('狗粮')


print('---完成---')
