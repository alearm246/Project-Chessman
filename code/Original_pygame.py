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

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
black = (0, 0, 0)

#Health = 1

font = pygame.font.SysFont("None", 20)
text = font.render("hello there", True, RED)
playerText = font.render("player", True, GREEN)
enemyText = font.render("Enemy", True, RED)
#healthscore = font.render("Health : " + str(Health), True, black)

class Character:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 7
        self.height = 10
        self.step = 1
        self.health = 10
        self.healthscore = font.render("Health : " + str(self.health), True, BLUE)
        self.visible = True


    def update_random(self):
        randomNumberY = random.random() # decimal number between 0 and 1
        randomNumberX = random.random() # decimal number between 0 and 1

        if randomNumberY < .5: # 50% chance move up
            self.y -= 1
        else: # 50% chance move down
            self.y += 1
        if randomNumberX < .5: #50% chance move left
            self.x -= 1
        else: # 50% chance move right
            self.x += 1

    def update_walk(self):
        self.x = self.x+self.step
        if self.x == 50:
            self.step = self.step + -1
        elif self.x == 0:
            self.step = self.step + 1

    def CheckBoundary(self):
            if self.x > 484:
                self.x = 484
            if self.y > 314:
                self.y = 314
            if self.x < 0:
                self.x = 0
            if self.y < 0:
                self.y = 0

    def IsTouching(self, otherCharacter): #checks for collisions
        self_left_X = self.x
        self_top_Y = self.y
        self_bottom_Y = self.height + self.y
        self_right_X = self.width + self.x
        other_left_x = otherCharacter.x
        other_top_Y = otherCharacter.y
        other_bottom_Y = otherCharacter.height + otherCharacter.y
        other_right_X = otherCharacter.width + otherCharacter.x
        if (

          self_right_X >= other_left_x
          and self_left_X <= other_right_X
          and self_bottom_Y >= other_top_Y
          and self_top_Y <= other_bottom_Y
        ):
          return True
        else:
          return False

    def Interacting(self, otherCharacter): # checks for interactions
         if self.IsTouching(otherCharacter):
             otherCharacter.displayText = " "

    def DrawHealth(self, x, y):
        surface.blit(self.healthscore, (x, y))

    def LivesRemoved(self, otherCharacter):
        if self.IsTouching(otherCharacter):
            self.health -= 1
            self.healthscore = font.render("Health : " + str(self.health), True, BLUE)
        if self.health < 1:
            self.health = 1
            self.Died()


    def Died(self):
        self.x = 225
        self.y = 85


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.x = 225
        self.y = 85
        self.color = GREEN
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
        self.CheckBoundary()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.DrawHealth(0, 0)
        pygame.display.flip()
        #self.CheckBoundary()

class NonPlayer(Character):
    def  __init__(self):
        Character.__init__(self)
        self.x = 36
        self.y = 36
        self.width = 32
        self.height = 32
        self.displayText = ""
        self.image = pygame.image.load('assets/npc_32x32.png')

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        if self.displayText != '':
            surface.blit(text, (self.x, self.y - 10))

        pygame.display.flip()

    def update(self):
        self.update_walk()
        self.CheckBoundary()

class Enemy(Character):
    def __init__(self):
        Character.__init__(self)
        self.x = 100
        self.y = 100
        self.width = 12
        self.height = 12
        self.color = RED
        self.health = 10
        self.image = pygame.image.load('assets/bad_face_12x12.png')

    def update(self):
        self.update_random()
        self.CheckBoundary()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.DrawHealth(430, 0)
        pygame.display.flip()

class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 740
        self.height = 400
        self.image = pygame.image.load('assets/background_image.png')

    def draw(self):
        surface.blit(self.image, (self.x, self.y))


class Door():
    def __init__(self, background):

        self.width = 16
        self.height = 16
        self.x = 0
        self.y = 150
        self.appBackground = background

    def update(self, otherCharacter):
        if self.IsTouching(otherCharacter):
            pass


    def draw(self):
        pygame.draw.rect(surface, (0, 0, 225), [self.x,self.y,35,35])
        #surface.0blit(surface,(self.x, self.y

    def IsTouching(self, otherCharacter):
        self_left_X = self.x
        self_top_Y = self.y
        self_bottom_Y = self.height + self.y
        self_right_X = self.width + self.x
        other_left_x = otherCharacter.x
        other_top_Y = otherCharacter.y
        other_bottom_Y = otherCharacter.height + otherCharacter.y
        other_right_X = otherCharacter.width + otherCharacter.x
        if (

          self_right_X >= other_left_x
          and self_left_X <= other_right_X
          and self_bottom_Y >= other_top_Y
          and self_top_Y <= other_bottom_Y
        ):
          return True
        else:
          return False

    def CheckDoorTouching(self, otherCharacter):
        if self.IsTouching(otherCharacter):
            print("touch")
            self.ChangeWorld()

    def ChangeWorld(self):
        print(self.appBackground)
        self.appBackground.image = pygame.image.load('assets/pixel_500x330.png')


class App:
    def __init__(self):
        self.width = 160
        self.height = 120
        self.App = App()
        self.Player = Player()
        self.Enemy = Enemy()
        self.npc = NonPlayer()
        self.Enemy2 = Enemy()
        self.background = Background()
        self.Door = Door(self.background)
    
        # Load images here after initializing, but before running
        ### PYGAME TODO:
        ### - need to figure out how pygame load images, and put loading here...
        background2 = pygame.image.load('assets/pixel_500x330.png')

        while True: # our main game update/draw loop
            self.update()
            self.draw()

    def update(self):
        self.Player.update()
        self.npc.update()
        self.Enemy.update()
        self.Enemy2.update()
        self.Player.IsTouching(self.Enemy)
        self.Player.IsTouching(self.Enemy2)
        self.Player.Interacting(self.npc)
        self.Player.LivesRemoved(self.Enemy)
        self.Player.LivesRemoved(self.Enemy2)
        self.Door.CheckDoorTouching(self.Player)
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    def draw(self):
        surface.fill((0, 0, 0)) # clear screen (Paint it all white)
        self.background.draw()
        self.Player.draw(surface)
        self.npc.draw(surface)
        self.Enemy.draw(surface)
        self.Enemy2.draw(surface)
        self.Door.draw()
        #self.Player.LivesRemoved(self.Enemy)
        #self.Player.LivesRemoved(self.Enemy2)
        screen.blit(surface, (0,0)) # this might be what was missing

        pygame.display.update() #  Actually do all the stuff? (Not actually sure what this does... but I think it should be called at the end of the drawing step)
        fpsClock.tick(FPS)

App()
