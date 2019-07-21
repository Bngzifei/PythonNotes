import pygame  # 动态模块.dll.pyd 静态模块:.py 静态的必须导入模块名.动态的只需要导入包名就行
import sys
from pygame.locals import *

"""
1.创建窗口
2.加载背景图片
3.把背景图片贴到窗口上
4.刷新窗口

少说话,多干活.

Python 中没有常量,只是模拟常量了.
事件监测:监听事件操作,产生相应的效果.是否监听到并处理
vs.code:记得装一下.

原理就是贴和装.
"""


# 坐标都是元组


def main():
	# 1.创建窗口
	window = pygame.display.set_mode((512, 768))
	# 2.加载背景图片
	bg_image = pygame.image.load('res/img_bg_level_1.jpg')
	# 2.1 加载英雄飞机图片
	hero_flight_img = pygame.image.load('res/hero2.png')
	# 定义两个变量来表示英雄飞机的位置
	x = 196
	y = 500
	while True:  # 无线循环,不是死循环(死循环是bug)
		# 3.把背景图片贴到窗口上
		window.blit(bg_image, (0, 0))
		# 3.1把飞机图贴到窗口上 重复贴
		window.blit(hero_flight_img, (x, y))
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
		# 键盘长按事件
		pressed_keys = pygame.key.get_pressed()
		# print(pressed_keys)  # 是一个元组类型
		# 获取当前键盘所有按键的状态(按下/没有按下),返回bool元组(0,0,0,1,0,0,0)
		# 通过索引去取对应键的值,默认都是0,0代表没按下,1表示按下.去找对应位置的为1的那个.
		if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
			print("left")
			x -= 5
		if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
			print("right")
			x += 5


if __name__ == '__main__':
	main()
