from Packet import Packet
from Segment import Segment
class Packet10RemoveSegment(Packet):
	def __init__(self,main, data):
		Packet.__init__(self, 10,data)
		self.main = main
	def process(self):
		id = int(self.data)
		self.main.removeSegment(id)
		self.main.segments.pop(id)

