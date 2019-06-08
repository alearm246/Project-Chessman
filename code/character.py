import pygame
import common
import random

class Character(pygame.Rect):
    def __init__(self, world, x, y, width, height):
        super().__init__(x, y, width, height)
        self.world = world
        self.step = 1
        self.health = 10
        self.font = pygame.font.SysFont("None", 20)

        self.health_score = self.font.render("Health : " + str(self.health),
                            True, common.blue)

    def update_random(self):
        random_number_y = random.random() # decimal number between 0 and 1
        random_number_x = random.random() # decimal number between 0 and 1

        if random_number_y < .5: # 50% chance move up
            self.y -= 1
        else: # 50% chance move down
            self.y += 1
        if random_number_x < .5: #50% chance move left
            self.x -= 1
        else: # 50% chance move right
            self.x += 1

    def update_walk(self):
        self.x = self.x+self.step
        if self.x > 50:
            self.step = self.step + -1
        elif self.x > 0:
            self.step = self.step + 1

    def check_boundary(self):
            if self.x > 484:
                self.x = 484
            if self.y > 314:
                self.y = 314
            if self.x < 0:
                self.x = 0
            if self.y < 0:
                self.y = 0

    def is_touching(self, other_character): #checks for collisions
        if other_character == None:
            return
        self_left_X = self.x
        self_top_Y = self.y
        self_bottom_Y = self.height + self.y
        self_right_X = self.width + self.x
        return self.is_touching_rectangle(self_left_X, self_bottom_Y,
                                     self_top_Y, self_right_X, other_character)

    def is_touching_rectangle(self,left, bottom, top, right, other_character):
        other_left_x = other_character.x
        other_top_Y = other_character.y
        other_bottom_Y = other_character.height + other_character.y
        other_right_X = other_character.width + other_character.x
        if (

          right >= other_left_x
          and left <= other_right_X
          and bottom >= other_top_Y
          and top <= other_bottom_Y
        ):
          return True
        else:
          return False

    def Interacting(self, other_character): # checks for interactions
         if other_character ==  None:
             return
         if self.is_touching(other_character):
             other_character.display_text = " "

    def draw_health(self, x, y):
        self.world.surface.blit(self.health_score, (x, y))

    def lives_removed(self, other_character):
        if other_character == None:
            return
        if self.is_touching(other_character):
            self.health -= 1
            self.health_score = self.font.render("Health : " + str(self.health), True, blue)
        if self.health < 1:
            self.health = 1
            self.died()

    def died(self):
        self.x = 225
        self.y = 85

    def destroy(self):
        self = None

    def kill(self, other_character):
        if self.is_touching(other_character):
            self.destroy()
