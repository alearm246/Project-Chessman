from enemy import Enemy

class ItemAttacker(Enemy):
    def __init__(self, world,enemy_wave, x, y, image):
        super().__init__(world,enemy_wave, x, y, image)


    def update(self):
        self.move_towards(self.world.protectable_item.x, self.world.protectable_item.y)
        self.interact_with_world()
