#! /usr/bin/python3

import sys
from settings import *
from invaders import Invaders

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Space Invaders")
        self.window = pg.display.set_mode(FIELD_SIZE)
        self.CLOCK = pg.time.Clock()
        self.plane_pos = [400, 700]
        self.invaders = Invaders(self)
    
    def update(self):
        self.invaders.update(self.plane_pos)
        self.CLOCK.tick(FPS)

    def draw(self):
        self.window.fill(color=(48, 39, 32))
        self.invaders.draw()
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        key_input = pg.key.get_pressed()
        if key_input[pg.K_LEFT]:
            self.plane_pos[0] -= 10
        elif key_input[pg.K_RIGHT]:
            self.plane_pos[0] += 10

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
