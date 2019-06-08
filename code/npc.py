import pygame
import common
from character import Character

class NonPlayer(Character):
    def  __init__(self, world, image):
        Character.__init__(self, world, 100, 100, 32, 32)
        self.world = world
        self.display_text = ""
        self.image = image
        self.text = pygame.font.SysFont("None", 20).render("hello there", True, common.red)

    def draw(self, surface):
        self.world.surface.blit(self.image, (self.x, self.y))
        if self.display_text != '':
            self.world.surface.blit(self.text, (self.x, self.y - 10))

        pygame.display.flip()

    def update(self):
        self.update_walk()
        self.check_boundary()
