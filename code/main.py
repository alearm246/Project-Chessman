import pygame
import sys
import time
import random
from pygame.locals import *

FPS = 30
pygame.init()
fpsClock=pygame.time.Clock()

window_size = SCREEN_WIDTH, SCREEN_HEIGHT = 320,240
screen = pygame.display.set_mode(window_size,RESIZABLE)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255,255,255))

pygame.key.set_repeat(1, 40)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#Health = 1

font = pygame.font.SysFont("None", 20)
text = font.render("hello there", True, red)
player_text = font.render("player", True, green)
enemy_text = font.render("Enemy", True, red)
#healthscore = font.render("Health : " + str(Health), True, black)

App()
