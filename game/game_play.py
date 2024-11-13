import os 
from generate_level import generer_niveau 
from deplacement_engine import move_choice 
from generate_level import dragon_emoji
from fight import fight

def main():
  # Le niveau de base 
  niveau = generer_niveau(9,9)
  set_life = 9
  
  # la position du joueur 
  gamer = [0, 0]

  ## j'affiche 
  while gamer:
    os.system('clear')
    
    set_life = fight(set_life) if niveau[gamer[0], gamer[1]] == dragon_emoji else set_life
    niveau[gamer[0], gamer[1]] = "🛡️"
    
    
    life(set_life)
    print(niveau)

    # la faudra faire le Fight 
    
    niveau[gamer[0],gamer[1]] = "🍁"
    # le print du niveau avec le joueur
    gamer = move_choice(niveau, gamer) 
    
def life(set_life):
  totalLife = 9
  lifeEmoji = []
  for i in range(totalLife):
    if i < set_life:
      lifeEmoji.append("💙")
    else:
      lifeEmoji.append("💀")
  print(lifeEmoji)
  print("\n")


main()
