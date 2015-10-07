from Packet import Packet
class Packet07GetSegments(Packet):
	def __init__(self,main, data):
		Packet.__init__(self, 07,data)
		self.main = main
	def process(self):
		string = "";
		for x in range(len(self.main.segments)):
			seg = self.main.segments[x]
			if seg.script != None:
				string += str(x) + "," + str(seg.paused) + "," + str(seg.start) + "," + str(seg.end) + "," + seg.name + "," +seg.script.getName() +  ":"
			else:
				string += str(x) + "," + str(seg.paused) + "," + str(seg.start) + "," + str(seg.end) + "," + seg.name + "," +"None" +  ":"			
		self.returnData += str(string)

		