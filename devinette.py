"""
Un compteur de mot qui est une exercice du cours Activité TEchnologie.
Par: Zihao Li
groupe 401
"""
import random

chiffre_aleatoire = random.randint(1, 1000)

guess = int(input('Entrer votre guess'))

nb_essai = 0
while chiffre_aleatoire < nb_essai or chiffre_aleatoire > nb_essai:
    print(nb_essai)
    nb_essai += 1
    if chiffre_aleatoire == nb_essai:
        break

if chiffre_aleatoire == nb_essai:
    print('vous avez raison')
elif chiffre_aleatoire < nb_essai:
    print('le guess est trop grand')
elif chiffre_aleatoire > nb_essai:
    print('le guess est trop petit')














