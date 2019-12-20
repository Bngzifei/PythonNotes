from rest_framework import serializers
from goods.models import SKU


# 视图序列化器命名参照models模型.不能随意命名

# 4.购物车全选
class CartSelectAllSerializer(serializers.Serializer):
	"""购物车是否全选"""
	selected = serializers.BooleanField(label='全选')  # 不能给默认值了.也不需要单个校验了





# 3.删除购物车
class CartDeleteSerializer(serializers.Serializer):
	"""删除购物车数据序列化器"""

	# 定义字段
	sku_id = serializers.IntegerField(label='商品id', min_value=1)

	# 数据校验
	def validate_sku_id(self, value):
		try:
			sku = SKU.objects.get(id=value)  # 注意这里的写法.直接就是id=value
		except SKU.DoesNotExist:
			raise serializers.ValidationError('商品不存在')

		return value


# 2.输出商品模型.查询购物车
class CartSKUSerializer(serializers.ModelSerializer):
	"""序列化输出商品模型"""
	count = serializers.IntegerField(label='商品数量') # 序列化的时候,不需要这些最小值,默认值了.因为不是存储
	selected = serializers.BooleanField(label='是否勾选')
	class Meta:
		model = SKU
		fields = ['id', 'name', 'count', 'price', 'default_image_url', 'selected']



# 1.保存/修改的购物车的序列化器
class CartSerializer(serializers.Serializer):
	"""保存/修改的购物车的序列化器"""
	# label:是给调用接口的人看的
	sku_id = serializers.IntegerField(label='商品ID', min_value=1)
	count = serializers.IntegerField(label='商品数量', min_value=1)
	selected = serializers.BooleanField(label='是否勾选', default=True)

	def validate_sku_id(self, attrs):
		"""对sku_id进行额外的校验:格式就是validate_需要校验的字段"""
		try:
			SKU.objects.get(id=attrs)  # 注意这里的id=attrs.
		except SKU.DoesNotExist:
			raise serializers.ValidationError('sku_id不存在')
		return attrs

	# 写法2:
	# def validate(self, attrs):
	# 	"""对sku_id进行额外的校验"""
	# 	try:
	# 		SKU.objects.get(id=attrs.get('sku_id'))
	# 	except SKU.DoesNotExist:
	# 		raise serializers.ValidationError('sku_id不存在')
	# 	return attrs