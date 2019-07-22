import pygame  # 动态模块.dll.pyd 静态模块:.py 静态的必须导入模块名.动态的只需要导入包名就行
import sys
from pygame.locals import *
import time
import random

"""
1.创建窗口
2.加载背景图片
3.把背景图片贴到窗口上
4.刷新窗口

Python 中没有常量,只是模拟常量了.
事件监测:监听事件操作,产生相应的效果.是否监听到并处理
vs.code:记得装一下.
"""


# 坐标都是元组
# 因为英雄飞机,敌人飞机都一样,所以创建父类让这两个类去继承

class BaseFlight:
	def __init__(self, img_path, x, y, window):
		self.img = pygame.image.load(img_path)
		self.x = x
		self.y = y
		self.window = window

	def display(self):
		self.window.blit(self.img, (self.x, self.y))


class HeroBullet:
	"""英雄子弹类"""

	def __init__(self, img_path, x, y, window):
		self.img = pygame.image.load(img_path)
		self.x = x
		self.y = y
		self.window = window

	def display(self):
		self.window.blit(self.img, (self.x, self.y))

	def move(self):
		"""英雄的子弹向上飞"""
		self.y -= 25


class HeroFlight(BaseFlight):
	"""英雄飞机类"""

	def __init__(self, img_path, x, y, window):
		super().__init__(img_path, x, y, window)  # 注意这里的参数
		self.bullets = []  # 来记录该飞机发出的子弹

	def display_bullets(self):
		"""贴子弹的图"""
		delete_bullets = []

		for bullet in self.bullets:
			# 判断子弹是否超出上边界
			if bullet.y > -31:
				bullet.display()  # 调用子弹的display()方法
				bullet.move()  # 调用子弹的move()方法
			else:
				delete_bullets.append(bullet)  # 回收外面的子弹

		for out_window_bullet in delete_bullets:
			self.bullets.remove(out_window_bullet)  # 销毁屏幕外面的子弹

	def mov_left(self):
		"""左飞"""
		self.x -= 5

	def mov_right(self):
		"""右飞"""
		self.x += 5

	def mov_up(self):
		"""上"""
		self.y -= 5

	def mov_down(self):
		"""下"""
		self.y += 5

	def fire(self):
		"""发射子弹"""

		# 先要使用子弹类来创建子弹对象
		bullet = HeroBullet("res/bullet_9.png", self.x + 60 - 10, self.y - 31, self.window)

		# 显示子弹
		bullet.display()
		self.bullets.append(bullet)


class EnemyFlight(BaseFlight):
	"""敌人飞机类"""

	def mov_down(self):
		"""敌机移动"""
		self.y += 10  # 敌机肯定是先移动位置后进行坐标判断.
		if self.y >= 768:  # 判断敌机是否飞到外面,飞到外面的就回到界面顶部的随机位置
			self.x = random.randint(0, random.randint(0, 512 - 100))
			self.y = 0  # 回到顶部


def main():
	pygame.init()

	# 1.创建窗口
	window = pygame.display.set_mode((512, 768))
	# 2.加载背景图片
	bg_image = pygame.image.load('res/img_bg_level_1.jpg')

	# 2.1 创建英雄飞机对象
	hero_flight = HeroFlight("res/hero2.png", 240, 500, window)

	# 2.2 创建敌机对象,在飞机界面顶部随机位置产生敌人的飞机
	enemy_flight = EnemyFlight("res/img-plane_5.png", random.randint(0, 512 - 100), 0, window)

	while True:
		# 3.把背景图片贴到窗口上
		window.blit(bg_image, (0, 0))
		# 3.1 把飞机贴到窗口上
		hero_flight.display()
		# 3.2 把飞机的子弹贴到窗口上
		hero_flight.display_bullets()
		# 3.3 把敌机贴到窗口上
		enemy_flight.display()
		# 3.4 让敌机移动
		enemy_flight.mov_down()

		# 4.刷新窗口
		pygame.display.update()

		# 获取事件
		for event in pygame.event.get():
			# 1. 鼠标点击关闭窗口事件
			if event.type == QUIT:  # 判断是不是退出程序
				print("点击关闭窗口按钮")
				sys.exit()  # 关闭程序


			# 2. 键盘按下事件
			elif event.type == KEYDOWN:
				# 判断用户按键
				if event.key == K_SPACE:
					# hero_flight.fire()
					pass

		# 获取连续按下的事件
		pressed_keys = pygame.key.get_pressed()

		if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
			hero_flight.fire()
			hero_flight.mov_left()

		if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
			hero_flight.fire()
			hero_flight.mov_right()

		if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
			hero_flight.fire()
			hero_flight.mov_up()

		if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
			hero_flight.fire()
			hero_flight.mov_down()

		# 每次循环都让程序休眠一会儿
		time.sleep(0.01)


# 编写测试情况下的代码,判断是否是主动执行这个文件
if __name__ == '__main__':
	main()
