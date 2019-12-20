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

# 1.创建窗口
window = pygame.display.set_mode((512, 768))

# 2.加载背景图片
bg_image = pygame.image.load('res/img_bg_level_1.jpg')
# 2.1 加载英雄飞机图片
hero_flight_img = pygame.image.load('res/hero.png')

while True:
	# 3.把背景图片贴到窗口上
	window.blit(bg_image, (0, 0))
	# 3.1 把飞机图贴到窗口上
	window.blit(hero_flight_img, (256, 384))
	# 4.刷新窗口
	pygame.display.update()

	# 获取新事件
	for event in pygame.event.get():
		# 1. 鼠标点击关闭窗口事件
		if event.type == QUIT:  # 判断是不是退出
			print("点击关闭窗口按钮")
			sys.exit()  # 关闭程序

		# 2. 键盘按下事件
		if event.type == KEYDOWN:
			# 判断用户按键
			if event.key == K_LEFT or event.key == K_a:
				print("left")
			if event.key == K_RIGHT or event.key == K_d:
				print("right")
			if event.key == K_UP or event.key == K_w:
				print("up")
			if event.key == K_DOWN or event.key == K_s:
				print("down")
			if event.key == K_SPACE:
				print("space")
