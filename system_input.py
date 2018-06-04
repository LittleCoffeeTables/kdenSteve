import key_config as kcfg

import curses

class InputHandler(object):
	def __init__(self, eid, stdscr):
		#self.__EM = entityManager
		#self.__SM = systemsManager
		self.__eid = eid
		self.__stdscr = stdscr

	def update(self, EM, EQ):
		i = self.__eid
		try:
			key = self.__stdscr.getkey()
		except curses.error:
			return
		#EQ.put("debug", {"text":"input %s %i"%(key, i)})
		if key in kcfg.quit:
			EQ.put("quit", {})
		elif key in kcfg.up:
			EQ.put("move_or_attack", {"eid":i, "dir":(0,-1)})
		elif key in kcfg.down:
			EQ.put("move_or_attack", {"eid":i, "dir":(0,1)})
		elif key in kcfg.left:
			EQ.put("move_or_attack", {"eid":i, "dir":(-1,0)})
		elif key in kcfg.right:
			EQ.put("move_or_attack", {"eid":i, "dir":(1,0)})
		else:
			curses.beep()
		EQ.put("refresh", {})

