from settings import *
class Bullet(pg.sprite.Sprite):
    def __init__(self, invaders, position):
        super().__init__(invaders.sprite_group)
        self.position = position
        self.invaders = invaders
        self.size = 10
        self.image = pg.Surface([self.size, self.size])
        self.image.fill('red')

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position[0], self.position[1]

    def update(self):
        self.position[1] -= 10
        if self.position[1] < 0:
            self.kill()
        self.rect.topleft = self.position[0], self.position[1]

    def draw(self):
        pg.draw.rect(self.game.window, (255, 0, 255), pg.Rect(self.position[0], self.position[1], self.size, self.size))
