from Script import Script
class Cycle(Script):
	def __init__(self, main):
		Script.__init__(self, main,"Cycle")
		self.j = 0

	def next(self):
		if self.j >= 256:
			self.j = 0
		c = self.wheel((self.j) & 255)
		self.setAll(c.r,c.g,c.b)
		self.show()
		self.sleepMils(1)
		self.j += 3