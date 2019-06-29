from item_attacker_enemy import ItemAttacker
from player_attacker_enemy import PlayerAttacker
import pygame

class EnemyWave:
    def __init__(self, world):
        self.world = world
        self.num_total_enemies = 1
        self.current_wave_num = 1

        self.spawn_enemy()

    def update(self):
        pass

    def spawn_enemy(self):
        for enemy_number in range(0,self.num_total_enemies):
            if self.num_total_enemies % 2 == 0:
                PlayerAttacker(self.world,self, 50, 50,  pygame.image.load('assets/demon1.png'))
            else:
                ItemAttacker(self.world,self, 10, 10,  pygame.image.load('assets/demon1.png'))
        print(enemy_number)
    def create_new_wave(Self):
        pass
