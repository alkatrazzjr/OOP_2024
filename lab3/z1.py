import pygame
from pygame.draw import *

white = (205, 205, 205)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(white)

def draw_litso():
	circle(screen, (255, 255, 0), (200, 175), 100)
	circle(screen, (0, 0, 0), (200, 175), 100, 2)
def draw_lglaz():
	circle(screen, (255, 0, 0), (160, 150), 25)
	circle(screen, (0, 0, 0), (160, 150), 25, 2)
	circle(screen, (0, 0, 0), (160, 150), 10)
	circle(screen, (0, 0, 0), (160, 150), 10, 2)
	line(screen, (0, 0, 0), [110, 90], [190, 136], 12)
def draw_pglaz():
	circle(screen, (255, 0, 0), (240, 150), 20)
	circle(screen, (0, 0, 0), (240, 150), 20, 2)
	circle(screen, (0, 0, 0), (240, 150), 8)
	circle(screen, (0, 0, 0), (240, 150), 8, 2)
	line(screen, (0, 0, 0), [215, 136], [281, 101], 12)
def draw_rot():
	rect(screen, (0, 0, 0), (155, 225, 90, 20))

draw_litso()
draw_lglaz()
draw_pglaz()
draw_rot()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
