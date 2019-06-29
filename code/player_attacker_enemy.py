from enemy import Enemy


class PlayerAttacker(Enemy):
    def __init__(self, world,enemy_wave, x, y, image):
        super().__init__(world, enemy_wave, x, y, image)

    def update(self):
        self.move_towards(self.world.player.x, self.world.player.y)
        self.interact_with_world()
