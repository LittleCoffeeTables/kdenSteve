import curses

class Renderer(object):
	def __init__(self, stdscr, mainscreen):
		self.__stdscr = stdscr
		self.__mscr = mainscreen
		self.__other_screens = [] #TODO
		self.__bot_panel_h = 1
		#TODO: get rid of this
		self.__player_id = 0

	def update(self, EM, EQ):
		if not EQ.can_get("refresh", 0):
			return
		self.__mscr.update(EM, EQ,
				(0,0, curses.COLS-1,
				 curses.LINES-1-self.__bot_panel_h))
		
		hp = EM.get_value(self.__player_id, "health", "N/A")
		self.__stdscr.move(curses.LINES-self.__bot_panel_h, 0)
		self.__stdscr.addch(curses.ACS_DIAMOND, self.get_color_pair(
			curses.COLOR_RED, curses.COLOR_BLACK))
		hp_attrs = 0
		if type(hp) == int and hp < 10:
			hp_attrs |= curses.A_BLINK
			hp_attrs |= self.get_color_pair(
					curses.COLOR_RED, curses.COLOR_BLACK)
		self.__stdscr.addstr("{0:>3} ".format(hp), hp_attrs)
		
		ap = EM.get_value(self.__player_id, "ap")
		max_ap = EM.get_value(self.__player_id, "max_ap")
		ap_str = "{0:>1}/{1:>1}".format(ap, max_ap)
		if ap is None:
			ap_str = "N/A"
		apc = self.get_color_pair(curses.COLOR_BLUE, curses.COLOR_BLACK)
		self.__stdscr.addch(curses.ACS_DARROW, apc)
		self.__stdscr.addstr(ap_str, apc)

		curses.doupdate()

	#def move_camera(self, to):
	#	self.__mscr.update_coords(to)
	
	def get_color_pair(self, fg, bg):
		return curses.color_pair(1 + 8 * fg + bg)


