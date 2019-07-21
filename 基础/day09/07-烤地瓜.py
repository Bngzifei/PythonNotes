"""烤地瓜:"""


# 会给原型图,效果图

# 会给写网页,项目的开发文档(类似操作指南,具体开发过程)

# 不建议先去大公司,分工细,接触的东西少,学到的东西少.刚刚毕业要眼光长远,首要任务是提升技术.能学到东西为先.学不到东西了就得换一家了

# 看到对象,心中有类

# class SweetPotato:
# 属性:
# state = '生的'
# cooked_time = 0  #烧烤总时间
# 方法:
# cook(self,time) 烧烤
# str 对象的自定义输出  只是在我们这里用,实际开发不会有str()方法

class SweetPotato:
	"""地瓜类"""

	def __init__(self):
		self.state = '生的'
		self.cooked_time = 0

	def cook(self, time):
		"""烧烤方法"""
		self.cooked_time += time  # 累加烧烤总时间
		if self.cooked_time >= 0 and self.cooked_time < 3:
			self.state = '生的'
		elif self.cooked_time >= 3 and self.cooked_time < 6:
			self.state = '半生不熟'
		elif self.cooked_time >= 6 and self.cooked_time < 8:
			self.state = '熟了'
		else:
			self.state = '有毒'

	def __str__(self):
		return '地瓜状态为:%s,总时间为:%d' % (self.state, self.cooked_time)


dg1 = SweetPotato()
dg1.cook(2)
print(dg1)

dg2 = SweetPotato()
dg2.cook(6)
print(dg2)