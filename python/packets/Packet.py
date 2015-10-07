class Packet(object):
	def __init__(self, packetId, data):
		self.packetId = packetId
		self.data = data
		self.returnData = ""

	def process(self):
		raise NotImplementedError("Please Implement process")
	
	def getString(self,data):
		string = ""
		for st in range(0, len(data)):
			string += chr(data[st])
		return string
	def returnString(self):
		return self.returnData