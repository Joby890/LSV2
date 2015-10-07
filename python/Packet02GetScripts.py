from Packet import Packet
class Packet02GetScripts(Packet):
	def __init__(self,main, data):
		Packet.__init__(self, 02,data)
		self.main = main
	def process(self):
		string = self.main.scripts[0].getName()
		for i in range(1, len(self.main.scripts)):
			string += "," + self.main.scripts[i].getName()
		self.returnData += string

		