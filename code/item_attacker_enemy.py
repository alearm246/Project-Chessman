from enemy import Enemy

class itemAttacker(Enemy):
    def __init__(self, world, x, y, image):
        super().__init__(world, x, y, image)

    def update(self):
        self.move_towards(self.world.protectable_item.x, self.world.protectable_item.y)
        self.interact_with_world()
