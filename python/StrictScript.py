from Script import Script
import time
class StrictScript(Script):
	

	def __init__(self, main, name, updatesPerSecond):
		Script.__init__(self, main,name)
		self.updatesPerSecond = updatesPerSecond
		self.last = self.getTime()
	def next(self):
		if self.getTime() - self.last > 1000.0 / self.updatesPerSecond:
			self.update()
			self.last = self.getTime()
		self.sleepMils(.5)

	def getTime(self):
		return float(time.time() * 1000)


