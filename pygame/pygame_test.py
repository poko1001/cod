#-*- coding: utf-8 -*-
import pygmae

pygmae.int()
screen = pygmae.display.set_mode((600.800))
clock = pygmae.time.clock()



while True:
    screen.fill((0,0,0))



    event.type == pygmae.QUIT:
    break


    pygmae.display.update()
    clock.tick(30)

pygmae.quit()