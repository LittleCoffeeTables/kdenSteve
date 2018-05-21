import entity_manager
import systems
#import event_queue
#import input_handler
#import event_handler
import main_screen
import dungeon

import curses
import time

def main(stdscr):
	stdscr.clear()
	curses.curs_set(False)

	EM = entity_manager.EntityManager()
	player = EM.create_entity({"p_pos":[3,7], "physical":True,
		"r_char":"@", "r_pos":[3,7], "r_prio":900, "camera":True})

	d_size = (100, 100)

	MS = main_screen.MainScreen(d_size[1], d_size[0], EM)

	SM = systems.SystemsManager(EM, stdscr, MS)

	DM = dungeon.Dungeon(d_size, EM)

	stdscr.nodelay(True)

	quit = 0
	while not quit:
		quit = SM.update_all()
		
	stdscr.refresh()


curses.wrapper(main)
