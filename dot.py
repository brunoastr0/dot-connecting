import random as rnd
import pygame as pg
import time

pg.init()

W_HEIGHT = 720
W_WIDTH = 1080
COLORS = {'BLACK': (0, 0, 0), 'WHITE': (255, 255, 255), 'RED': (
    255, 0, 0), 'BLUE': (0, 0, 255), 'GREEN': (0, 255, 0)}

DOWN = 1
UP = 3
LEFT = 7
RIGHT = 9
movements = {0: UP, 1: DOWN, 2: LEFT, 3: RIGHT}
MOVESPEED = 2
FPS = 60

windowsSurface = pg.display.set_mode((W_WIDTH, W_HEIGHT), 0, 32)
pg.display.set_caption("Dots")
fps_Clock = pg.time.Clock()


class Dot(pg.Rect):

    def __init__(self) -> None:
        self.x = rnd.randint(0, W_WIDTH)
        self.y = rnd.randint(0, W_HEIGHT)
        self.color = COLORS['RED']
        self.radius = 3
        self.speedx = rnd.randint(1, 3)
        self.speedy = rnd.randint(1, 3)
        self.dot = pg.Rect(self.x, self.y, 8, 8)
        # self.vision = 80
        self.connected = False

    def draw(self) -> None:
        pg.draw.circle(windowsSurface, self.color,
                       (self.x, self.y), self.radius)

    def move(self):
        if self.y < 0:            # block has moved past the top
            self.y += W_HEIGHT
        if self.bottom > W_HEIGHT:  # block has moved past the bottom
            self.y -= W_HEIGHT
        if self.left < 0:         # block has moved past the left side
            self.x += W_WIDTH
        if self.right > W_WIDTH:   # block has moved past the right side
            self.x -= W_WIDTH
        self.draw()


def dist_between(x, y): return (abs(x.x-y.x)+abs(y.y-x.y))


dotList: list = []
partList = []  # list of particles for the background[stars effect]
visited = []

for i in range(0, 220):
    part = Dot()
    part.color = COLORS['WHITE']
    part.radius = 1
    partList.append(part)
    dot: Dot = Dot()
    dotList.append(dot)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    windowsSurface.fill(COLORS['BLACK'])
    can_Move = True
    for i, dot_i in enumerate(dotList):
        dot_2: Dot
        if can_Move:
            movey = rnd.random()
            if movey <= 0.03:
                MOVESPEED *= -1
                dot_i.speedy = rnd.randint(0, 3)*MOVESPEED

        else:
            movex = rnd.random()
            if movex <= 0.03:
                MOVESPEED *= -1
                dot_i.speedx = rnd.randint(0, 3)*MOVESPEED

        dot_i.left += dot_i.speedx
        dot_i.top += dot_i.speedy
        can_Move = False
        if event.type == pg.MOUSEMOTION:
            mouse_pos = pg.mouse.get_pos()
            mouse = pg.Rect(mouse_pos[0], mouse_pos[1], 6, 6)
            if dist_between(mouse, dot_i) < 200:
                pg.draw.line(windowsSurface, COLORS['GREEN'],
                             (mouse.x, mouse.y), (dot_i.x, dot_i.y), 2)
        for j, dot_j in enumerate(dotList):
            visited.append(dot_j)
            if dist_between(dot_i, dot_j) < 80 and dot_i not in visited:
                pg.draw.line(windowsSurface, COLORS['BLUE'],
                             (dot_i.x, dot_i.y), (dot_j.x, dot_j.y), 2)
        visited.clear()    
        dot_i.move()
        partList[i].draw()
    pg.display.flip()
    fps_Clock.tick(FPS)
    time.sleep(0.02)
