# 烤地瓜应用智能版

"""
cook() 把地瓜烤一段时间
addCondiments()给地瓜添加配料
__init__():设置默认属性
__str__():让print()方法的结果看起来更好一些

auto_addCondiments():自动随机添加一种配料
auto_cook():自动烤地瓜,当地瓜烤熟了,自动停止


"""

import random


# 定义地瓜类
class SweetPotato:
	"""地瓜类"""

	# 定义初始化方法
	def __init__(self):
		self.cooked_level = 0
		self.cooked_string = "生的"
		self.condiments = []

	# 输出返回值str()方法
	def __str__(self):
		msg = self.cooked_string + '地瓜'
		if len(self.condiments) > 0:
			msg = msg + '('
			for temp in self.condiments:
				msg = msg + temp + ','
			msg = msg.strip(',')
			msg = msg + ')'

		return msg

	# 烤地瓜方法
	def cook(self, time):
		self.cooked_level += time
		if self.cooked_level > 8:
			self.cooked_string = '吃个碳球,都灰了:'
		elif 6 < self.cooked_level <= 8:
			self.cooked_string = '烤熟,好了:'
		elif 4 < self.cooked_level <= 6:
			self.cooked_string = '还有点生:'
		elif 2 < self.cooked_level <= 4:
			self.cooked_string = '半生不熟:'
		else:
			self.cooked_string = '生的:'

	# 添加[配料
	def addCondiments(self, condiments=['番茄酱', '辣椒酱,''蒜蓉', '醋', '香油']):
		index = random.randint(0, len(condiments) - 1)
		self.condiments.append(condiments[index])

	def auto_cook(self, timestep=1):
		cmd = input('请问您要几分熟(7-10):')
		while True:
			self.cook(timestep)
			# 添加佐料
			if self.cooked_level >= 4 and len(self.condiments) == 0:
				self.addCondiments()
			if cmd == '7' and self.cooked_level == 4:
				print('7分熟:', self)
				break
			elif cmd == '8' and self.cooked_level == 5:
				print('8分熟:', self)
				break
			elif cmd == '9' and self.cooked_level == 6:
				print('9分熟:', self)
				break
			elif cmd == '10' and self.cooked_level == 7:
				print('10分熟:', self)
				break
			elif self.cooked_level == 8:
				print('完全熟了:', self)
				break


digua = SweetPotato()
digua.auto_cook()
