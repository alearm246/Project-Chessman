import pygame
from character import Character
from sword import Sword

class Player(Character):
    def __init__(self, world, x, y, width, height, speed=5):
        super().__init__(world, x, y, width, height)
        self.world = world
        self.health = 10
        self.image = pygame.image.load('assets/chessman-knight.png')
        self.my_sword = Sword('Excalibur', 10,'assets/Small_Sword_icon.png', self.x - 18, self.y +14 )
        self.speed = speed
        self.attacking = False

    def update(self): # moves the Player
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
              self.y -= self.speed
              self.my_sword.update_y(-self.speed)
          if event.key == pygame.K_s:
              self.y += self.speed
              self.my_sword.update_y(+self.speed)
          if event.key == pygame.K_a:
              self.x -= self.speed
              self.my_sword.update_x(-self.speed)
          if event.key == pygame.K_d:
              self.x += self.speed
              self.my_sword.update_x(+self.speed)
          if event.key == pygame.K_e:
              # Allow 1 attack per key pressed
              if self.attacking is False:
                self.attack()
                self.attacking = True

        elif event.type == pygame.KEYUP:
              if self.attacking:
                self.release()
                self.attacking = False

        self.check_boundary()


    def attack(self):
        self_right_side = self.x + self.width + 25
        self_left_side = self.x + self.width
        self_top_side = self.y
        self_bottom_side = self.height + self.y
        self.my_sword.attack()

        for enemy in self.world.enemy_list:
            if self.is_touching_rectangle(right=self_right_side,
                                  left=self_left_side,
                                  top=self_top_side,
                                  bottom=self_bottom_side,
                                  other_character = enemy):
                                  enemy.died()
    def release(self):
      self.my_sword.release()

    def draw(self, world_surface):
        world_surface.blit(self.image, (self.x, self.y))
        self.draw_health(0, 0)
        pygame.display.flip()
        self.my_sword.draw(world_surface)
