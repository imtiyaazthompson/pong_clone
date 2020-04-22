from Game import Rect,Circle
from physics import rand_dir,to_cartesian,to_rad
from math import sqrt

# TODO Implement Vector movement for paddles
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

# TODO change base classes to hold coordinates as list []
class Ball(Circle):

	def __init__(self,center,radius,color,point):
		super().__init__(center,radius,color)
		
		# Vector init to center coordinates of ball
		self.vector = Vector2D(point[0],point[1])
		self.reset = center

	# AI movement, therefore no dx,dy as params
	def move(self):
		x = self.center[0]
		dx = self.vector.getx()
		y = self.center[1]
		dy = self.vector.gety()
		self.center = (x+dx,y+dy)


	def alter_speed(self,value):
		self.vector.scalar_product(value)

	def set_vector(self,x,y):
		self.vector = Vector2D(x,y)
		self.alter_speed(10)

	def reset_pos(self):
		self.center = self.reset

# TODO Refactor into more understandable
# A vector is used to capture the magnitude (speed)
# and direction by which a rigid body is travelling
# Vector[dx*speed,dy*speed] -> think of this representing a velocity vector
# An object will have it current x,y coordinates and those coordinates change overtime
# By the velocity vector, since velocity is change in position over time
# So the magnitude is the speed, which can be modified with scalar product
class Vector2D:

	# For a point in the xy plane: origin=tail, point=head
	def __init__(self,x,y):
		# Y values are positive moving downwards
		self.vector = [x,y]

	def add(self,vector):
		self.vector[0] += vector[0]
		self.vector[1] += vector[1]

	def scalar_product(self,k):
		self.vector[0] *= k
		self.vector[1] *= k

	# Speed
	def get_magnitude(self):
		return sqrt(self.vector[0]**2 + self.vector[1]**2)
		

	def inc_x(self,value):
		self.vector[0] += value

	def inc_y(self,value):
		self.vector[1] += value

	def mulx(self,value):
		self.vector[0] *= value

	def muly(self,value):
		self.vector[1] *= value

	def get_pos(self):
		return (self.vector[0],self.vector[1])

	def getx(self):
		return self.vector[0]

	def gety(self):
		return self.vector[1]
