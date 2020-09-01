import random

def main():
  dice_rolls = int ( input ( 'Combien de dés voulez-vous lancer?' ))
  dice_size  =  int ( input ( 'Combien de côtés ont les dés?' ))
  dice_sum = 0
  for  i in range(0, dice_rolls):
    rouler = random.randint(1,dice_size)
    dice_sum += rouler
    if rouler == 1 :
      print("Vous avez obtenu in ", rouler, " ! critical fail")
    elif rouler == dice_size:
      print("Vous avez obtenu un ", rouler, " ! Critical success!")
    else :
      print("Vous avez lancer un ", rouler)
  print("Vous avez obtenu un total de ", dice_sum)

if __name__== "__main__":
  main()