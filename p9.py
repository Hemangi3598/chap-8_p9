''' class circlle: radius
		__init__(), show(), area(), cicum() '''

class circle:
	def __init__(self, radius):
		self.radius = radius
	def show(self):
		print("radius = ", self.radius)
	def area(self):	
		ans = 3.1459 * self.radius ** 2
		print("ans = ", round(ans, 2))
	def circum(self):
		ans = 2 * 3.1459 * radius
		print("ans = ", round(ans,2))

radius = float(input(" enter radius "))
c = circle(radius)
c.show()
c.area()
c.circum()

		