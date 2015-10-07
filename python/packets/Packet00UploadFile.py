from Packet import Packet
import os
class Packet00UploadFile(Packet):
	def __init__(self, main, data):
		Packet.__init__(self, 00, data)
		self.main = main

	def process(self):
		idc = int(chr(self.data[0]))
		self.data.remove(self.data[0])
		print idc

		name = ""
		for i in range(0, idc):
			a = chr(self.data[0])
			name += a
			self.data.remove(self.data[0])
		print name.strip()
		print os.path.abspath("./scripts/" + name.strip())
		if os.path.exists("./scripts/" + name.strip()):
			print "Removing"
			os.remove("./scripts/" + name.strip())
		print os.path.abspath("./scripts/" + name.strip() + "c")
		if os.path.exists("./scripts/" + name.strip() + "c"):
			print "Removing2"
			os.remove("./scripts/" + name.strip() + "c")
		f = open("./scripts/" + name, "wb")
		print f
		f.write(self.data)
		f.close()
		print self.data
		self.main.loadScript(name.split(".")[0])

