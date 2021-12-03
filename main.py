import pygame, sys
import math
import random
from pygame.locals import *

pygame.init()

HEIGHT = 500
WIDTH = 400

windowsSurface = pygame.display.set_mode((HEIGHT,WIDTH),0,32)
pygame.display.set_caption("Dots")

BLACL = (0,0,0)
WHITE = (255,255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
FPS = 20
fpsClock = pygame.time.Clock()


windowsSurface.fill(WHITE)

def circle() -> list:
    lista = list()
    if random.random() <= 0.8:
        dot = pygame.draw.circle(windowsSurface,RED,(random.randint(0,HEIGHT),random.randint(0,WIDTH)),2)
        lista.append(dot)
        for i in range(len(lista)):
            for j in range(len(lista)):
                dist_between = lambda x,y:(abs(x.x-y.x)+abs(y.y-x.y))
                dist = dist_between(lista[i],lista[j])
                print(dist)
                if dist < 10:
                        rect = pygame.draw.line(windowsSurface, RED, (lista[j].x,lista[j].y),(lista[i].x,lista[i].y))

        
    
dot1 = pygame.draw.circle(windowsSurface, GREEN, (random.randint(0,100),50), 2)
dot2 = pygame.draw.circle(windowsSurface, GREEN,(100,100),2)
dist_between = lambda x,y:(abs(x.x-y.x)+abs(y.y-x.y))
dist = dist_between(dot1,dot2)
print(dist)

if dist <= 100:
    rect = pygame.draw.line(windowsSurface, RED, (dot1.x,dot1.y),(dot2.x,dot2.y))
    




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    circle()
    pygame.display.update()
    fpsClock.tick(FPS)