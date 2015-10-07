from Command import Command
class ScriptCommand(Command):
	def __init__(self, main):
		Command.__init__(self, main)

	def onCommand(self, label, args):
		if label == "script":
			if len(args) >= 2:
				if args[0] == "set":
					s = self.main.getScript(args[1])
					if s == None:
						print("Unknow Script")
					else:
						print("Setting Script to " + args[1])
						self.main.setScript(s)