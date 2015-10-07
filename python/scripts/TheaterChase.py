from Script import Script
class TheaterChase(Script):
	def __init__(self, main):
		Script.__init__(self, main,"TheaterChase")

	def next(self):
		for q in range(3):
			for i in range(0, self.segment.getNum(), 3):
				l = self.getLed(i+q)
				if l != None:
					l.setColor(255,255,255)
			self.show()
			self.sleepMils(50)
			for i in range(0, self.segment.getNum(), 3):
				l = self.getLed(i+q)
				if l != None:
					l.setColor(0,0,0)
		
