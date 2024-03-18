from extras.scripts import Script

def myblah(self):
	self.log_info("HELLO")
	return "hi"

class Test2(Script):
	class Meta:
		name = "other misc tests"
		commit_default = False
		scheduling_enabled = False

	def run(self, data, commit=True):
		self.log_info("hmm")
		myblah(self)
