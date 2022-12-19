import pygame as pg
from models import Plane, Bullet

def main():
    """Entry point and start the game"""
    pg.init()
    FPS = 30
    CLOCK = pg.time.Clock()

    window = pg.display.set_mode((1000, 800))
    pg.display.set_caption("Space Invaders")
    plane = Plane("King", 300)
    # bullet = Bullet([plane.position[0] + 20, plane.position[1] - 10])
    bullets = [Bullet([plane.position[0] + 20, plane.position[1] - 10])]
    running = True
    while running:
        window.fill((255, 255, 255))
        pg.draw.rect(window, (255, 0, 255), pg.Rect(plane.position[0], plane.position[1], plane.size, plane.size))
        for bullet in bullets:
            pg.draw.rect(window, (255, 0, 0), pg.Rect(bullet.position[0], bullet.position[1], bullet.size, bullet.size))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        key_input = pg.key.get_pressed()
        if key_input[pg.K_LEFT]:
            plane.position[0] -= 10
        elif key_input[pg.K_RIGHT]:
            plane.position[0] += 10

        bullet.position[1] -= 5
        if bullet.position[1] < 500:
            if len(bullets) > 0:
                bullets.pop()
            bullets.append(Bullet([plane.position[0] + 20, plane.position[1] - 10]))

        pg.display.update()
        CLOCK.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
