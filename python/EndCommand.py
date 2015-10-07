from Command import Command
class EndCommand(Command):
	"""docstring for EndCommand"""
	def __init__(self, main):
		Command.__init__(self, main)

	def onCommand(self, label, args):
		if(label == "end"):
			print("Shutting Down")
			self.main.running = False
			return True
		return False
		