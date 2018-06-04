#system_dijkstra
import utils

import collections

class Dijkstra(object):
	def __init__(self):
		#self.__maps = collections.defaultdict(dict)
		pass

	def update(self, EM, EQ):
		#if not EQ.can_get("move", 0):
		#	return
		moved_entities = set()
		i = 0
		while EQ.can_get("move", i):
			event = EQ.get("move", i)
			i += 1
			moved_entities.add(event["eid"])
		#for e in EM.get_by_props(["p_pos","dijkstra_target"]):
		for e in moved_entities:
			if not EM.has_props(e, ["p_pos","dijkstra_target"]):
				continue
			#life = EM.get_value(e, "dijkstra_life")
			#if life > 0:
			#	#no need to refresh the map every turn
			#	continue
			#pos = EM.get_value(e, "p_pos")
			self.update_map(EM, EQ, e, [e])
		if not EQ.can_get("new_turn",0):
			return
		for e in EM.get_by_prop("dijksra_keeper"):
			#props needs to be a tuple to be a valid name!
			props = EM.get_value(e, "dijkstra_keeper")
			goals = EM.get_by_props(props)
			self.update_map(EM, EQ, props, goals)

	def update_map(self, EM, EQ, name, goals):
		name = str(name)
		self.calculate(EM, EQ, name+"_to", goals)
		self.invert(EM, EQ, name)
		self.calculate(EM, EQ, name+"_from", None)
		#self.__maps[name]["to"] = map_
		#inverse = self.invert(map_)
		#self.__maps[name]["from"] = self.calculate(inverse)


	def invert(self, EM, EQ, name):
		magic_multi = -1.2
		to_name = name + "_to"
		from_name = name + "_from"
		for t in EM.get_by_prop("tile"):
			to_val = EM.get_value(t, to_name)
			mv_cost = EM.get_move_cost(t)
			if to_val is None or mv_cost > 100:
				continue
			val = magic_multi * to_val 
			EM.set_value(t, from_name, val)

	def calculate(self, EM, EQ, name, goals):
		frontier = collections.deque()
		if goals is not None:
			EM.clear_prop(name)
			for g in goals:
				pos = EM.get_value(g, "p_pos")
				EM.set_value(pos, name, 0)
				frontier.append(pos)
		else:
			min_val = 0
			for t in EM.get_by_prop(name):
				val = EM.get_value(t, name)
				if val < min_val:
					frontier.clear()
					min_val = val
				if val == min_val:
					frontier.append(t)
		#access a tile's step value with:
		#EM.get_value(pos, name)
		try:
			while True:
				nx = frontier.popleft()
				a = EM.get_value(nx, name)
				for adj in utils.get_adjacent(nx):
					b = EM.get_value(adj, name)
					is_tile = EM.has_prop(adj, "tile")
					if not is_tile:
						continue
					mv_cost = EM.get_move_cost(adj)
					if b is None or b > a + mv_cost:
						EM.set_value(adj, name,
								a+mv_cost)
						frontier.append(adj)
		except IndexError:
			#deque is empty
			pass



