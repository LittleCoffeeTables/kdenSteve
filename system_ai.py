#system_ai

class AI(object):
	def __init__(self):
		pass

	def update(self, EM, EQ):
		#if EM.get_value(self.__player_id, "ap", 1) > 0:
		#	#do not do AI moves while player has actions remaining
		#	return
		for e in EM.get_by_props(["p_pos","ap"]):
			ap = EM.get_value(e, "ap")
			if ap < 1:
				continue
			if not EM.has_prop(e, "ai"):
				break
			ai = EM.get_value(e, "ai")
			pos = EM.get_value(e, "p_pos")
			target = EM.get_value(e, "target")
			if target is None:
				#TODO: idle ai
				continue
			target_pos = EM.get_value(target, "p_pos")
			if target_pos is None:
				continue

			if ai == "orc":
				self.move_towards(EM, EQ, e, pos, target_pos)

			#others wait for their turn
			EQ.put("refresh",{})
			break

	
	def move_towards(self, EM, EQ, e, pos, target_pos):
		x,y = 0,0
		if pos[0] < target_pos[0]:
			x = 1
		elif pos[0] > target_pos[0]:
			x = -1
		if pos[1] < target_pos[1]:
			y = 1
		elif pos[1] > target_pos[1]:
			y = -1
		EQ.put("move_or_attack", {"eid":e, "dir":(x,y)})
