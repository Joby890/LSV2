from Packet import Packet
class Packet12GetOptions(Packet):
	def __init__(self,main, data):
		Packet.__init__(self, 12,data)
		self.main = main
		self.data = data
	def process(self):
		name = self.data
		print(name)
		data = []
		options = self.main.getScript(name).options
		for x in range(0, len(options)):
			data.append({"name":options[x].name,"type":options[x].type,"value":options[x].value, "options":options[x].options})
		self.returnData = data

