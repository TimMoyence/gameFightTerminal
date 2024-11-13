import random
import numpy as np

dragon_emoji = "🐉"
castle_emoji = "🏰"

def generer_niveau(y, x):
  niveau = []
  for i in range (0, x):
    linelevel = []
    for j in range(0, y):
      nb = random.randint(0, 1)
      emojis = dragon_emoji if nb == 1 else castle_emoji
      linelevel.append(emojis)
    niveau.append(linelevel)
  niveau = np.array(niveau)
  return niveau





  
  
