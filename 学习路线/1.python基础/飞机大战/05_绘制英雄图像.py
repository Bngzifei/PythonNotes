import pygame

pygame.init()

# 创建窗口
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
#   1>加载图片数据
bg = pygame.image.load('./images/background.png')
# 2>blit绘制图像
screen.blit(bg, (0, 0))
# 3>更新屏幕显示,即刷新操作
pygame.display.update()

hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (150, 300))
pygame.display.update()

while True:
	pass
pygame.quit()
