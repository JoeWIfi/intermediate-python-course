import random

def main():
  nom_joueur_1 = input("nom du joueur 1: ")
  nom_joueur_2 = input("nom du joueur 2: ")
  dice_rolls = int ( input ( 'Combien de dés voulez-vous lancer ? ' ))
  dice_size  =  int ( input ( 'Combien de côtés ont les dés ? ' ))
  dice_sum_joueur_1 = 0
  dice_sum_joueur_2 = 0
  for j in range(0,2):
    for  i in range(0, dice_rolls):
      rouler = random.randint(1,dice_size)
      if j == 0:
        dice_sum_joueur_1 += rouler
      else:
        dice_sum_joueur_2 += rouler
      if rouler == 1 :
        print("Vous avez obtenu in ", rouler, " ! critical fail")
      elif rouler == dice_size:
        print("Vous avez obtenu un ", rouler, " ! Critical success!")
      else :
        print("Vous avez lancer un ", rouler)
  print(nom_joueur_1, ": vous avez obtenu un total de ", dice_sum_joueur_1)
  print(nom_joueur_2, ": vous avez obtenu un total de ", dice_sum_joueur_2)
  if dice_sum_joueur_1 == dice_sum_joueur_2:
    print("Egalité entre", nom_joueur_1, "et", nom_joueur_2)
  elif dice_sum_joueur_1 > dice_sum_joueur_2:
    print("Bravo", nom_joueur_1, "vous avez gagné")
  else:
    print("Bravo", nom_joueur_2, "vous avez gagné")

if __name__== "__main__":
  main()