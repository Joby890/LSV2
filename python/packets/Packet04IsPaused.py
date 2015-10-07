from Packet import Packet
class Packet04IsPaused(Packet):
	def __init__(self, main, data):
			Packet.__init__(self, 04, data)
			self.main = main
	def process(self):
		idc = int(chr(self.data[0]))
		self.returnData += "1" if self.main.segments[idc].isPaused() == True else "0"

