# A physics library for my pong clone
from math import sin,cos,pi
from Game import rand

# TODO bugfix bounces at 180, 0 and 90 degrees
# TODO bugfix scummy moves on side

def check_bounds_paddles(paddles,ceiling,ground):
	for paddle in paddles:
		if paddle.top <= ceiling:
			paddle.set(paddle.left,0)
		elif (paddle.top + paddle.h) >= ground:
			paddle.set(paddle.left,ground - paddle.h)

def check_bounds_ball(ball,lwall,rwall,ceiling,ground):
	angle = ball.vector[0]
	if (ball.center[0]-ball.r) <= lwall:
		# game over for player_1
		ball.reset_pos()	
	elif (ball.center[0]+ball.r) >= rwall:
		# game over for player_2
		ball.reset_pos()
	elif (ball.center[1]-ball.r) <= ceiling:
		# bounce ball
		a = process_wallbounce_top(ball.vector[0])
		ball.set_vector(a,2)
	elif (ball.center[1]+ball.r) >= ground:
		# bounce ball
		a = process_wallbounce_bottom(ball.vector[0])
		ball.set_vector(a,2)

def check_collisions(ball,players):
	for player in players:
		if player.collides_with(ball):
			a = process_paddle_bounce(ball.vector[0])
			ball.set_vector(a,2)

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

def process_wallbounce_top(angle):
	angle %= 2*pi
	angle *= -1
	return angle

def process_wallbounce_bottom(angle):
	angle %= 2*pi
	angle *= -1
	return angle

# Headache to solve
# But works for both paddles - A general solution
def process_paddle_bounce(angle):
	angle %= 2*pi
	angle *= -1
	angle += 2*pi
	angle = pi - angle
	angle *= -1
	return angle
