# uniform_bot.py
# Aaron Desin (adesin)
# Chaiz Tuimoloau (ctuimolo)

from random import choice

def think(state, quip):
  return choice(state.get_moves())
