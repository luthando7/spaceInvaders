from settings import *

class Enemy(pg.sprite.Sprite):
    def __init__(self, invaders: object, pos: list):
        super().__init__(invaders.sprite_group)
        self.size = 50
        self.invaders = invaders
        self.image = pg.Surface([self.size, self.size])
        self.image.fill('red')
        self.position = pos
        self.strength = 4

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position[0], self.position[1]

    def update(self, pos):
        self.position  = pos
        self.rect.topleft = self.position[0], self.position[1]

    def update_strength(self):
        self.strength -= 1
        if self.strength < 1:
            self.kill();


    def draw(self):
        pg.draw.rect(self.game.window, (255, 125, 255), pg.Rect(self.position[0], self.position[1], self.size, self.size))