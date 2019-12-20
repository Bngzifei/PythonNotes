class GoodsItem:
	"""商品类"""
	def __init__(self, name, price, comments):
		self._name = name
		self._price = price
		self._comments = comments

	@property
	def name(self):
		"""name方法"""
		return self._name

	@property
	def price(self):
		"""price方法"""
		return self._price

	@property
	def comments(self):
		"""comments方法"""
		return self._comments

	@name.setter
	def name(self, name):
		self._name = name
		return self._name

	@price.setter
	def price(self, price):
		self._price = price
		return self._price

	@comments.setter
	def comments(self, comments):
		self._comments = comments
		return self._comments

	@comments.deleter
	def comments(self):
		print('正在删除评论...')
		del self._comments

	@comments.getter
	def comments(self):
		print('正在获取评论...')
		return self._comments


goods = GoodsItem('橘子', 15.2, '真的很好吃')
import pdb;pdb.set_trace
print('商品名:', goods.name)
print('价格:', goods.price)
print('客户评价:', goods.comments)

# ------------------------------->
goods.name = '柚子'
print('商品名:', goods.name)
goods.comments = '有点酸'
print('客户评价:', goods.comments)
del goods.comments
goods.price = 98.9
print('价格:', goods.price)
