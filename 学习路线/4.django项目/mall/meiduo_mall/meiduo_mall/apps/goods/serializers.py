from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer
from goods.search_indexes import SKUIndex

from .models import SKU, GoodsChannel, GoodsCategory


class SKUSerializer(serializers.ModelSerializer):
	"""商品列表的序列化器:输出"""

	class Meta:
		model = SKU
		# 输出:序列化的字段
		fields = ['id', 'name', 'price', 'default_image_url', 'comments']


class SKUIndexSerializer(HaystackSerializer):
	"""
	SKU索引结果数据序列化器
	"""
	# 关联序列化器
	object = SKUSerializer(read_only=True)

	class Meta:
		index_classes = [SKUIndex]
		fields = ('text', 'object')


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = GoodsCategory
		fields = '__all__'


class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = GoodsChannel
		fields = '__all__'
