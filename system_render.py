import curses

class Renderer(object):
	def __init__(self, stdscr, mainscreen):
		self.__stdscr = stdscr
		self.__mscr = mainscreen
		self.__other_screens = [] #TODO

	def update(self, EM, EQ):
		if not EQ.can_get("refresh", 0):
			return
		self.__mscr.update(EM, EQ,
				(0,0, curses.COLS-1,curses.LINES-1))
		curses.doupdate()

	#def move_camera(self, to):
	#	self.__mscr.update_coords(to)
	
	def get_color_pair(self, fg, bg):
		return curses.color_pair(1 + 8 * fg + bg)


