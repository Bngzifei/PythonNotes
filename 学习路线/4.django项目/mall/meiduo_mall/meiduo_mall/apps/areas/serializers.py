from rest_framework import serializers
from .models import Area

# class AreaSerializer(serializers.Serializer):
# 注意:这里如果是Serializer,那么就需要自己手动的指定序列化操作的字段
# ModelSerializer:换成这个,在执行程序的时候会自动去映射models中的相关字段
class AreaSerializer(serializers.ModelSerializer):
	"""序列化省级数据"""
	class Meta:
		model = Area
		fields = ['id','name']



class SubAreaSerializer(serializers.ModelSerializer):
	"""序列化市/区级数据"""

	# 关联序列化器:这里就是关联所有
	subs = AreaSerializer(many=True,read_only=True)

	class Meta:
		model = Area
		fields = ['id','name','subs']