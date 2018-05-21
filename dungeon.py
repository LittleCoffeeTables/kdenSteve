

class Dungeon(object):
	def __init__(self, size, EM):
		self.__size = size
		self.__EM = EM
		for x in range(self.__size[0]):
			for y in range(self.__size[1]):
				pos = (x, y)

				material = "floor"
				if (x == 0 or y == 0
				 or x == self.__size[0] - 1
				 or y == self.__size[1] - 1):
					material = "wall"
				self.create_tile(pos, material)

	def create_tile(self, pos, mat):
		if mat == "wall":
			self.__EM.create_tile(pos, {"material":mat,
				"r_char":"#", "r_prio":1000, "physical":True})
		elif mat == "floor":
			self.__EM.create_tile(pos, {"material":mat,
				"r_char":".", "r_prio":0})


