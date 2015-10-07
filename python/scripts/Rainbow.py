from Script import Script
class Rainbow(Script):
	def __init__(self, main):
		Script.__init__(self, main,"Rainbow")


	def next(self):
		for j in range(256):
				for i in range(self.segment.getNum()):
					self.getLed(i).setColor(self.wheel((i+j) & 255))
				self.show()
				self.sleepMils(1)
		