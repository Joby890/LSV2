from Script import Script
from Color import Color
import random


class PColor(object):

	def __init__(self, segment, c):
		self.pixel = int(random.uniform(0, segment.getNum()))
		self.c = c
		self.dir = True

class LeftToRightRandom(Script):

	

	def __init__(self, main):
		Script.__init__(self, main,"LeftToRightRandom")
		self.colors = []#[PColor(main,Color(255,0,0))]
		#for x in range(0, 1):
		#	self.colors.append(PColor(main,self.randomColor()))

	def next(self):
		if len(self.colors) == 0:
			p = PColor(self.segment,Color(255,0,0))
			p.pixel = 0
			self.colors.append(p)
		for c in self.colors:
			self.getLed(c.pixel).setColor(0,0,0)
			if c.dir == True:
				c.pixel = c.pixel - 1
				if self.getLed(c.pixel) == None:
					c.dir = False
					c.pixel = c.pixel + 1
					if int(random.uniform(0,2)) == 1:
						self.colors.remove(c)
					
			else:
				c.pixel = c.pixel + 1
				if self.getLed(c.pixel) == None:
					c.dir = True
					c.pixel = c.pixel - 1
					if int(random.uniform(0,2)) == 1:
						self.colors.append(PColor(self.segment,self.randomColor()))
					
			self.getLed(c.pixel).setColor(c.c.r,c.c.g,c.c.b)
		self.sleepMils(7)	
		self.show()



		