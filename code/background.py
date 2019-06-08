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
