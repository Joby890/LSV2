from Script import Script
import random
class RandomLed(Script):
	def __init__(self, main):
		Script.__init__(self, main,"Random")

	def next(self):
		c = self.randomColor()
		i = random.uniform(0,self.segment.getNum() - 1)
		self.getLed(int(i)).setColor(int(c.r),int(c.g),int(c.b))
		self.show()
		self.sleepMils(1)

		