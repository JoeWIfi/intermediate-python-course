import random

def main():
  dice_rolls = 2
  dice_sum = 0
  for  i in range(0, dice_rolls):
    rouler = random.randint(1,6)
    dice_sum += rouler
    print("Vous avez lancer un ", rouler)
  print("Vous avez obtenu un total de ", dice_sum)

if __name__== "__main__":
  main()