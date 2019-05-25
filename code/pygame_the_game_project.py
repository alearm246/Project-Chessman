import pygame
import sys
import time
import random
from pygame.locals import *

FPS = 30
pygame.init()
fpsClock=pygame.time.Clock()

window_size = SCREEN_WIDTH, SCREEN_HEIGHT = 320,240
screen = pygame.display.set_mode(window_size,RESIZABLE)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255,255,255))

pygame.key.set_repeat(1, 40)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#Health = 1

font = pygame.font.SysFont("None", 20)
text = font.render("hello there", True, red)
player_text = font.render("player", True, green)
enemy_text = font.render("Enemy", True, red)
#healthscore = font.render("Health : " + str(Health), True, black)

class Character:
    def __init__(self, world):
        self.world = world
        self.x = 0
        self.y = 0
        self.width = 7
        self.height = 10
        self.step = 1
        self.health = 10
        self.health_score = font.render("Health : " + str(self.health), True, blue)
        #self.visible = True

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

    def Interacting(self, other_character): # checks for interactions
         if other_character ==  None:
             return
         if self.is_touching(other_character):
             other_character.display_text = " "

    def draw_health(self, x, y):
        surface.blit(self.health_score, (x, y))

    def lives_removed(self, other_character):
        if other_character == None:
            return
        if self.is_touching(other_character):
            self.health -= 1
            self.health_score = font.render("Health : " + str(self.health), True, blue)
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

class Player(Character):
    def __init__(self, world):
        Character.__init__(self, world)
        self.world = world
        self.x = 225
        self.y = 85
        self.color = green
        self.width = 16 # exact image dimensions (otherwise it gets cut off)
        self.height = 16 # exact image dimensions (otherwise it gets cut off)
        self.health = 10
        self.image = pygame.image.load('assets/New Piskel clone.png')

    def update(self): # moves the Player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 2
        if keys[pygame.K_s]:
            self.y += 2
        if keys[pygame.K_a]:
            self.x -= 2
        if keys[pygame.K_d]:
            self.x += 2
        self.check_boundary()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.draw_health(0, 0)
        pygame.display.flip()
        #self.CheckBoundary()

class NonPlayer(Character):
    def  __init__(self, world, image):
        Character.__init__(self, world)
        self.world = world
        self.x = 100
        self.y = 100
        self.width = 32
        self.height = 32
        self.display_text = ""
        self.image = image
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        if self.display_text != '':
            surface.blit(text, (self.x, self.y - 10))

        pygame.display.flip()

    def update(self):
        self.update_walk()
        self.check_boundary()

class Enemy(Character):
    def __init__(self, world, x, y, image):
        Character.__init__(self, world)
        self.world = world
        self.world.enemy_list.append(self, self.enemy, self.enemy2)
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12
        self.color = red
        self.health = 10
        self.image = image

    def update(self):
        self.update_random()
        self.check_boundary()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.draw_health(430, 0)
        pygame.display.flip()

class Background():
    def __init__(self, world, background_image):
        self.world = world
        self.x = 0
        self.y = 0
        self.width = 740
        self.height = 400
        self.image = background_image

    def change_image(self, background_image):
        self.image = background_image

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


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

class World:
    def __init__(self):
        self.enemy_list = []
        self.width = 160
        self.height = 100
        self.player = Player(self)
        self.background = Background(self, pygame.image.load('assets/background_image.png'))
        self.door = Door(self,self.background, 0, 150)
        self.door_2 = Door(self,self.background,0,50)

        '''
        self.enemy = None
        self.enemy2 = None
        '''
        self.npc = None





    def update(self):
        self.player.update()
        '''
        self.player.is_touching(self.enemy)
        self.player.lives_removed(self.enemy)
        self.player.kill(self.enemy)
        self.player.is_touching(self.enemy2)
        self.player.lives_removed(self.enemy2)
        '''
        self.player.Interacting(self.npc)
        self.door.check_door_touching(self.player)
        self.door.check_door_touching(self.player)
        self.player.Interacting(self.npc)
        for this_enemy in self.enemy_list:
            this_enemy.update()
        if self.npc != None:
            self.npc.update()

    def draw(self):
        surface.fill((0, 0, 0)) # clear screen (Paint it all white)
        self.background.draw(surface)
        self.player.draw(surface)
        if self.npc != None:
            self.npc.draw(surface)
        for this_enemy in self.enemy_list:
            this_enemy.draw(surface)
            this_enemy.draw(surface)
        self.door.draw(surface)

        screen.blit(surface, (0,0)) # this might be what was missing
        pygame.display.update() #  Actually do all the stuff? (Not actually sure what this does... but I think it should be called at the end of the drawing step)
        fpsClock.tick(FPS)

    def change_location(self, background_image):
        self.background.change_image(background_image)
        self.npc = NonPlayer(self, pygame.image.load('assets/npc_32x32.png'))

class App:
    def __init__(self):
        self.width = 160
        self.height = 120
        self.world = World()
        # Load images here after initializing, but before running
        ### PYGAME TODO:
        ### - need to figure out how pygame load images, and put loading here...


        while True: # our main game update/draw loop
            self.update()
            self.draw()


    def update(self):
        self.world.update()


        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    def draw(self):
        self.world.draw()


App()
