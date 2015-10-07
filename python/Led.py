from Color import Color
class Led(object):
	def __init__(self, main, num):
		super(Led, self).__init__()
		self.num = num
		self.main = main

	def getSpot(self):
		return self.num
	def getNum(self):
		return self.num
	#def setColorPixel(self, col):
	#	print("Called 1")
	#	self.main.setPixel(self.num, col.r, col.g, col.b)
	def setColor(self, r,g = None,b = None):
		if isinstance(r, Color) == True:
			self.main.setPixel(self.num, r.r,r.g,r.b)
			return
		self.main.setPixel(self.num, r,g,b)
		