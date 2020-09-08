"""
异常抛出的原理:

raise: 关键字 抛出 表示抛出指定的异常实例对象
raise 抛出异常的实例对象,然后except去拦截这个异常实例对象.
能不能拦截:是要看这个错误是不是这个错误的类创建的.

拦截:判断是不是同一个类造出来的,是,就把这个异常实例对象赋值给error.

先抛出来才能拦截.


自定义异常:不用解释器提供异常类.
1> 让异常信息是中文的,让用户也能看懂.更加人性化
2> 提前干预,还没有出错之前就来对问题进行处理.
3> 简化异常处理的流程,批量抛出,一次拦截.

注意:  自定义异常类必须继承Exception类,是为了使用raise的能力.否则会报错误.



"""


try:
	# print(a)
	error_instance = NameError("name 'a' is not define")  # 创建指定异常的实例对象
	print(id(error_instance))  # 2291212287760
	raise error_instance  # 抛出指定的异常实例对象


# except NameError as error:  # 里面写了各种错误类型,根据错误去找是什么样的错误类型.
# 	print('提示:%s' % error)  # 实际是一个NameError()类产生的一个实例对象.error实际就是一个错误类型的实例对象. 
# 	print(id(error))  # 2291212287760

# error = error_instance  ,实际对应关系.

class PhoneException(Exception):
	# 实际的
	# def __init__(self, name):
	# 	self.name = name
	#
	# def __str__(self):
	# 	# return 'xxxxxxxxxxxxxxxx'
	# 	return self.name
	pass


phone_num = input('手机号:')

try:
	if len(phone_num) != 11:
		# print('号码位数不对')
		raise PhoneException('手机号码位数不对')
	elif phone_num.isdecimal() is False:  # isdecimal():判断是不是数字,返回值是False或者是True
		# print('号码不是纯数字')
		raise PhoneException('手机号码不是纯数字')

except PhoneException as error:
	print(error)


var = 'df'.center(20,'*')  # 输出 : *********df*********
print(var)
