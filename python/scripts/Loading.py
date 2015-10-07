from Script import Script
class Loading(Script):
	
	current = 0
	flash = False

	def __init__(self,main):
		Script.__init__(self, main,"loading")

	def next(self):
		if self.flash == False:
			if self.getLed(self.current) == None:
				self.flash = True
				return
			self.getLed(self.current).setColor(255,0,0)
			self.sleepMils(50)
			self.current = self.current + 1
		else:
			self.light(1000)
		self.show()
	def light(self, i):
		if i > 10:
			self.setAll(0,0,0)
			self.show()
			self.sleepMils(i)
			self.setAll(255,0,0)
			self.show()
			to = i * .75
			self.sleepMils(to)

			self.light(to)

		else:
			self.setAll(0,0,0)
			self.flash = False
			self.current = 0

	def stop(self):
		self.flash = False
		self.current = 0
		
		