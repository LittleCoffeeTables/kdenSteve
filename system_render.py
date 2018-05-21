import curses

class Renderer(object):
	def __init__(self, stdscr, mainscreen):
		self.__stdscr = stdscr
		self.__mscr = mainscreen
		self.__other_screens = [] #TODO

	def update(self, EM, EQ):
		self.__mscr.update(EM, EQ,
				(0,0, curses.COLS-1,curses.LINES-1))
		curses.doupdate()

	def move_camera(self, to):
		self.__mscr.update_coords(to)
