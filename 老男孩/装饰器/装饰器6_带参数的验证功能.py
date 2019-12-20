# 用户信息列表  但是这样就又写死了,一般情况下都是把这些数据放到数据库或者文件中(数据库也是文件的一种形式)
# 所以,新建一个 filedb的文件来存储用户信息,一行就是一条用户信息.
user_list = [
	{'name':'alex0','passwd':'123'},
	{'name':'alex1','passwd':'1234'},
	{'name':'alex2','passwd':'12345'},
	{'name':'alex3','passwd':'123456'},
]


# 保存用户名和登录状态的全局变量
current_user_dict = {'username': None, 'login': False}


def auth(auth_type='filedb'):
	def auth_func(func):
		def wrapper(*args, **kwargs):
			print('认证类型是:',auth_type)
			if auth_type == 'filedb':
				# 登录之前就要判断
				if current_user_dict['username'] and current_user_dict['login']:
					res = func(*args, **kwargs)
					return res  # 执行完了就返回
				# 不满足的情况下执行下面
				username = input('用户名:').strip()  # strip(): 去除字符串两边的空格
				password = input('密 码:').strip()

				# 这里就应该是使用循环去遍历user_list,查看登录的用户是否在那个列表中
				for user_dict in user_list:
					if user_dict['name'] == username and user_dict['passwd'] == password:
						current_user_dict['username'] = username
						current_user_dict['login'] = True
						res = func(*args, **kwargs)
						return res  # 执行完了就返回
					# 放到这里,就是第一次循环去找,找不到的情况下就输出else的语句,逻辑错误,应该是找完了列表之后,才最终输出找不到,不应该是找一次没找到就输出else
					# else:
					# 	print('用户名或密码错误')
				# 放到这里,表示for循环结束,所有的列表元素都找完了,但是没找到的情况,这样就符合逻辑了.最后没找到才输出else的语句.
				else:
					print('用户名/密码错误,请重新输入')
			elif auth_type == 'ldap':
				print('鬼才会玩')
				res = func(*args, **kwargs)
				return res  # 执行完了就返回
			else:
				print('鬼才知道你用的什么认证方式')
				res = func(*args, **kwargs)
				return res  # 执行完了就返回
		return wrapper
	return auth_func


# 给已经写好的装饰器加参数(目的是为了让用户自己选择验证的类型,意思就是从数据库进行验证还是从文件进行验证)
# auth_func = auth(auth_type = 'filedb') --> @auth_func  附加了一个auth_type形参 ---> index=auth_func(index)
@auth(auth_type='filedb')
def index():
	print('欢迎来到京东主页')


@auth(auth_type='ldap')
def home(name):
	print('欢迎回家:', name)


@auth(auth_type='sssssssssssss')
def shopping_car(name):
	print('%s购物车有[%s,%s,%s]' % (name, '奶茶', '妹妹', '娃娃'))

# print('before--->',current_user_dict)
# index()
# print('after--->',current_user_dict)
# home('产品经理')
shopping_car('产品经理')
