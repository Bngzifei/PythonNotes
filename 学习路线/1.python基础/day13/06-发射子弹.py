import pygame  # 动态模块.dll.pyd 静态模块:.py 静态的必须导入模块名.
import sys
from pygame.locals import *

"""
1.创建窗口
2.加载背景图片
3.贴图
4.刷新

子弹的y = 英雄飞机的y - 子弹的高度
子弹的x = 英雄飞机的x + 英雄飞机宽的一半 - 子弹宽的一半
"""


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
		self.y -= 5


class HeroPlane:
	"""英雄飞机类"""

	def __init__(self, img_path, x, y, window):
		self.img = pygame.image.load(img_path)  # 飞机图片
		self.x = x  # 记录飞机位置
		self.y = y
		self.window = window  # 将来飞机所在的窗口
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


def main():
	# 1.创建窗口
	window = pygame.display.set_mode((512, 768))
	# 2.加载背景图片
	bg_image = pygame.image.load('res/img_bg_level_1.jpg')
	# 2.1 创建英雄飞机实例对象
	hero_plane = HeroPlane('res/hero2.png', 196, 500, window)

	while True:
		# 3.把背景图片贴到窗口上
		window.blit(bg_image, (0, 0))
		# 3.1把飞机图贴到窗口上 重复贴
		hero_plane.display()
		# 2.遍历子弹列表取出每个子弹,让每一个子弹重复贴图
		for bullet in hero_plane.bullets:
			bullet.display()  # 重复贴子弹图
			bullet.move()
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


if __name__ == '__main__':
	main()
