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

FPS = 60

windowsSurface = pg.display.set_mode((W_WIDTH, W_HEIGHT), 0, 32)
pg.display.set_caption("Dots")
fps_Clock = pg.time.Clock()


class Dot(pg.Rect):

    def __init__(self,color=False,radius=False) -> None:
        self.x = rnd.randint(0, W_WIDTH)
        self.y = rnd.randint(0, W_HEIGHT)
        self.color = color if color else COLORS['RED']
        self.radius = radius if radius else 3
        self.speedx = rnd.randint(1, 3)
        self.speedy = rnd.randint(1, 3)
        self.dot = pg.Rect(self.x, self.y, 8, 8)
        # self.vision = 80
        # self.connected = False

    def draw(self) -> None:
        pg.draw.circle(windowsSurface, self.color,
                       (self.x, self.y), self.radius)
        
    def dist_between(self,dot2:pg.Rect):
        return abs(self.x-dot2.x) + abs(dot2.y-self.y)

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

    def change_direction(self,movespeed,can_move=False):  
            movespeed*=-1
            if can_move and rnd.random() < 0.03:
                self.speedy = rnd.randint(0,3)*movespeed
            elif rnd.random() < 0.03:
                self.speedx = rnd.randint(0,3)*movespeed
            self.left+=self.speedx
            self.top+=self.speedy



                
def draw_line(screen,dots:list, mouse)->None:
    mouse_pos = pg.mouse.get_pos() if mouse else (-100,-100,-100)
    mouse_rect = pg.Rect(mouse_pos[0],mouse_pos[1],6,6) if mouse else 0
    for i, dot_i in enumerate(dots):
        for dot_j in dots[i+1:]:
            if dot_i.dist_between(dot_j) < 80:
                pg.draw.line(screen,COLORS['BLUE'],(dot_i.x, dot_i.y), (dot_j.x, dot_j.y),2)
        if mouse and dot_i.dist_between(mouse_rect) < 200:
            pg.draw.line(screen,COLORS['GREEN'],(mouse_rect.x,mouse_rect.y),(dot_i.x,dot_i.y),2)
        

dotList = [Dot() for _ in range(250)]
partList = [Dot(COLORS['WHITE'],1) for _ in range(250)]  # list of particles for the background[stars effect]


def main():
    MOVESPEED = 2
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        windowsSurface.fill(COLORS['BLACK'])
        can_Move = True
        mouse = event.type == pg.MOUSEMOTION
        draw_line(windowsSurface,dotList,mouse)
        
        for i, dot_i in enumerate(dotList):
            dot_i.change_direction(MOVESPEED,can_Move)
            can_Move = False
            dot_i.move()
            partList[i].draw()
            
        pg.display.flip()
        fps_Clock.tick(FPS)
        time.sleep(0.02)

main()