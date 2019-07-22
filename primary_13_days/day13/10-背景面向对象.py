import pygame  # 动态模块.dll.pyd 静态模块:.py 静态的必须导入模块名.
import sys
from pygame.locals import *
import time
import random

"""
1.创建窗口
2.加载背景图片
3.贴图
4.刷新

子弹的y = 英雄飞机的y - 子弹的高度
子弹的x = 英雄飞机的x + 英雄飞机宽的一半 - 子弹宽的一半
"""


class Map:
	"""地图类"""

	def __init__(self, img_path, x, y, window):
		self.img = pygame.image.load(img_path)  # 背景图片
		self.x = x  # 记录背景位置
		self.y = y
		self.window = window  # 将来背景所在的窗口

	def display(self):
		"""显示背景"""
		self.window.blit(self.img, (self.x, self.y))


class Bullet:
	"""子弹类"""

	def __init__(self, img_path, x, y, window):
		self.img = pygame.image.load(img_path)  # 子弹图片
		self.x = x  # 记录子弹位置
		self.y = y
		self.window = window  # 将来子弹所在的窗口

	def display(self):
		"""显示子弹"""
		self.window.blit(self.img, (self.x, self.y))

	def move(self):
		"""子弹移动"""
		print('bullet move up')
		self.y -= 10

	def __del__(self):
		"""验证子弹是否销毁"""
		print('子弹销毁了')


class BasePlane:
	"""飞机基类"""

	def __init__(self, img_path, x, y, window):
		self.img = pygame.image.load(img_path)  # 飞机图片
		self.x = x  # 记录飞机位置
		self.y = y
		self.window = window  # 将来飞机所在的窗口

	def display(self):
		"""显示飞机"""
		self.window.blit(self.img, (self.x, self.y))


class EnemyPlane(BasePlane):
	"""敌机类"""

	def move_down(self):
		"""敌机下移"""
		print('down')
		self.y += 5
		if self.y >= 768:
			self.y = random.randint(-300, -68)  # 也可以将y设置成随机的
			self.x = random.randint(0, 412)  # 设置成x位置随机
			self.img = pygame.image.load('res/img-plane_%d.png' % random.randint(1, 7))


class HeroPlane(BasePlane):
	"""英雄飞机类"""

	def __init__(self, img_path, x, y, window):
		super().__init__(img_path, x, y, window)
		self.bullets = []  # 保存所有子弹

	def display(self):
		"""显示英雄飞机"""
		self.window.blit(self.img, (self.x, self.y))

	def move_left(self):
		"""飞机左移"""
		print('left')
		self.x -= 5

	def move_right(self):
		"""飞机右移"""
		print('right')
		self.x += 5

	def fire(self):
		"""开火"""
		# 1.创建子弹对象
		print('----')
		bullet = Bullet('res/bullet_14.png', self.x + 50, self.y - 56, self.window)
		self.bullets.append(bullet)  # 添加到子弹列表

	def display_bullet(self):
		"""处理子弹的显示问题"""
		temp_list = []  # 记录要销毁的子弹
		for bullet in self.bullets:
			if bullet.y > -56:  # 没有飞出去,继续贴图
				bullet.display()  # 重复贴子弹图
				bullet.move()
			else:
				# self.bullets.remove(bullet)  # 飞出去销毁子弹
				temp_list.append(bullet)  # 把超出窗口的子弹回收
		for del_bullet in temp_list:  # 销毁子弹
			self.bullets.remove(del_bullet)


def main():
	# 1.创建窗口
	window = pygame.display.set_mode((512, 768))
	# 2.加载背景图片
	map1 = Map('res/img_bg_level_1.jpg', 0, 0, window)
	# 2.1 创建英雄飞机实例对象
	hero_plane = HeroPlane('res/hero2.png', 196, 500, window)
	# 创建敌机实例对象
	enemy_plane_list = []
	for i in range(5):
		enemy_plane = EnemyPlane('res/img-plane_%d.png' % random.randint(1, 5),
								 random.randint(0, 412), random.randint(-300, -68), window)
		enemy_plane_list.append(enemy_plane)

	while True:
		# 3.把背景图片贴到窗口上
		map1.display()
		# 3.1把飞机图贴到窗口上 重复贴
		hero_plane.display()
		# 调用子弹显示方法
		hero_plane.display_bullet()
		# 3.3 贴敌机图
		for enemy_plane in enemy_plane_list:
			enemy_plane.display()
			enemy_plane.move_down()
		# 4.刷新窗口,不刷没法显示以上效果
		pygame.display.update()

		# 获取新事件
		for event in pygame.event.get():
			# 1. 鼠标点击关闭窗口事件
			if event.type == QUIT:  # 判断是不是退出
				print("点击关闭窗口按钮")
				sys.exit()  # 关闭程序

			# 2. 键盘按下事件  # 只是一个单按事件,单击事件
			if event.type == KEYDOWN:
				# 判断用户按键
				if event.key == K_SPACE:
					print("space")
					hero_plane.fire()  # 这里只会贴一次

		# 键盘长按事件
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
			hero_plane.fire()
			hero_plane.move_left()
		if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
			hero_plane.fire()
			hero_plane.move_right()

		time.sleep(0.02)  # 执行到这里的时候,程序会暂停0.02秒,为了让cpu缓一缓 提高效率cpu.


if __name__ == '__main__':
	main()
