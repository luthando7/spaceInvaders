from settings import *
from .bullet import Bullet

class Plane(pg.sprite.Sprite):
    def __init__(self, invaders, pos):
        super().__init__(invaders.sprite_group)
        self.size = 50
        self.invaders = invaders
        self.image = pg.Surface([self.size, self.size])
        self.image.fill('orange')
        self.position = pos
        self.bullet = Bullet(self.invaders, [self.position[0] + 20, self.position[1] - 10])

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position[0], self.position[1]

    def update(self, pos):
        if self.bullet.position[1] < 0:
            self.bullet.kill()
            self.bullet = Bullet(self.invaders, [self.position[0] + 20, self.position[1] - 10])
        self.position = pos
        self.bullet.update()
        self.rect.topleft = self.position[0], self.position[1]

    def draw(self):
        pg.draw.rect(self.game.window, (255, 0, 255), pg.Rect(self.position[0], self.position[1], self.size, self.size))
