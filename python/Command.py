class Command(object):

	def __init__(self, main):
		self.main = main

	def onCommand(self):
		raise NotImplementedError("Please Implement onCommand")
