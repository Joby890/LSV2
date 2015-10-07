from Script import Script
class Light(Script):
	pos = 10
	def __init__(self, main):
		Script.__init__(self, main, "Light")

	def next(self):
		self.setAll(0,0,0)
		for x in range(self.pos - 10, self.pos + 10):
			self.getLed(x).setColor(255,255,255)
		self.show()
		self.sleep(3)
		self.pos = self.pos + 10

		if self.getLed(self.pos + 10) == None:
			self.pos = 10

