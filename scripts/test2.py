from extras.scripts import Script
from local.loctest import util_test

def myblah(self):
	self.log_info("HELLO")
	self.log_warning("yup")
	#ab = util_test(self)
	return "hi"

class Test2(Script):
	class Meta:
		name = "other misc tests"
		commit_default = False
		scheduling_enabled = False

	def run(self, data, commit=True):
		self.log_info("hmm")
		myblah(self)
