from Packet import Packet
from Segment import Segment
import thread
class Packet08ReAddSegment(Packet):
	def __init__(self,main, data):
		Packet.__init__(self, 8,data)
		self.main = main
	def process(self):
		start = self.data.split(",")[0]
		end = self.data.split(",")[1]

		segment = Segment(self.main,start,end,self.getString(self.data.split(",")[2]))
		self.main.segments.append(segment)
		thread.start_new_thread(self.main.proccessSegment, (segment,))

