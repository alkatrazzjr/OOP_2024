import pygame
from pygame.draw import *

white = (205, 205, 205)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
screen.fill(white)

def draw_telo():
	circle(screen, (255, 120, 0), (250, 500), 120)
	circle(screen, (0, 0, 0), (250, 500), 120, 1)
def draw_ruki():
	ellipse(screen, (244, 222, 204), (30, 120, 50, 65))
	ellipse(screen, (244, 222, 204), (420, 120, 50, 65))
	line(screen, (244, 222, 204), [50, 150], [155, 400], 30)
	line(screen, (244, 222, 204), [450, 150], [345, 400], 30)
	polygon(screen, (255, 120, 0), [[175, 450], [130, 440], [130, 395], [170, 375], [190, 405]])
	polygon(screen, (0, 0, 0), [[175, 450], [130, 440], [130, 395], [170, 375], [190, 405]], 1)
	polygon(screen, (255, 120, 0), [[325, 450], [370, 440], [370, 395], [330, 375], [310, 405]])
	polygon(screen, (0, 0, 0), [[325, 450], [370, 440], [370, 395], [330, 375], [310, 405]], 1)
def draw_golova():
	ellipse(screen, (244, 222, 204), (162.5, 200, 175, 200))
def draw_glaza():
	circle(screen, (0, 191, 255), (220, 280), 20)
	circle(screen, (0, 0, 0), (220, 280), 20, 1)
	circle(screen, (0, 0, 0), (220, 280), 7)
	circle(screen, (0, 191, 255), (280, 280), 20)
	circle(screen, (0, 0, 0), (280, 280), 20, 1)
	circle(screen, (0, 0, 0), (280, 280), 7)
def draw_nos():
	polygon(screen, (128, 64, 48), [[240, 315], [260, 315], [250, 330]])
def draw_rot():
	polygon(screen, (255, 20, 40), [[210, 350], [290, 350], [250, 375]])
def draw_volosi():
	polygon(screen, (197, 0, 127), [[185, 230], [145, 220], [168, 263]])
	polygon(screen, (197, 0, 127), [[205, 212], [170, 195], [185, 230]])
	polygon(screen, (197, 0, 127), [[205, 212], [210, 170], [235, 200]])
	polygon(screen, (197, 0, 127), [[235, 200], [250, 170], [265, 200]])
	polygon(screen, (197, 0, 127), [[265, 200], [290, 170], [295, 212]])
	polygon(screen, (197, 0, 127), [[295, 212], [330, 195], [315, 235]])
	polygon(screen, (197, 0, 127), [[315, 235], [355, 220], [330, 265]])
def draw_tabli4ka():
	rect(screen, (100, 255, 0), (10, 90, 480, 65))
	rect(screen, (0, 0, 0), (10, 90, 480, 65), 1)	
def draw_text():
	font = pygame.font.Font(None, 65)
	text = font.render("PYTHON is AMAZING", True, (0, 0, 0))
	text_rect = text.get_rect()
	text_rect.center = (250, 125)
	screen.blit(text, text_rect)
	
draw_telo()
draw_ruki()
draw_golova()
draw_glaza()
draw_nos()
draw_rot()
draw_volosi()
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
