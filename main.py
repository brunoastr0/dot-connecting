import pygame
import random as rnd

pygame.init()

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 400

w_surface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH), 0, 32)
pygame.display.set_caption("Dots")

COLORS = {"BLACK": (0, 0, 0), "WHITE": (255, 255, 255, 255), "RED": (255, 0, 0),
          "BLUE": (0, 0, 255), "GREEN": (0, 255, 0)}

FPS = 20
fpsClock = pygame.time.Clock()

w_surface.fill(COLORS["WHITE"])


def circle() -> list:
    dots_list = []
    if rnd.random() < 0.8:
        return None
    dot = pygame.draw.circle(w_surface, COLORS["RED"], (rnd.randint(0, WINDOW_HEIGHT), rnd.randint(0, WINDOW_WIDTH)), 2)
    dots_list.append(dot)
    for i, dot_i in enumerate(dots_list):
        for j, dot_j in enumerate(dots_list):
            distance = abs(dot_i.x - dot_j.x) + abs(dot_i.y - dot_j.y)
            print(distance)
            if dist < 80:
                pygame.draw.line(w_surface, COLORS["RED"], (dot_i.x, dot_j.y), (dot_i.x, dot_i.y))


dot1 = pygame.draw.circle(w_surface, COLORS["GREEN"], (rnd.randint(0, 100), 50), 2)
dot2 = pygame.draw.circle(w_surface, COLORS["GREEN"], (100, 100), 2)
dist = abs(dot1.x - dot2.x) + abs(dot1.y - dot2.y)
print(dist)

if dist <= 100:
    rect = pygame.draw.line(w_surface, COLORS["RED"], (dot1.x, dot1.y), (dot2.x, dot2.y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    circle()
    pygame.display.update()
    fpsClock.tick(FPS)
