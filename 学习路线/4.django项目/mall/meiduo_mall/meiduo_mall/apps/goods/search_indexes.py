from haystack import indexes

from .models import SKU


class SKUIndex(indexes.SearchIndex, indexes.Indexable):
	"""
	SKU索引数据模型类:类似于模型.通过哪个模型建立索引
	"""
	# text限定了搜索的时候的url的关键字  就类似于百度搜索时候的wd参数
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		"""返回建立索引的模型类"""
		return SKU

	def index_queryset(self, using=None):
		"""返回要建立索引的数据查询集"""
		return self.get_model().objects.filter(is_launched=True)  # 上架商品




"""
其中text字段我们声明为document=True，表名该字段是主要进行关键字查询的字段，
该字段的索引值可以由多个数据库模型类字段组成，具体由哪些模型类字段组成，
我们用use_template=True表示后续通过模板来指明。
"""