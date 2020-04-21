from Game import Game,getkey
from objects import Paddle,Ball
from pygame.locals import * #Use pygame key constants from here
from physics import check_bounds_paddles,check_bounds_ball,check_collisions,rand_dir,to_rad

# OBJECT SIZES
PADDLE_WIDTH = 30
PADDLE_HEIGHT = 145
PADDLE_PLAYER_X = 30
BALL_RADIUS = 10

# TODO handle keydown events, change how you listen for key presses in Game
def main():
	# CREATE A SCREEN AND ENTER GAME LOOP
	g = Game(800,600,"Pong Clone")
	g.fillscreen(Game.Black)
	g.set_keys_repeat(1)
	
	# GET SCREEN BOUNDS AND OTHER PARAMS
	BOUNDS = g.get_bounds()
	CEIL = BOUNDS[1] # Upper Y coordinate 0
	GROUND = BOUNDS[3]  # Lower Y coordinate 600
	LWALL = BOUNDS[0]
	RWALL = BOUNDS[2]
	CENTER = g.get_center()

	# OBJECT STARTING PARAMETERS
	PADDLE_CPU_X = BOUNDS[2] - PADDLE_WIDTH - PADDLE_PLAYER_X
	OFFSET = int(PADDLE_HEIGHT/2)
	PADDLE_Y = int(BOUNDS[3]/2) - OFFSET	

	# CREATE OBJECTS WITH STARTING SIZES AND PARAMETERS
	player = Paddle(PADDLE_PLAYER_X,PADDLE_Y,PADDLE_WIDTH,PADDLE_HEIGHT,Game.White)
	computer = Paddle(PADDLE_CPU_X,PADDLE_Y,PADDLE_WIDTH,PADDLE_HEIGHT,Game.White)
	ball = Ball(CENTER,BALL_RADIUS,Game.White)

	is_started = False
	while True:
		g.clear()
		for event in g.get_events():
			if g.is_quit(event.type):
				g.close()
		
		if is_started:
			ball.move()
		print(ball.vector)
		keys = g.get_pressed_keys()
		if keys[K_w]: player.move(0,-2)
		if keys[K_s]: player.move(0,2)
		if keys[K_UP]: computer.move(0,-2)
		if keys[K_DOWN]: computer.move(0,2)
		if keys[K_SPACE] and is_started == False:
			is_started = True
			ball.set_vector(rand_dir(),2)
		if keys[K_r] and is_started == True:
			is_started = False
			ball.reset_pos()

		# Draw before applying physics since a bound is only set when drawn
		player.draw(g.screen)
		computer.draw(g.screen)
		ball.draw(g.screen)
		ball.showbounds(g.screen)

		# physics
		check_bounds_paddles([player,computer],CEIL,GROUND)
		if is_started:
			check_bounds_ball(ball,LWALL,RWALL,CEIL,GROUND)
			check_collisions(ball,[player,computer])
	
		g.update()

if __name__ == '__main__':
	main()
