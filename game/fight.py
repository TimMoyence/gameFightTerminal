import random
from generate_level import dragon_emoji
from generate_level import castle_emoji

def dice():
  return random.randint(1, 6)

def fight(life):
      nb = dice()
      if 1 <= nb <= 3:
        life -= 1
      elif 4 <= nb <= 5:
        life -= 2
      else:
        life -= 3
      return life


