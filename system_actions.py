#system_actions

class Actions(object):
	def __init__(self):
		pass

	def new_turn(self, EM, EQ):
		# do not run AI, but tick the every-turn things
		EM.clear_prop("attacked_this_turn")
		#for e in EM.get_by_props([]):
		#	EM.set_value(e, "stuck_counter", 0)
		for e in EM.get_by_props(["ap", "max_ap"]):
			ap = EM.get_value(e, "ap")
			max_ap = EM.get_value(e, "max_ap")
			if ap < 1:
				EM.set_value(e, "ap", max_ap)
			EM.set_value(e, "stuck_counter", 0)


	def update(self, EM, EQ):
		for e, ap in EM.get_prop("ap").items():
			if ap > 0:
				return
		self.new_turn(EM, EQ)
		EQ.put("new_turn", {})
		

