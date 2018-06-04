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
			e = event["eid"]
			if not self.move(EM, EQ, e, event):
				if not EM.has_prop(e, "stuck_counter"):
					EM.set_value(e, "stuck_counter", 1)
				else:
					EM.edit_value(e,
						"stuck_counter", add=1)
				if EM.get_value(e, "stuck_counter") > 2:
					EM.edit_value(e, "ap", add=-1)

	def move(self, EM, EQ, eid, event):
		if not EM.has_prop(eid, "p_pos"):
			return False
		pos = EM.get_value(eid, "p_pos")
		if "dir" in event:
			new_pos = (pos[0]+event["dir"][0],
				   pos[1]+event["dir"][1])
		elif "to" in event:
			new_pos = event["to"]
		else:
			raise ValueError("No dir or to in event: %s"%event)
		if EM.has_prop(eid, "physical"):
			for other in (
			 EM.get_by_props(["physical", "p_pos"])):
				if other == eid:
					continue
				if new_pos == EM.get_value(other, "p_pos"):
					return False
		#pos[0] = new_pos[0]; pos[1] = new_pos[1]
		EM.set_value(eid, "p_pos", new_pos)
		cost = 1 #TODO
		if EM.has_prop(eid, "ap"):
			EM.edit_value(eid, "ap", add=-cost)
		if EM.has_prop(eid, "r_pos"):
			#r_pos = EM.get_value(eid, "r_pos")
			#r_pos[0] = pos[0]; r_pos[1] = pos[1]
			EM.set_value(eid, "r_pos", new_pos)
		if EM.has_prop(eid, "camera"):
			EQ.put("move_camera",
					{"to":tuple(new_pos)})
		
		return True

