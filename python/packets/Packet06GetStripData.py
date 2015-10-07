from Packet import Packet
class Packet06GetStripData(Packet):
	def __init__(self,main, data):
		Packet.__init__(self, 06,data)
		self.main = main
	def process(self):
		self.returnData += self.main.name + "," + self.main.version

		