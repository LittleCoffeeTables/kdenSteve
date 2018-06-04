#system_corpses

class Corpses(object):
	def __init__(self):
		pass

	def update(self, EM, EQ):
		maybe_new_corpses = EM.get_by_props(["p_pos", "health"])
		for e in maybe_new_corpses:
			if EM.get_value(e, "health") <= 0:
				pos = EM.get_value(e, "p_pos")
				if EM.has_prop(e, "blood"):
					EM.set_value(pos, "bloody", True)
				if EM.has_prop(e, "gibbed"):
					EM.rm_entity(e)
					continue
				EM.set_value(e, "r_char", "%")
				EM.edit_value(e, "r_prio", multi=0.04)
				EM.rm_value(e, "physical", noerror=True)
				EM.rm_value(e, "health")
