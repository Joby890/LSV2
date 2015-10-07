from Color import Color
import random
class Script(object):
	def __init__(self, segment, name):
		self.name = name
		self.segment = segment
		self.options = [];
	
	def setSegment(self, segment):
		self.segment = segment

	def getName(self):
		return self.name

	def sleepMils(self, mils):
		self.segment.sleep(mils)

	def sleep(self, secs):
		self.segment.sleep(secs * 1000)

	def getLed(self, num):
		return self.segment.getLed(num)
	def setAll(self, c):
		return self.segment.setAll(c)

	def setAll(self, r,g,b):
		return self.segment.setAll(r,g,b)
	def show(self):
		self.segment.show()

	def next(self):
		raise NotImplementedError("Please Implement next")
	def stop(self):
		self.setAll(0,0,0)
	def wheel(self, pos):
		if pos < 85:
			return Color(pos * 3, 255 - pos * 3, 0)
		elif pos < 170:
			pos -= 85
			return Color(255 - pos * 3, 0, pos * 3)
		else:
			pos -= 170
			return Color(0, pos * 3, 255 - pos * 3)
	def randomColor(self):
		c = Color(int(random.uniform(0,255)),int(random.uniform(0,255)),int(random.uniform(0,255)))
		#print c.r
		return c
	def getOption(self,index):
		return self.options[index].value