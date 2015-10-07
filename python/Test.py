from Script import Script
class Test(Script):
	
	def __init__(self,main):
		Script.__init__(self,main,"Test")
	def next(self):
		self.setAll(255,0,0)
		self.show()
		self.sleep(1)
		self.setAll(0,255,0)
		self.show()
		self.sleep(1)
		self.setAll(0,0,255) 
		self.show()
		self.sleep(1)