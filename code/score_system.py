import pygame
import common

class ScoreDisplay:
    def __init__(self, world):
        self.score = 0
        self.font = pygame.font.SysFont("None", 20)
        self.world = world


    def draw(self):
        font_surface = self.font.render("score: " + str(self.score), True, common.purple)
        self.world.surface.blit(font_surface,(self.world.width/2,0))


    def increment(self):
        self.score += 1
