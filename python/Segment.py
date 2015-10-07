class Segment(object):
	def __init__(self, main, start, end, name):
		self.main = main
		self.paused = False
		self.start = int(start)
		self.end = int(end)
		self.script = None
		self.running = True
		self.name = name

	def getNum(self):
		return self.end - self.start

	def getScript(self):
		return self.script

	def setScript(self, script):
		script.setSegment(self)
		self.script = script

	def update(self):
		if self.isPaused() == False:
			if self.getScript() != None:
				self.getScript().next()
		else:
			self.sleepMils(1)

	def isPaused(self):
		return self.paused
	def setPaused(self, paused):
		self.paused = paused


	def sleepMils(self, mils):
		self.main.sleep(mils)

	def sleep(self, secs):
		self.main.sleep(secs)
		

	def getLed(self, num):
		if num >= self.end - self.start:
			return None
		if num < 0:
			return None
		return self.main.pixels[num + self.start]
		for x in range(0, self.main.getNumPixels()):
			p = self.main.pixels[x]
			if p.num == num + self.start:
				return p
	def setAll(self, c):
		for x in range(0, self.getNum()):
			self.getLed(x).setColor(c)

	def setAll(self, r,g,b):
		for x in range(0, self.getNum()):
			self.getLed(x).setColor(r,g,b)
	def show(self):
		self.main.show()