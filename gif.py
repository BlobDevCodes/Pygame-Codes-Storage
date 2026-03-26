import pygame as pg
import sys
import gif_pygame as gpg

pg.init()

gif = gpg.load("tenor-2663287124.gif")

screen = pg.display.set_mode((498, 331))
print (gif.width, gif.height)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    gif.render(screen, dest=(0, 0))
    pg.display.flip()
