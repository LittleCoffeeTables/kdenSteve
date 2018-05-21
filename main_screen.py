import curses


class MainScreen(object):
	def __init__(self, width, height, EM):
		self.__scr = curses.newpad(height+1, width)
		#self.__EM = EM
		self.__coords = (0,0)
		self.__size = (width, height)

	def update(self, EM, EQ, whereto):
		self.__scr.clear()

		i = 0
		while EQ.can_get("move_camera", i):
			event = EQ.get("move_camera", i)
			i+=1
			self.update_coords(event["to"])

		entities = EM.get_by_prop("r_prio").items()
		priorities = sorted(entities, key=lambda x: x[1])
		for entity, priority in priorities:
			pos = EM.get_value(entity, "r_pos")
			#assert(pos == EM.get_value(entity, "p_pos"))
			#EQ.put("debug", {"text":"helloisms %i %i"%(
			#	pos[0],pos[1])})
			char = EM.get_value(entity, "r_char")
			if pos is not None and char is not None:
				self.__scr.addch(pos[1], pos[0], char)

		#self.__scr.addstr(10, 10,
		#		"%i, %i"%(self.__coords[0], self.__coords[1]))

		self.__scr.noutrefresh(self.__coords[1], self.__coords[0],
				whereto[1],whereto[0], whereto[3],whereto[2])

	def update_coords(self, centre, visible_size=None):
		if visible_size is None:
			visible_size = (curses.COLS, curses.LINES)
		x = centre[0] - visible_size[0]//2
		y = centre[1] - visible_size[1]//2
		x = max(0, min(x, self.__size[0]-visible_size[0]))
		y = max(0, min(y, self.__size[1]-visible_size[1]))
		self.__coords = (x,y)

