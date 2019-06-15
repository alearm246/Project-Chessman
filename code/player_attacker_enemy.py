from enemy import Enemy

class PlayerAttacker(Enemy):
    def __init__(self, world, x, y, image):
        super().__init__(world, x, y, image)

    def update(self):
        self.move_towards(self.world.player.x, self.world.player.y)
        self.interact_with_world(self.world.player)
