#system_attack.py
import curses

class Attacks(object):
	def __init__(self):
		pass

	def update(self, EM, EQ):
		i = 0
		while EQ.can_get("attack", i):
			event = EQ.get("attack", i)
			i += 1
			self.try_attack(EM, EQ, event,
					False)
		while EQ.can_get("move_or_attack", 0):
			event = EQ.pop("move_or_attack")
			if not self.try_attack(EM, EQ, event, True):
				EQ.put("move", event)

	def try_attack(self, EM, EQ, event, auto):
		eid = event["eid"]
		#is a physical position really necessary to attack?
		if not EM.has_prop(eid, "p_pos"):
			return False
		pos = EM.get_value(eid, "p_pos")
		if "dir" in event:
			new_pos = (pos[0]+event["dir"][0],
				   pos[1]+event["dir"][1])
		elif "to" in event:
			new_pos = event["to"]
		else:
			raise ValueError("event has no dir or to: "+str(event))
		other = None
		if auto:
			others = EM.get_by_props([
			  "physical", "p_pos", "health"])
		else:
			others = EM.get_by_props([
			  "physical", "p_pos"])
		#this could use a priority sorting system one day
		for other in others:
			if other == eid:
				#self harm not enabled by default
				continue
			if new_pos == EM.get_value(other, "p_pos"):
				break
		else:
			return False
		
		#do the thing
		self.do_attack(EM, EQ, eid, other)

		return True


	def do_attack(self, EM, EQ, eid, target):
		#curses.beep()
		if (EM.has_prop(target, "health")
		  and EM.has_prop(eid, "attack_dmg")):
			dmg = EM.get_value(eid, "attack_dmg")
			EM.edit_value(target, "health", add=-dmg)
			cost = 1 #TODO: attacks that cost more than 1 ap
			EM.edit_value(eid, "ap", add=-cost)
			EM.set_value(eid, "attacked_this_turn", True)
			curses.beep()


