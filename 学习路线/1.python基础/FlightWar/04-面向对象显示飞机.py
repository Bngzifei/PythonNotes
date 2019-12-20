import pygame  # 动态模块.dll.pyd 静态模块:.py 静态的必须导入模块名.动态的只需要导入包名就行
import sys
from pygame.locals import *

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






# 飞机位置坐标
# x = 256
# y = 384

class HeroFlight:
	def __init__(self, img_path, x, y, window):
		self.img = pygame.image.load(img_path)
		self.x = x
		self.y = y
		self.window = window  # 加载飞机图片也需要窗口

	def display(self):
		"""贴图"""
		# 3.1 把飞机图贴到窗口上
		self.window.blit(self.img, (self.x, self.y))

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


def main():
	pygame.init()

	# 1.创建窗口
	window = pygame.display.set_mode((512, 768))
	# 2.加载背景图片
	bg_image = pygame.image.load('res/img_bg_level_1.jpg')

	# 2.1 创建英雄飞机对象
	hero_flight = HeroFlight("res/hero.png", 256, 384, window)

	while True:
		# 3.把背景图片贴到窗口上
		window.blit(bg_image, (0, 0))
		# 3.1 把飞机贴到窗口上
		hero_flight.display()
		# 4.刷新窗口
		pygame.display.update()

		# 获取新事件
		for event in pygame.event.get():
			# 1. 鼠标点击关闭窗口事件
			if event.type == QUIT:  # 判断是不是退出程序
				print("点击关闭窗口按钮")
				sys.exit()  # 关闭程序

			# 2. 键盘按下事件
			elif event.type == KEYDOWN:
				# 判断用户按键
				# if event.key == K_LEFT or event.key == K_a:
				# 	x -= 13
				# if event.key == K_RIGHT or event.key == K_d:
				# 	x += 13
				# if event.key == K_UP or event.key == K_w:
				# 	y -= 13
				# if event.key == K_DOWN or event.key == K_s:
				# 	y += 13
				if event.key == K_SPACE:
					print("space")

		# 获取连续按下的事件
		pressed_keys = pygame.key.get_pressed()

		if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
			hero_flight.x -= 25
		if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
			hero_flight.x += 25
		if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
			hero_flight.y -= 25
		if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
			hero_flight.y += 5


# 编写测试情况下的代码,判断是否是主动执行这个文件

if __name__ == '__main__':
	main()
