"""
Un compteur de mot qui est une exercice du cours Activité TEchnologie.
Par: Zihao Li
groupe 401
"""
import random

chiffre_aleatoire = random.randint(1, 100)
guess=print('cest un jeu que vous devez guess un chiffre aleatoire entre 1-100')

nb_essai = 1
while guess != chiffre_aleatoire:
    guess = int(input('Entrer votre guess, cest entre 1-100'))
    if guess < chiffre_aleatoire:
        print('le nombre que vous cherchez est plus grand que votre guess')
    elif guess > chiffre_aleatoire:
        print('le nombre que vous cherchez est plus petit que votre guess')

    nb_essai += 1
    print('continuer à deviner')



    if guess == chiffre_aleatoire:
        print(f'vous avez trouver le bon nombre: {chiffre_aleatoire}')
        print(f'vous avez trouver le bon nombre en: {nb_essai} essai')
        break






