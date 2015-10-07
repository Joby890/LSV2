import os
import time
import thread
from neopixel import *
from Led import Led
from Segment import Segment
import glob

class Main(object):

	scripts = []
	segments = []
	strip = None
	pixels = []
	running = True
	commands = []
	server = None
	paused = False
	name = "Desk"
	version = "01"



	def start(self):
		self.addSegment(Segment(self, 9,120, "mid"))
		self.addSegment(Segment(self, 120,240, "end"))
		thread.start_new_thread(self.listenToInput, ())
		thread.start_new_thread(self.serverSetup, ())
		
		for x in range(0, 240):
			self.pixels.append(Led(self,x))

 		self.strip = Adafruit_NeoPixel(240, 18, 800000, 11, False, 255)
 		self.strip.begin()
 		self.strip.show()
 		self.loadSceiptsNew("");
		#self.loadScripts("./scripts")

		self.loadPackets("./packets")
		self.segments[0].setScript(self.scripts[8])


		self.strip.setPixelColorRGB(120, 250,0,0)
		self.strip.show()
		print self.scripts
		print len(self.scripts)
		#print("starting..")
		while self.running:
			try:
				self.sleep(1)

			except KeyboardInterrupt:
				self.running = False
				print("Stop running")
			except:
				print("Error Caught")
				raise
		#self.server.shutdown()

	def serverSetup(self):
		from LedServer import LedServer
		from LedServer import LedServerHandler
		server = LedServer(("192.168.1.235", 13373), LedServerHandler,self)
		server.serve_forever()
	def proccessRequest(self, packet, data):
		import sys
		sys.path.insert(0, "./packets")
		from Packet00UploadFile import Packet00UploadFile
		from Packet01SetScript import Packet01SetScript
		from Packet02GetScripts import Packet02GetScripts
		from Packet03SetPaused import Packet03SetPaused
		from Packet04IsPaused import Packet04IsPaused
		from Packet05GetCurrent import Packet05GetCurrent
		from Packet06GetStripData import Packet06GetStripData
		from Packet07GetSegments import Packet07GetSegments
		from Packet08ReAddSegment import Packet08ReAddSegment
		from Packet09ChangeSegment import Packet09ChangeSegment
		from Packet10RemoveSegment import Packet10RemoveSegment
		from Packet11ChangeOptions import Packet11ChangeOptions
		from Packet12GetOptions import Packet12GetOptions
		p = None
		
		packet = int(packet)
		if(packet == 0):
			p = Packet00UploadFile(self, data)
			p.process()
		if packet == 1:
			p = Packet01SetScript(self,data)
			p.process()
		if packet == 2:
			p = Packet02GetScripts(self,data)
			p.process()
		if packet == 3:
			p = Packet03SetPaused(self, data)
			p.process()
		if packet == 4:
			p = Packet04IsPaused(self, data)
			p.process()
		if packet == 5:
			p = Packet05GetCurrent(self, data)
			p.process()
		if packet == 6:
			p = Packet06GetStripData(self, data)
			p.process()
		if packet == 7:
			p = Packet07GetSegments(self, data)
			p.process()
		if packet == 8:
			p = Packet08ReAddSegment(self, data)
			p.process()
		if packet == 9:
			p = Packet09ChangeSegment(self, data)
			p.process()
		if packet == 10:
			p = Packet10RemoveSegment(self, data)
			p.process()
		if packet == 11:
			p = Packet11ChangeOptions(self, data)
			p.process()
		if packet == 12:
			p = Packet12GetOptions(self, data)
			p.process()
		return p
		
	def addSegment(self, segment):
		self.segments.append(segment)
		thread.start_new_thread(self.proccessSegment, (segment,))
	def removeSegment(self, seg):
		self.segments[seg].running = False
	def proccessSegment(self, seg):
		while self.running and seg.running:
			seg.update()

	def setPixel(self,n,r,g,b):
		self.strip.setPixelColorRGB(n,r,g,b)
	def setPixelColor(self,n, c):
		self.strip.setPixelColor(n,Color(c.r, c.g, c.b))

	def show(self):
		self.strip.show()

	def sleep(self, mils):
		i = float(mils) / 1000.0
		time.sleep(i)

	def getNumPixels(self):
		return self.strip.numPixels()

	def listenToInput(self):

		from EndCommand import EndCommand
		self.commands.append(EndCommand(self))

		from ScriptCommand import ScriptCommand
		self.commands.append(ScriptCommand(self))

		while self.running == True:
			quick = raw_input("")
			self.proccessCommand(quick)
	def getScript(self, name):
		for script in self.scripts:
			if script.getName() == name:
				return script
	#Depricated
	def setScript(self, script):
		if self.segments[0].getScript() != None:
			self.segments[0].getScript().stop()
		self.segments[0].setScript(script)
	def loadSceiptsNew(self, dir):
		scripts = glob.glob("./scripts/*.py")
		for x in range(len(scripts)):
			self.loadScript(os.path.basename(scripts[x]).split(".")[0])

	def loadScript(self, name):
		if self.getScript(name) != None:
			self.scripts.remove(self.getScript(name))
		import sys
		sys.path.insert(0, "./scripts")
		import importlib
		i = importlib.import_module(name)
		class_ = getattr(i, name)
		instance = class_(self.segments[0])
		self.scripts.append(instance)

	def proccessCommand(self, quick):

		args = quick.split(" ")
		if len(args) >= 0:
				label = args[0]
				args.remove(args[0])
				b = False
				for command in self.commands:
					re = command.onCommand(label, args)
					b = b or re
				if b == False:
					print("Unknow command")
				return b

	def loadScripts(self, dir):
		import sys
		sys.path.insert(0, "./scripts")
		from Script import Script
		s = Script(self,"test")
		from loading import Loading
		l = Loading(self.segments[0])
		self.scripts.append(l)
		from TheaterChase import TheaterChase
		t = TheaterChase(self.segments[0])
		self.scripts.append(t)
		from rainbow import Rainbow
		r = Rainbow(self.segments[0])
		self.scripts.append(r)
		from LeftToRightRandom import LeftToRightRandom
		lr = LeftToRightRandom(self.segments[0])
		self.scripts.append(lr)
		from RandomLed import RandomLed
		r = RandomLed(self.segments[0])
		self.scripts.append(r)
		from Light import Light
		self.scripts.append(Light(self.segments[0]))
		from Test import Test
		self.scripts.append(Test(self.segments[0]))
		from Cycle import Cycle
		self.scripts.append(Cycle(self.segments[0]))
		from SingleColor import SingleColor
		self.scripts.append(SingleColor(self.segments[0]))

	def loadPackets(self, dir):
		import sys
		sys.path.insert(0, "./packets")
		from Packet00UploadFile import Packet00UploadFile









main = Main()
main.start()