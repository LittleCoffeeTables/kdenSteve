import collections


class EntityManager(object):
	def __init__(self):
		self.__max_entity = -1
		#dict with propname as key, dict of ID:value as val
		self.__all_properties = collections.defaultdict(dict)

	def new_entity(self):
		self.__max_entity += 1
		return self.__max_entity

	def create_entity(self, properties):
		i = self.new_entity()
		for prop, value in properties.items():
			self.__all_properties[prop][i] = value
		return i

	def create_tile(self, pos, properties):
		self.__all_properties["tile"][pos] = True
		self.__all_properties["p_pos"][pos] = pos
		self.__all_properties["r_pos"][pos] = pos
		for prop, value in properties.items():
			self.__all_properties[prop][pos] = value

	def get_by_prop(self, prop):
		return self.__all_properties[prop]

	def get_value(self, i, prop, default=None):
		return self.__all_properties[prop].get(i, default)

	def has_prop(self, i, prop):
		return (i in self.__all_properties[prop])

	def has_props(self, i, props):
		for prop in props:
			if i not in self.__all_properties[prop]:
				return False
		return True

