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

	#init colour pairs
	for fg in range(8):
		for bg in range(8):
			curses.init_pair(1 + 8 * fg + bg, fg, bg)

	f = open("debug.log", "w")
	f.close()

	EM = entities.EntityManager()
	EM.create_entity({"controlled": True, "p_pos":(3,7), "physical":True,
		"r_char":"@", "r_pos":(3,7), "r_prio":900, "camera":True,
		"health":30, "attack_dmg":6, "blood":1000,
		"r_colour": curses.COLOR_BLACK,
		"ap":3, "max_ap":3, "dijkstra_target":True})

	d_size = (100, 100)

	MS = main_screen.MainScreen(d_size[0], d_size[1], EM)

	SM = systems.SystemsManager(EM, stdscr, MS)

	dungeon.Dungeon(d_size, EM)

	stdscr.nodelay(True)

	#EM.load("derp")

	SM.event("refresh", {})

	quit = 0
	while not quit:
		quit = SM.update_all()

	EM.save("derp")

	stdscr.refresh()


curses.wrapper(main)
