

class Logger(object):
	def __init__(self):
		pass

	def update(self, EM, EQ):
		with open("debug.log", "a") as f:
			i = 0
			while EQ.can_get("debug", i):
				event = EQ.get("debug", i)
				i+=1
				f.write("%s\n"%event["text"])

