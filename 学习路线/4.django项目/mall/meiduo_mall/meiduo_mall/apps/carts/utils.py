import pickle
import base64
from django_redis import get_redis_connection


# qq两个地方,user一个地方都需要进行合并,所以在这里工具包里面进行一个合并的函数,
# 方便大家都可以调用
# 别人调的时候传一个request参数
def merge_cart_cookie_to_redis(request, response, user):  # 注意这里的形参的位置需要和qq登录那里调用的实参位置要一致
	"""
	登录时购物车的cookie合并到redis
	合并请求用户的购物车数据，将未登录保存在cookie里的保存到redis中,
	遇到cookie与redis中出现相同的商品时候,以cookie为主,覆盖redis中的数据
	:param request: 用户的请求对象
	:param user: 当前的登录用户
	:param response: 响应对象,用于清除购物车cookie
	:return: None
	"""

	# 1.取出cookie中购物车的数据
	cookie_cart_str = request.COOKIES.get('cart')
	if not cookie_cart_str:  # 这一条必须加,因为如果用户清除了cookie,那么程序不应该奔溃.还应该是可以顺利运行的
		return response

	# 将cookie中的购物车字符串转成字典
	cookie_cart_dict = pickle.loads(base64.b64decode(cookie_cart_str.encode()))  # 可能是{} 或者''这样的,
	# cookie中没有数据就响应结果
	# if not cookie_cart_str:  # 如果cookie中没有购物车数据,直接返回
	# 	return response
	if not len(cookie_cart_dict.keys()):  # 如果cookie中没有购物车数据,直接返回.在这里进行判断就有点晚了,因为在qq登录的时候,那边最开始是from ... import 这个函数,会先运行这个函数,那么就会奔溃报错
		return response
	"""
	redis_dict:

	{sku_1:1,sku_2:2}


	cookie_dict{
		sku_1:{
			'count':1,
			'selected':True
			},
		sku_2:{
			'count':1,
			'selected':True
			}


	}
	"""

	# 2.获取redis中的购物车数据
	redis_conn = get_redis_connection('cart')

	redis_cart_dict = redis_conn.hgetall('cart_%s' % user.id)
	"""
	这里不可以使用request.user,因为是在登录的时候调用,
	那个时候request对象里面是没有用户这个值的.
	所以在request里面就是一个匿名用户.就是空的
	"""

	# 是否勾选的set集合
	redis_cart_selected = redis_conn.smembers('selected_%s' % user.id)

	# 先新包一个字典,等下存进来.将来存储到redis中的购物车数据.
	# 这个字典是在内存中.程序运行到这里的时候才会被创建.
	new_redis_cart_dict = {}

	"""
	必须先把redis中的购物车数据加入到new_redis_cart_dict,
	如果后面的cookie购物车中有redis购物车中相同的商品,
	就可以用cookie购物车的商品数据覆盖掉redis购物车中的商品数据.
	这样就实现了以用户cookie购物车数据为基准的设计原则.
	因为cookie中的数据才是用户最新,最真实的购物数据.在有相同选择的商品的情况下,
	必须以cookie中的数据为准
	"""
	# 以下两个for循环是合并的核心代码

	# redis的哈希字典中的值都是bytes,需要转换成int
	for sku_id, count in redis_cart_dict.items():
		new_redis_cart_dict[int(sku_id)] = int(count)  # 注意数据类型转换

	# 遍历cookie_cart_dict,将sku_id和count覆盖到new_redis_cart_dict
	# cookie字典数据向redis哈希字典靠拢
	for sku_id, cookie_dict in cookie_cart_dict.items():
		new_redis_cart_dict[sku_id] = cookie_dict.get('count')

		# 把勾选的商品sku_id
		if cookie_dict['selected']:
			"""如果当前cookie中当前这件的商品的状态是勾选,
			就把此商品的sku_id添加到redis中的集合中"""
			# set.add(元素)  给无序集合添加新元素
			# 勾选状态这里没有覆盖,全部是以勾选为准.这里就是redis中已勾选,cookie中没勾选,
			# 那就以redis中有勾选为基准
			redis_cart_selected.add(sku_id)

	# 将redis_cart_dict写入到数据库中  pl的使用是在设置的时候常用
	pl = redis_conn.pipeline()
	# 把合并好的商品字典数据合并到redis哈希里面
	pl.hmset('cart_%s' % user.id, new_redis_cart_dict)
	# 把合并好的商品字典数据合并到redis的set里面
	pl.sadd('selected_%s' % user.id, *redis_cart_selected)
	# 执行管道
	pl.execute()

	# 拿response就是为了合并之后把cookie删除
	response.delete_cookie('cart')
	# 抛出去,让别人把删除了cookie的response执行下去.响应结果
	return response

# ------------------------老师的:---------------------------------
# import pickle, base64
# from django_redis import get_redis_connection
#
# def merge_cart_cookie_to_redis(request, user, response):
# 	"""登录时购物车的cookie合并到redis"""
#
#
# 	# 获取cookie中的购物车数据
# 	cookie_cart_str = request.COOKIES.get('cart')
# 	if not cookie_cart_str:  #  这一条必须加,因为如果用户清除了cookie,那么程序不应该奔溃.还应该是可以顺利运行的
# 		return response
# 	cookie_cart_dict = pickle.loads(base64.b64decode(cookie_cart_str.encode()))
# 	if not len(cookie_cart_dict.keys()):  # 如果cookie中没有购物车数据直接返回,不要执行下面的合并代码
# 		return response
#
# 	# 获取redis中的购物车数据
# 	redis_conn = get_redis_connection('cart')
# 	redis_cart_dict = redis_conn.hgetall('cart_%s' % user.id)
# 	redis_selecteds = redis_conn.smembers('selected_%s' % user.id)  # 取原本redis中所有商品勾选状态
#
# 	"""
# 	redis_dict
# 	{sku_1: 1, sku_2: 2}
#
#
# 	cookie_dict
# 	{
# 		sku_1: {
# 			'count': 1
# 			'selected': True
# 		},
# 		sku_1: {
# 			'count': 2
# 			'selected': True
# 		}
# 	}
# 	"""
# 	# 以下两个for循环就是合并的核心代码
# 	new_redis_cart_dict = {}  # 将来要重新存入到redis中的购物车商品数据
# 	# 必须先对redis数据进行加入到new_redis_cart_dict 目的就是如果后续cookie中有相同商品,可以用cookie数据赋值redis数据
# 	for sku_id, count in redis_cart_dict.items():
# 		new_redis_cart_dict[int(sku_id)] = int(count)  # 注意数据类型转换问题
#
# 	for sku_id, cookie_dict in cookie_cart_dict.items():  # 将cookie字典数据向redis 哈希中字典格式靠拢
# 		new_redis_cart_dict[sku_id] = cookie_dict['count']
#
# 		if cookie_dict['selected']:
# 			# 如果当前cookie中当前这件商品状态是勾选,那么就把此商品的sku_id添加到redis set集合
# 			# set.add(元素) 给无序集合添加新元素
# 			redis_selecteds.add(sku_id)
#
# 	pl = redis_conn.pipeline()
# 	# 把合并好的商品字典存储到redis的哈希里面
# 	pl.hmset('cart_%s' % user.id, new_redis_cart_dict)
# 	# 把商品勾选状态存入redis的set中
# 	pl.sadd('selected_%s' % user.id, *redis_selecteds)
# 	# 执行管道
# 	pl.execute()
#
# 	# 为了合并之后删除cookie数据
# 	response.delete_cookie('cart')
# 	return response
