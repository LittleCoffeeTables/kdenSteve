import collections


class EventQueue(object):
	#TODO: do I want to have a way to cancel all events this turn
	# for in case an illegal event was queued?
	def __init__(self):
		self.__queues = collections.defaultdict(collections.deque)

	def put(self, evtype, item):
		self.__queues[evtype].append(item)

	def get(self, evtype, index):
		item = self.__queues[evtype][index]
		return item

	def can_get(self, evtype, index):
		return index < len(self.__queues[evtype])

	def clear(self, evtype):
		if evtype == "all":
			self.__queues.clear()
		else:
			self.__queues[evtype].clear()

