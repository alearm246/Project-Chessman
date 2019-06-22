import pygame
from weapon import Weapon

class Sword(Weapon):
    def __init__(self, name, damage, image_filename, x, y):
        Weapon.__init__(self, name, damage, image_filename, x, y)

    def update():
        pass

    def attack(self):
        self.rotate_image(90)
        print("attack")

    def draw(self, world_surface):
        world_surface.blit(self.image_surface, (self.x, self.y))

    def update_x(self, player_x_movement):
      self.x += player_x_movement
    def update_y(self, player_y_movement):
      self.y += player_y_movement

    def release(self):
      self.rotate_image(-90)

    def rotate_image(self, angle):
      self.image_surface = pygame.transform.rotate(self.image_surface, angle)
