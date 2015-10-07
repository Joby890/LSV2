from Packet import Packet
class Packet03SetPaused(Packet):
	def __init__(self, main,data):
		Packet.__init__(self,03,data)
		self.main = main
	def process(self):
		idc = int(chr(self.data[0]))
		self.data.remove(self.data[0])
		b = int(self.getString(self.data))
		if b == 0:
			self.main.segments[idc].setPaused(False)
		else:
			self.main.segments[idc].setPaused(True)
