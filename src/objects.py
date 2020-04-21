from Game import Rect,Circle
from physics import rand_dir,to_cartesian,to_rad

# Inherit methods from Shape -> Rect
class Paddle(Rect):

	def __init__(self,x,y,w,h,color):
		super().__init__(x,y,w,h,color)

	def move(self,dx,dy):
		self.left += dx
		self.top += dy
		# NOTE when a paddle is moved and drawn, its bounds is updated

	def set(self,x,y):
		self.left = x
		self.top = y

	def collides_with(self,rect):
		return self.bounds.colliderect(rect.bounds)

class Ball(Circle):

	def __init__(self,center,radius,color):
		super().__init__(center,radius,color)
		
		# Store the direction of last movement
		self.vector = None
		self.reset = center

	# Randomly move by dr in direction self.theta
	def move(self):
		angle = self.vector[0]
		speed = self.vector[1]
		dx,dy = to_cartesian(speed,angle)
		x,y = self.center
		self.center = (x+dx,y+dy)

	def set(self,pos):
		self.center = pos

	def reverse(self):
		self.speed *= -1

	def set_vector(self,angle,speed):
		self.vector = (angle,speed)

	def mod_vector(self,amod,smod):
		angle,speed = self.vector
		self.vector = (angle+amod,speed+smod)

	def reset_pos(self):
		self.center = self.reset
