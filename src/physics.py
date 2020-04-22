# A physics library for my pong clone
from math import sin,cos,pi
from Game import rand

# TODO bug fix scummy moves

def check_bounds_paddles(paddles,ceiling,ground):
	for paddle in paddles:
		if paddle.top <= ceiling:
			paddle.set(paddle.left,0)
		elif (paddle.top + paddle.h) >= ground:
			paddle.set(paddle.left,ground - paddle.h)

def check_bounds_ball(ball,lwall,rwall,ceiling,ground):
	if (ball.getx()-ball.r) <= lwall:
		# game over for player_1
		ball.reset_pos()	
	elif (ball.getx()+ball.r) >= rwall:
		# game over for player_2
		ball.reset_pos()
	elif (ball.gety()-ball.r) <= ceiling:
		# bounce ball
		process_wallbounce(ball.vector)
	elif (ball.gety()+ball.r) >= ground:
		# bounce ball
		process_wallbounce(ball.vector)

def check_collisions(ball,players):
	for player in players:
		if player.collides_with(ball):
			process_paddle_bounce(ball.vector)

# dr is the change in r over time
# particle travels r per second (vel)
# theta is assumed to be in radians
def to_cartesian(r,theta):
	dx = r * cos(theta)
	dy = r * sin(theta)

	return (int(dx),int(dy))

def to_rad(deg):
	return (deg*pi)/180.0

def to_deg(rad):
	return (rad*180.0)/pi

def rand_dir(constraint=360):
	return to_rad((rand() * constraint))

def process_wallbounce(vector):
	# make dy the opposite
	vector.muly(-1)

# Headache to solve
def process_paddle_bounce(vector):
	# make dx opposite
	vector.mulx(-1)
