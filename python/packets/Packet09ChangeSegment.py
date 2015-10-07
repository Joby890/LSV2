from Packet import Packet
from Segment import Segment
class Packet09ChangeSegment(Packet):
	def __init__(self,main, data):
		Packet.__init__(self, 9,data)
		self.main = main
	def process(self):
		print(self.data)
		string = self.data.split(",")
		segment = self.main.segments[int(string[0])]
		print(segment)
		segment.start = int(string[1])
		segment.end = int(string[2])
		segment.name = string[3]
