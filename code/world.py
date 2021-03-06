import pygame
import random
from pygame.locals import *

from player import Player
from npc import NonPlayer
from background import Background
from door import Door
from player_attacker_enemy import PlayerAttacker
from protectable_item import ProtectableItem
from item_attacker_enemy import itemAttacker
from score_system import ScoreDisplay

class World:
    def __init__(self, app):
        self.app = app
        self.enemy_list = []
        self.width = 640
        self.height = 480
        self.player = Player(self, 225, 85, 15, 15)
        self.background = Background(self, pygame.image.load('assets/background_image.png'))
        self.door = Door(self,self.background, 0, 150)
        self.door_2 = Door(self,self.background,0,50)
        self.npc = None
        self.protectable_item = ProtectableItem(self,app,150,150, 'assets/cake.png')
        self.score_display = ScoreDisplay(self)
        window_size = SCREEN_WIDTH, SCREEN_HEIGHT = 320,240
        self.screen = pygame.display.set_mode(window_size,RESIZABLE)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.fpsClock=pygame.time.Clock()


    def update(self):
        self.player.update()
        self.player.Interacting(self.npc)
        if self.door.check_door_touching(self.player):
            for enemy_number in range(0,1):
                PlayerAttacker(self, 50, 50,  pygame.image.load('assets/demon1.png'))
                itemAttacker(self, 10, 10,  pygame.image.load('assets/demon1.png'))



        #self.door.check_door_touching(self.player)
        self.player.Interacting(self.npc)
        for this_enemy in self.enemy_list:
            this_enemy.update()
        if self.npc != None:
            self.npc.update()

    def draw(self):
        self.surface.fill((0, 0, 0)) # clear screen (Paint it all white)
        self.background.draw(self.surface)
        self.player.draw(self.surface)
        self.protectable_item.draw(self.surface)
        self.score_display.draw()
        if self.npc != None:
            self.npc.draw(self.surface)
        for this_enemy in self.enemy_list:
            this_enemy.draw(self.surface)
            this_enemy.draw(self.surface)
        self.door.draw(self.surface)

        self.screen.blit(self.surface, (0,0)) # this might be what was missing
        pygame.display.update() #  Actually do all the stuff? (Not actually sure what this does... but I think it should be called at the end of the drawing step)
        FPS = 30
        self.fpsClock.tick(FPS)

    def change_location(self, background_image):
        self.background.change_image(background_image)
        self.npc = NonPlayer(self, pygame.image.load('assets/npc_32x32.png'))
