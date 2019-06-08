import pygame


class ProtectableItem(pygame.Rect):
    def __init__(self, world,x, y, image_filename):
        self.image = pygame.image.load(image_filename)
        self.health = 10
        super().__init__(x, y, self.image.get_width(), self.image.get_height())

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def is_being_attacked(self, other_character):
        if self.colliderect(other_character):
            self.health -= 1
        if self.health <= 0:
            self.kill()

    def kill(self):
        print("You won, Your score blank") #make screen change color and show score

    def
