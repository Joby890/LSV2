from StrictScript import StrictScript
import time
class Test(StrictScript):

	def __init__(self, main):
		StrictScript.__init__(self,main,"Test",10)
		self.our = time.time() * 1000
		self.updates = 0
		self.current = 0
	

	def update(self):
		self.getLed(self.current).setColor(0,255,0)
		self.show()
		if self.getTime() - self.our >= 1000 * 10:
			print("We had this many updates: " + str(self.updates))
			self.updates = 0
			self.our = self.getTime()
			#self.setAll(0,0,0)
		if self.getLed(self.current + 1) == None:
			self.current = 0
			self.setAll(0,0,0)
		self.current = self.current + 1
		self.updates = self.updates + 1