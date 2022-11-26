import pygame
import sys
pygame.init()

size=width, height =300,300
red=(255,0,0)

screen=pygame.display.set_mode((size),0,32)
pygame.display.set_caption("為畫布上色")

face=pygame.Surface([100,100])
face.fill(red)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
sys.ext()
pygame.display.update()