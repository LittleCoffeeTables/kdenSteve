#system_actions

class Actions(object):
	def __init__(self):
		pass

	def update(self, EM, EQ):
		for e, ap in EM.get_prop("ap").items():
			if ap > 0:
				return
		for e in EM.get_by_props(["ap", "max_ap"]):
			ap = EM.get_value(e, "ap")
			max_ap = EM.get_value(e, "max_ap")
			if ap < 1:
				EM.set_value(e, "ap", max_ap)



