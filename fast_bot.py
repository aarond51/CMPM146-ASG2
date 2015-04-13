# fast_bot.py
# Aaron Desin (adesin)
# Chaiz Tuimoloau (ctuimolo)

import random
import time
import math


THINK_DURATION = 1
ROLLOUT_DURATION = 5

class Node (object):
	def __init__ (self, move = None, parent = None, state = None):
		self.move = move
		self.parent = parent
		self.children = []
		self.wins = 0.0
		self.visits = 0
		self.untrieds = state.get_moves()
		self.player = state.get_whos_turn()

	def select_child(self):
		sorted_list = sorted(self.children, key = lambda c: c.wins/c.visits + math.sqrt(2*math.log(self.visits)/c.visits))[-1]

		return sorted_list

	def add_child(self, newMove, newState):
		n = Node (move = newMove, parent = self, state = newState)
		self.untrieds.remove(newMove)
		self.children.append(n)
		return n

def think(state, quip):
	t_start = time.time()
	t_end = t_start + THINK_DURATION
	t_curr = 0.0
	iterations = 0
	
	root_state = state.copy()
	root_node = Node(state = root_state)
	
	while True:
		iterations += 1
		times_rolled_out = 0
	
		node = root_node
		new_state = root_state.copy()
		
		### Inner loop select ###
		while node.untrieds == [] and node.children != []:
			node = node.select_child()
			new_state.apply_move(node.move)
			
		### Expand            ###
		if node.untrieds != []:
			m = random.choice(node.untrieds)
			new_state.apply_move(m)
			node = node.add_child(m, new_state)
		
		### Autobots!         ###
		while new_state.get_moves() != [] and times_rolled_out < ROLLOUT_DURATION:
			new_state.apply_move(random.choice(new_state.get_moves()))
			times_rolled_out += 1
		
		### Back-propagate     ###
		while node != None:
			node.visits += 1
			if node.parent == None:
				break
			node.wins += new_state.get_score()[node.parent.player]
			node = node.parent
			
		t_curr = time.time()
		if t_curr > t_end:
			break
	
	""" This is sample rate"""
	sample_rate = float(iterations)/(t_curr - t_start)
	quip(sample_rate)
	
	new_move = sorted(root_node.children, key = lambda c: c.visits)[-1].move
	return new_move
	
	
	
	
	