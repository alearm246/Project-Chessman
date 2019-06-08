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
