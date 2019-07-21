import pygame

# Recet:矩形的意思
hero_rect = pygame.Rect(100, 500, 120, 125)  # 原点(100,500),宽:120,长:500

print('英雄的原点:%d %d' % (hero_rect.x, hero_rect.y))
print('英雄的尺寸:%d %d' % (hero_rect.width, hero_rect.height))
print('%d,%d' % hero_rect.size)
