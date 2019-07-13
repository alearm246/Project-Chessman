import pygame
from character import Character


class Enemy(Character):
    def __init__(self, world,  x, y, image):
        super().__init__(world, x, y, 12, 12)
        self.world.enemy_list.append(self)
        self.health = 10
        self.image = image
        self.death_observers = []

    def update(self):
        #self.update_random()
        pass
    def interact_with_world(self):
        self.check_boundary()
        if self.is_touching(self.world.player):
            self.world.player.x = 250
            self.world.player.y = 200
        if self.colliderect(self.world.protectable_item):
            self.world.protectable_item.is_attacked()

    def died(self):
        super().died()
        self.world.score_display.score += 1
        print("health")
        for observer in self.death_observers:
            pass



    def add_death_listener(self, to_notify):
        self.death_observers.append(to_notify)


    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.draw_health(430, 0)
        pygame.display.flip()
