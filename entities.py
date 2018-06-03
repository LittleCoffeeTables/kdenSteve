import collections
import json
import ast


class EntityManager(object):
	def __init__(self):
		self.__max_entity = -1
		#dict with propname as key, dict of ID:value as val
		self.__all_properties = collections.defaultdict(dict)

	def new_entity(self):
		self.__max_entity += 1
		return self.__max_entity

	def save(self, fname):
		#def dumper(dict_):
		#	if type(dict_) not in (dict, collections.defaultdict):
		#		return dict_
		#	new = {str(k):dumper(v) for k, v in
		#		dict_.items()}
			#return json.dumps(new)
		#	return new
		#prop_string = json.dumps(dumper(self.__all_properties))
		prop_string = str(dict(self.__all_properties))
		with open(fname, "w") as f:
			f.write("%i\n"%(self.__max_entity))
			f.write(prop_string)

	def load(self, fname):
		#this is dumb
		#def loader(x):
		#	if type(x[0][1]) == dict:
		#		return collections.defaultdict(dict, x)
		#	else:
		#		return ast.literal_eval(x)
		with open(fname, "r") as f:
			things = f.read().split('\n')
			self.__max_entities = int(things[0])
			#self.__all_properties = json.loads(things[1],
			#		object_pairs_hook=loader)
			self.__all_properties = collections.defaultdict(
					dict, ast.literal_eval(things[1]))
		#with open("derp.log", "w") as f:
		#	for prop in self.__all_properties:
		#		f.write("%s %s\n"%(
		#			prop, self.get_value(0, prop)))
			#f.write(self.__all_properties.__repr__())

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

	def quick_entity(self, prefab_name, pos, ow={}):
		prefab_props = None
		if prefab_name == "orc":
			prefab_props = {
					"r_char": "o",
					"r_colour": "green",
					"r_prio": 100,
					"physical": True,
					"ai": "orc",
					"blood": 1000,
					}

		if prefab_props is not None:
			ow["p_pos"] = pos
			ow["r_pos"] = pos
			all_props = collections.ChainMap(ow, prefab_props)
			self.create_entity(all_props)

	def get_prop(self, prop):
		return self.__all_properties[prop]

	def get_by_prop(self, prop):
		return self.__all_properties[prop].keys()

	def get_by_props(self, props):
		dicts = []
		for prop in props:
			dicts.append(self.__all_properties[prop])
		#create set of the keys in common across all dicts
		return set.intersection(*map(set, dicts))

	def get_value(self, i, prop, default=None):
		return self.__all_properties[prop].get(i, default)

	def set_value(self, i, prop, value):
		self.__all_properties[prop][i] = value

	def has_prop(self, i, prop):
		return (i in self.__all_properties[prop])

	def has_props(self, i, props):
		for prop in props:
			if i not in self.__all_properties[prop]:
				return False
		return True

	def edit_value(self, i, prop, 
			set=None, add=None, multi=None, invert=None):
		if not self.has_prop(i, prop):
			raise KeyError
		val = self.get_value(i, prop)
		if set is not None:
			val = set
		if add is not None:
			val += add
		if multi is not None:
			val *= multi
		if invert is not None:
			val = not val
		self.set_value(i, prop, val)

