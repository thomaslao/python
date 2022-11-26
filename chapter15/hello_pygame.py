import pygame
import sys
pygame.init()

screen=pygame.display.set_mode((300,300),1)
pygame.display.set_caption("我的第一支Pygame程式")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quite()
sys.exit()

