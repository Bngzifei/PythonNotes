from django.db import models

class BaseModel(models.Model):
	"""为模型类补充字段:"""
	create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
	update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')

	class Meta:
		abstract = True  # 表示这是一个抽象类.只用于继承,数据库迁移建表的时候不创建BaseModel的表
