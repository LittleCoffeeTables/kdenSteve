#system_movement.py

class Movement(object):
	def __init__(self):
		#self.__EM = entityManager
		pass

	def update(self, EM, EQ):
		i = 0
		while EQ.can_get("move", i):
			event = EQ.get("move", i)
			i += 1
			self.move(EM, EQ, event["eid"], event["dir"])

	def move(self, EM, EQ, eid, dir_):
		if not EM.has_prop(eid, "p_pos"):
			return False
		pos = EM.get_value(eid, "p_pos")
		new_pos = (pos[0]+dir_[0], pos[1]+dir_[1])
		if EM.has_prop(eid, "physical"):
			for other in (
			 EM.get_by_props(["physical", "p_pos"])):
				if other == eid:
					continue
				if new_pos == EM.get_value(other, "p_pos"):
					return False
		pos[0] = new_pos[0]; pos[1] = new_pos[1]
		if EM.has_prop(eid, "r_pos"):
			r_pos = EM.get_value(eid, "r_pos")
			r_pos[0] = pos[0]; r_pos[1] = pos[1]
		if EM.has_prop(eid, "camera"):
			EQ.put("move_camera",
					{"to":tuple(pos)})
		
		return True

