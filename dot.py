import random
import pygame
from pygame.locals import *
import time

pygame.init()

HEIGHT = 720
WIDTH = 1080
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
DOWN = 1
UP = 3
LEFT = 7
RIGHT = 9
movements = {0: UP, 1: DOWN, 2: LEFT, 3: RIGHT}
MOVESPEED = 2
FPS = 120

windowsSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Dots")
fpsClock = pygame.time.Clock()


class Dot(pygame.Rect):

    def __init__(self) -> None:
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.color = RED
        self.radius = 3
        self.speedx = random.randint(1, 3)
        self.speedy = random.randint(1, 3)
        self.dot = pygame.Rect(self.x, self.y, 8, 8)
        self.vision = 80
        self.connected = False

    def draw(self) -> None:
        pygame.draw.circle(windowsSurface, self.color,
                           (self.x, self.y), self.radius)

    def move(self):
        if self.y < 0:            # block has moved past the top
            self.y += HEIGHT
        if self.bottom > HEIGHT:  # block has moved past the bottom
            self.y -= HEIGHT
        if self.left < 0:         # block has moved past the left side
            self.x += WIDTH
        if self.right > WIDTH:   # block has moved past the right side
            self.x -= WIDTH
        self.draw()


def dist_between(x, y): return (abs(x.x-y.x)+abs(y.y-x.y))


dotList: list = []
partList = []

for i in range(0, 250):
    part = Dot()
    part.color = WHITE
    part.radius = 1
    partList.append(part)
    dot: Dot = Dot()
    dotList.append(dot)


while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    windowsSurface.fill(BLACK)
    canMove = True
    for x, i in enumerate(dotList):
        if canMove:
            movey = random.random()
            if 0.04 > movey <= 0.05:
                MOVESPEED *= -1
                i.speedy = random.randint(0, 3)*MOVESPEED

        else:
            movex = random.random()
            if 0.04 > movex <= 0.05:
                MOVESPEED *= -1
                i.speedx = random.randint(0, 3)*MOVESPEED

        i.left += i.speedx
        i.top += i.speedy
        canMove = False
        i.move()
        partList[x].draw()

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            mouse = pygame.Rect(pos[0], pos[1], 6, 6)
            if dist_between(mouse, i) < 200:
                pygame.draw.line(windowsSurface, GREEN,
                                 (mouse.x, mouse.y), (i.x, i.y), 2)
        vision = i.left+i.vision
        """if vision in (dotList[x].x,dotList[x].y):
            pygame.draw.line(windowsSurface,BLUE,(i.x,i.y),(dotList[x].x,dotList[x].y),1)
            """
        for j in dotList:
            if dist_between(i, j) < 80 and not i.connected:
                i.connected = True
                j.connected = True
                pygame.draw.line(windowsSurface, BLUE,
                                 (i.x, i.y), (j.x, j.y),2)
            i.connected = False
            j.connected = False
            
    pygame.display.update()
    fpsClock.tick(FPS)
    time.sleep(0.02)
    
    
