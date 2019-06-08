import pygame

class Weapon(pygame.Rect):
    def __init__(self,name, damage, image_filename, x, y):
        self.image_surface = pygame.image.load(image_filename)
        super().__init__(x, y, self.image_surface.get_width(),
                               self.image_surface.get_height())
        #print(self.imafe.get_width())
    #self.durability = durability
        self.name = name
        self.damage = damage

    def draw(self):
        surface.blit()
