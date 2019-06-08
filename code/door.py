class Door():
    def __init__(self, world, background, x, y):
        self.world = world
        self.width = 16
        self.height = 16
        self.x = x
        self.y = y
        self.app_background = background

    def update(self, world, other_character):
        if self.is_touching(other_character):
            pass


    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 225), [self.x,self.y,35,35])
        #pygame.draw.rect(surface, (0, 0, 225), [290,150,35,35])
        #surface.0blit(surface,(self.x, self.y

    def is_touching(self, other_character):
        self_left_X = self.x
        self_top_Y = self.y
        self_bottom_Y = self.height + self.y
        self_right_X = self.width + self.x
        other_left_x = other_character.x
        other_top_Y = other_character.y
        other_bottom_Y = other_character.height + other_character.y
        other_right_X = other_character.width + other_character.x
        if (

          self_right_X >= other_left_x
          and self_left_X <= other_right_X
          and self_bottom_Y >= other_top_Y
          and self_top_Y <= other_bottom_Y
        ):
          return True
        else:
          return False

    def check_door_touching(self, other_character):
        if self.is_touching(other_character):
            self.world.change_location(pygame.image.load('assets/pixel_500x330.png'))
            self.world.player.x = 225
            self.world.player.y = 85
            return True
        else:
            return False
