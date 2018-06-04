import curses

class MainScreen(object):
	def __init__(self, width, height, EM):
		# height+1 because you cannot write to the bottom-right-most
		# spot of a pad/window, this is a workaround
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
			self.update_coords(event["to"], (whereto[2]-whereto[0],
					whereto[3]-whereto[1]))

		entities = EM.get_prop("r_prio").items()
		priorities = sorted(entities, key=lambda x: x[1])
		for entity, priority in priorities:
			pos = EM.get_value(entity, "r_pos")
			char = EM.get_value(entity, "r_char")
			#if EM.has_prop(pos, "0_from"):
			#	val = EM.get_value(pos, "0_from")
			#	#if val < 10:
			#	char = str(val)[1:2]
			attrs = 0
			fg_colour = EM.get_value(entity, "r_colour",
					curses.COLOR_WHITE)
			bg_colour = curses.COLOR_CYAN
			if EM.has_prop(pos, "bg_colour"):
				bg_colour = EM.get_value(pos, "bg_colour")
				if EM.has_prop(pos, "bloody"):
					bg_colour = curses.COLOR_RED
			else:
				#this is a dumb effect
				attrs |= curses.A_REVERSE
			attrs |= self.get_color_pair(fg_colour, bg_colour)
			if pos is not None and char is not None:
				self.__scr.addstr(pos[1], pos[0], char, attrs)

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


	def get_color_pair(self, fg, bg):
		return curses.color_pair(1 + 8 * fg + bg)


