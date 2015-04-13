# greedy_bot.py
# Aaron Desin (adesin)
# Chaiz Tuimoloau (ctuimolo)

from random import choice

def think(state, quip):
   maxMove = None;
   maxScore = -1;
   for move in state.get_moves():
      newState = state.copy()
      newState.apply_move(move)
      newScore = newState.get_score()[state.get_whos_turn()]
      if newScore > maxScore:
         maxMove = move
         maxScore = newScore
   return maxMove
 
