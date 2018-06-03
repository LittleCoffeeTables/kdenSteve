import event_queue
import system_input
import system_movement
import system_render
import system_logger
import system_attack
import system_corpses

import collections

#TODO: get rid of this
DEFAULT_PLAYER = 0

class SystemsManager(object):
	def __init__(self, entityManager, stdscr, MS):
		self.__EM = entityManager
		self.__systems = [
				system_input.InputHandler(DEFAULT_PLAYER,
					stdscr),
				system_attack.Attacks(),
				system_movement.Movement(),
				system_corpses.Corpses(),
				system_render.Renderer(stdscr, MS),
				system_logger.Logger(),
				]
		self.__EQ = event_queue.EventQueue()

	def update_all(self):
		for system in self.__systems:
			system.update(self.__EM, self.__EQ)
		if self.__EQ.can_get("quit",0):
			return 1
		self.__EQ.clear("all")
		return 0

	def event(self, evtype, item):
		self.__EQ[evtype].put(item)

