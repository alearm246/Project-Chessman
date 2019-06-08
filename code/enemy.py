class Enemy(Character):
    def __init__(self, world, x, y, image):
        Character.__init__(self, world)
        self.world = world
        self.world.enemy_list.append(self)
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
        if self.is_touching(self.world.player):
            self.world.player.x = 250
            self.world.player.y = 200
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.draw_health(430, 0)
        pygame.display.flip()
