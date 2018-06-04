#system_ai
import utils

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
			if self.do_ai(EM, EQ, e, ai, pos, target):
				continue
			EQ.put("refresh",{})

			#others wait for their turn
			break

	
	def do_ai(self, EM, EQ, e, ai, pos, target):
		if target is None:
			#TODO: idle ai
			return 1
		#target_pos = EM.get_value(target, "p_pos")
		#if target_pos is None:
		#	return 1

		if ai in ("orc",):
			if EM.has_prop(e, "attacked_this_turn"):
				#flee
				self.move_away(EM, EQ, e, pos, target)
			else:
				#move in
				self.move_towards(EM, EQ, e, pos, target)

		return 0

	def move_away(self, EM, EQ, e, pos, to):
		d_name = str(to)+"_from"
		cmpr = lambda a, b: a < b
		best_adj = self.find_best_adj(EM, EQ, pos, cmpr, d_name)
		#pick random one from best_adj
		#EQ.put("debug", {"text":str(best_adj)})
		if len(best_adj) < 1:
			return False
		new_pos = utils.random_from(EM, best_adj, "entity_rng")
		EQ.put("move_or_attack", {"eid":e, "to":new_pos})

	def move_towards(self, EM, EQ, e, pos, to):
		d_name = str(to)+"_to"
		cmpr = lambda a, b: a > b
		best_adj = self.find_best_adj(EM, EQ, pos, cmpr, d_name)
		#pick random one from best_adj
		#EQ.put("debug", {"text":str(best_adj)})
		if len(best_adj) < 1:
			return False
		new_pos = utils.random_from(EM, best_adj, "entity_rng")
		EQ.put("move_or_attack", {"eid":e, "to":new_pos})

	def find_best_adj(self, EM, EQ, pos, cmpr, d_name):
		best_adj = []
		best = None
		for adj in utils.get_adjacent(pos):
			val = EM.get_value(adj, d_name)
			if val is None:
				continue
			EQ.put("debug", {"text":"w00t"})
			if best is None or cmpr(best, val):
				best = val
				best_adj.clear()
			if best == val:
				best_adj.append(adj)
		return best_adj

	#def move_away(self, EM, EQ, e, pos, target_pos):
		#why is EM responsible for rng...
		#x = EM.randint(-1, 1, "entity_rng")
		#y = EM.randint(-1, 1)
		#EQ.put("debug",{"text":"%s %s" % (x,y)})
		#if pos[0] < target_pos[0]:
		#	x = -1
		#elif pos[0] > target_pos[0]:
		#	x = 1
		#if pos[1] < target_pos[1]:
		#	y = -1
		#elif pos[1] > target_pos[1]:
		#	y = 1
		#EQ.put("move_or_attack", {"eid":e, "dir":(x,y)})
	
	#def move_towards(self, EM, EQ, e, pos, target_pos):
	#	x,y = 0,0
	#	if pos[0] < target_pos[0]:
	#		x = 1
	#	elif pos[0] > target_pos[0]:
	#		x = -1
	#	if pos[1] < target_pos[1]:
	#		y = 1
	#	elif pos[1] > target_pos[1]:
	#		y = -1
	#	EQ.put("move_or_attack", {"eid":e, "dir":(x,y)})

