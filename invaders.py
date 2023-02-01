from models import Plane, Enemy
from settings import *

class Invaders:
    def __init__(self, game):
        self.game = game
        self.sprite_group = pg.sprite.Group()
        self.enemy = Enemy(self, [400, 100])
        self.plane = Plane(self, self.game.plane_pos)

    def load_background(self):
        pass

    def update(self, plane_pos):
        self.plane.update(plane_pos, self.enemy)

    def draw(self):
        self.sprite_group.draw(self.game.window)