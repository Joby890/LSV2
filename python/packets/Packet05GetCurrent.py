from Packet import Packet
class Packet05GetCurrent(Packet):
	def __init__(self,main, data):
		Packet.__init__(self, 02,data)
		self.main = main
	def process(self):
		idc = int(chr(self.data[0]))
		self.data.remove(self.data[0])
		string = self.main.segments[idc].getScript().getName()
		self.returnData = string

		