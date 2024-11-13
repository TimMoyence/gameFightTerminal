def move_choice(niveau, gamer):
   ## Need to check live one times
  move_choice = input("Where do you want to go ? (N, S, E, W) : ")   
  if move_choice == "N" and (gamer[0] > 0): 
    gamer[0] -= 1
  elif move_choice == "S" and len(niveau[0]) -  1 > gamer[0]:
      gamer[0] += 1
  elif move_choice == "E" and len(niveau[0]) - 1 > gamer[1]:
        gamer[1] += 1
  elif move_choice == "W" and (gamer[1] > 0):
        gamer[1] -= 1
  return gamer

      
