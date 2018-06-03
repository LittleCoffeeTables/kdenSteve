import entities
import systems
#import event_queue
#import input_handler
#import event_handler
import main_screen
import dungeon

import curses
#import time

def main(stdscr):
	stdscr.clear()
	curses.curs_set(False)

	f = open("debug.log", "w")
	f.close()

	EM = entities.EntityManager()
	EM.create_entity({"p_pos":[3,7], "physical":True,
		"r_char":"@", "r_pos":[3,7], "r_prio":900, "camera":True})

	d_size = (100, 100)

	MS = main_screen.MainScreen(d_size[0], d_size[1], EM)

	SM = systems.SystemsManager(EM, stdscr, MS)

	dungeon.Dungeon(d_size, EM)

	stdscr.nodelay(True)

	#EM.load("derp")

	quit = 0
	while not quit:
		quit = SM.update_all()

	EM.save("derp")

	stdscr.refresh()


curses.wrapper(main)
