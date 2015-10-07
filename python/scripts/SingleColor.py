from Script import Script
from ScriptOptions import ScriptOption
class SingleColor(Script):
	pos = 10
	def __init__(self, main):
		Script.__init__(self, main, "SingleColor")
		self.options.append(ScriptOption("color", "colorpicker","150,0,150",[]))

	def next(self):
		c = self.getOption(0).split(",")
		self.setAll(int(c[0]),int(c[1]),int(c[2]))
		self.show()
		self.sleepMils(1)