import pygame  # 动态模块.dll.pyd 静态模块:.py 静态的必须导入模块名.动态的只需要导入包名就行

"""
1.创建窗口
2.加载背景图片
3.把背景图片贴到窗口上
4.刷新窗口

vs.code:记得装一下.
"""
# 坐标都是元组

# 1.创建窗口
window = pygame.display.set_mode((512, 768))

# 2.加载背景图片
bg_image = pygame.image.load('res/img_bg_level_1.jpg')

while True:
	# 3.把背景图片贴到窗口上
	window.blit(bg_image, (0, 0))

	# 4.刷新窗口
	pygame.display.update()

