from Packet import Packet
import os
import sys
class Packet01SetScript(Packet):
	def __init__(self, main, data):
		Packet.__init__(self,01,data)
		self.main = main

	def process(self):
		try:
			print(self.data[0])
			idc = int(chr(self.data[0]))
			self.data.remove(self.data[0])
			name = self.getString(self.data)
			#name = os.path.splitext(name)[0]
			s = self.main.getScript(name)
			if s == None:
				#Attempt to load script
				self.main.loadScript(name)
				s = self.main.getScript(name)
			if s != None:
				#if name is now loaded set it
				self.main.segments[idc].setScript(s)
		except Exception, e:
			print "Exception wile processing Packet: ", e
			print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
		