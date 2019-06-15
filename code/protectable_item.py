import pygame


class ProtectableItem(pygame.Rect):
    def __init__(self, world,app, x, y, image_filename):
        self.image = pygame.image.load(image_filename)
        self.health = 10
        self.world = world
        self.app = app
        super().__init__(x, y, self.image.get_width(), self.image.get_height())

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def is_attacked(self):
        self.health -= 1
        if self.health == 0:
            self.app.lose_game()

    def kill(self):
        print("You won, Your score blank") #make screen change color and show score
