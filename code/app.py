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
