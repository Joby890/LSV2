from Packet import Packet
from ScriptOptions import ScriptOption
class Packet11ChangeOptions(Packet):
	def __init__(self, main, data):
			Packet.__init__(self, 11, data)
			self.main = main
			self.data = data
	def process(self):
		try:
			name = self.data["name"]
			for x in range(0, len(self.data["options"])):
				optionname = self.data["options"][x]["name"]
				optiontype = self.data["options"][x]["type"]
				optionvalue = self.data["options"][x]["value"]
				optionoptions = self.data["options"][x]["options"]
				option = ScriptOption(optionname, optiontype, optionvalue, optionoptions)
				self.main.getScript(name).options[x] = (option)
		except Exception, e:
			print "Exception wile processing P2: ", e
			raise e


