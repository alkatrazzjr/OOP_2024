import pygame
from pygame.draw import *

white = (205, 205, 205)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 500))
screen.fill(white)

def draw_telo1():
	circle(screen, (120, 255, 0), (250, 500), 120)
	circle(screen, (0, 0, 0), (250, 500), 120, 1)
def draw_telo2():
	circle(screen, (255, 120, 0), (750, 500), 120)
	circle(screen, (0, 0, 0), (750, 500), 120, 1)
def draw_ruki1():
	ellipse(screen, (244, 222, 204), (30, 120, 50, 65))
	ellipse(screen, (244, 222, 204), (420, 120, 50, 65))
	line(screen, (244, 222, 204), [50, 150], [155, 400], 30)
	line(screen, (244, 222, 204), [450, 150], [345, 400], 30)
	polygon(screen, (120, 255, 0), [[175, 450], [130, 440], [130, 395], [170, 375], [190, 405]])
	polygon(screen, (0, 0, 0), [[175, 450], [130, 440], [130, 395], [170, 375], [190, 405]], 1)
	polygon(screen, (120, 255, 0), [[325, 450], [370, 440], [370, 395], [330, 375], [310, 405]])
	polygon(screen, (0, 0, 0), [[325, 450], [370, 440], [370, 395], [330, 375], [310, 405]], 1)
def draw_ruki2():
	ellipse(screen, (244, 222, 204), (530, 120, 50, 65))
	ellipse(screen, (244, 222, 204), (920, 120, 50, 65))
	line(screen, (244, 222, 204), [550, 150], [655, 400], 30)
	line(screen, (244, 222, 204), [950, 150], [845, 400], 30)
	polygon(screen, (255, 120, 0), [[675, 450], [630, 440], [630, 395], [670, 375], [690, 405]])
	polygon(screen, (0, 0, 0), [[675, 450], [630, 440], [630, 395], [670, 375], [690, 405]], 1)
	polygon(screen, (255, 120, 0), [[825, 450], [870, 440], [870, 395], [830, 375], [810, 405]])
	polygon(screen, (0, 0, 0), [[825, 450], [870, 440], [870, 395], [830, 375], [810, 405]], 1)
def draw_golova1():
	ellipse(screen, (244, 222, 204), (162.5, 200, 175, 200))
def draw_golova2():
	ellipse(screen, (244, 222, 204), (662.5, 200, 175, 200))
def draw_glaza1():
	circle(screen, (200, 200, 200), (220, 280), 20)
	circle(screen, (0, 0, 0), (220, 280), 20, 1)
	circle(screen, (0, 0, 0), (220, 280), 7)
	circle(screen, (200, 200, 200), (280, 280), 20)
	circle(screen, (0, 0, 0), (280, 280), 20, 1)
	circle(screen, (0, 0, 0), (280, 280), 7)
def draw_glaza2():
	circle(screen, (0, 191, 255), (720, 280), 20)
	circle(screen, (0, 0, 0), (720, 280), 20, 1)
	circle(screen, (0, 0, 0), (720, 280), 7)
	circle(screen, (0, 191, 255), (780, 280), 20)
	circle(screen, (0, 0, 0), (780, 280), 20, 1)
	circle(screen, (0, 0, 0), (780, 280), 7)
def draw_nos1():
	polygon(screen, (128, 64, 48), [[240, 315], [260, 315], [250, 330]])
def draw_nos2():
	polygon(screen, (128, 64, 48), [[740, 315], [760, 315], [750, 330]])
def draw_rot1():
	polygon(screen, (255, 20, 40), [[210, 350], [290, 350], [250, 375]])
def draw_rot2():
	polygon(screen, (255, 20, 40), [[710, 350], [790, 350], [750, 375]])
def draw_volosi1():
	polygon(screen, (255, 255, 0), [[185, 230], [145, 220], [168, 263]])
	polygon(screen, (255, 255, 0), [[205, 212], [170, 195], [185, 230]])
	polygon(screen, (255, 255, 0), [[205, 212], [210, 170], [235, 200]])
	polygon(screen, (255, 255, 0), [[235, 200], [250, 170], [265, 200]])
	polygon(screen, (255, 255, 0), [[265, 200], [290, 170], [295, 212]])
	polygon(screen, (255, 255, 0), [[295, 212], [330, 195], [315, 235]])
	polygon(screen, (255, 255, 0), [[315, 235], [355, 220], [330, 265]])
def draw_volosi2():
	polygon(screen, (197, 0, 127), [[685, 230], [645, 220], [668, 263]])
	polygon(screen, (197, 0, 127), [[705, 212], [670, 195], [685, 230]])
	polygon(screen, (197, 0, 127), [[705, 212], [710, 170], [735, 200]])
	polygon(screen, (197, 0, 127), [[735, 200], [750, 170], [765, 200]])
	polygon(screen, (197, 0, 127), [[765, 200], [790, 170], [795, 212]])
	polygon(screen, (197, 0, 127), [[795, 212], [830, 195], [815, 235]])
	polygon(screen, (197, 0, 127), [[815, 235], [855, 220], [830, 265]])
def draw_tabli4ka():
	rect(screen, (100, 255, 0), (10, 90, 980, 65))
	rect(screen, (0, 0, 0), (10, 90, 980, 65), 1)	
def draw_text():
	font = pygame.font.Font(None, 95)
	text = font.render("PYTHON is REALLY AMAZING!", True, (0, 0, 0))
	text_rect = text.get_rect()
	text_rect.center = (500, 125)
	screen.blit(text, text_rect)
	
draw_telo1()
draw_telo2()
draw_ruki1()
draw_ruki2()
draw_golova1()
draw_golova2()
draw_glaza1()
draw_glaza2()
draw_nos1()
draw_nos2()
draw_rot1()
draw_rot2()
draw_volosi1()
draw_volosi2()
draw_tabli4ka()
draw_text()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
