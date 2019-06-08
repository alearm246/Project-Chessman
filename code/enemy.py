import pygame
from character import Character


class Enemy(Character):
    def __init__(self, world, x, y, image):
        super().__init__(world, x, y, 12, 12)
        self.world.enemy_list.append(self)
        self.health = 10
        self.image = image

    def update(self):
        #self.update_random()
        pass
    def interact_with_world(self):
        self.check_boundary()
        if self.is_touching(self.world.player):
            self.world.player.x = 250
            self.world.player.y = 200
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.draw_health(430, 0)
        pygame.display.flip()
