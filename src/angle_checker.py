from Game import Game
from objects import Ball
from pygame.locals import *
from physics import to_rad
from math import pi

angle = None
g = Game(300,300,"Trig Checker")
g.fillscreen(Game.White)

ball = Ball((150,150),10,Game.Red)
ball.set_vector(0,2)

while True:
	for event in g.get_events():
		if g.is_quit(event.type):
			g.close()

		keys = g.get_pressed_keys()
		if keys[K_SPACE]:
			ball.set_vector(pi/2,2)
			ball.move()
		if keys[K_r]:
			ball.reset_pos()
	g.clear()
	ball.draw(g.screen)
	g.update() 
