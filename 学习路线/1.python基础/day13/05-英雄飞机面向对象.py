import pygame  # 动态模块.dll.pyd 静态模块:.py 静态的必须导入模块名.
import sys
from pygame.locals import *

"""
1.创建窗口
2.加载背景图片
"""


class HeroPlane:
	"""英雄飞机类"""

	def __init__(self, img_path, x, y, window):
		self.img = pygame.image.load(img_path)  # 飞机图片
		self.x = x  # 记录飞机位置
		self.y = y
		self.window = window  # 将来飞机所在的窗口

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
		# 4.刷新窗口,不刷没法显示以上效果
		pygame.display.update()

		# 获取事件
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
		# 键盘长按事件
		pressed_keys = pygame.key.get_pressed()
		# print(pressed_keys)  # 是一个元组类型
		# 获取当前键盘所有按键的状态(按下/没有按下),返回bool元组(0,0,0,1,0,0,0)
		# 通过索引去取对应键的值,默认都是0,0代表没按下,1表示按下.去找对应位置的为1的那个.
		if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
			hero_plane.move_left()
		if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
			hero_plane.move_right()


if __name__ == '__main__':
	main()
