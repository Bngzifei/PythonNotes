"""给函数添加验证功能:不能修改函数内部代码,不能修改函数的调用方式"""


def auth_func(func):
	def wrapper(*args, **kwargs):
		username = input('用户名:').strip()  # strip(): 去除字符串两边的空格,避免用户输入空格符之后,程序将空格符当做用户名的一部分(ps:没有谁会把空格符当做用户名,但是会误触空格键)
		password = input('密 码:').strip()
		if username == 'sb' and password == '123':
			res = func(*args, **kwargs)
			return res  # 执行完了就返回
		else:
			print('用户名/密码错误')

	return wrapper


@auth_func
def index():
	print('欢迎来到京东主页')


@auth_func
def home(name):
	print('欢迎回家:', name)


@auth_func
def shopping_car(name):
	print('%s购物车有[%s,%s,%s]' % (name, '奶茶', '妹妹', '娃娃'))


index()
home('产品经理')
shopping_car('产品经理')
