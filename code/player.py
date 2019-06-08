class Player(Character):
    def __init__(self, world, x, y, width, height):
        super().__init__(world, x, y, width, height)
        self.world = world
        self.health = 10
        self.image = pygame.image.load('assets/New Piskel clone.png')
        self.my_sword = Sword('Excalibur', 10,'assets/Small_Sword_icon.png', self.x + 10, self.y )

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

        if keys[pygame.K_n]:
            self.attack()

        self.check_boundary()


    def attack(self):
        self_right_side = self.x + self.width + 25
        self_left_side = self.x + self.width
        self_top_side = self.y
        self_bottom_side = self.height + self.y
        pygame.transform.rotate()

        for enemy in self.world.enemy_list:
            if self.is_touching_rectangle(right=self_right_side,
                                  left=self_left_side,
                                  top=self_top_side,
                                  bottom=self_bottom_side,
                                  other_character = enemy):
                                  enemy.died()





    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.draw_health(0, 0)
        pygame.display.flip()

        #self.CheckBou
