"""
Un compteur de mot qui est une exercice du cours Activité TEchnologie.
Par: Zihao Li
groupe 401
"""
from random import randint


question = input('est ce que vous voulez personalisez les bornes ou utilier notre borne, repondez 1 comme oui et 2 comme non')




borne_min_str = input("Entrez la borne minimale (un entier) : ")
borne_min = int(borne_min_str)


borne_max_str = input("Entrez la borne maximale (un nombre décimal) : ")
borne_max = int(borne_max_str)

nombre_aleatoire = randint(borne_min, borne_max)

guess=print('cest un jeu que vous devez guess un chiffre aleatoire entre les bornes que vous avez entrer')


nb_essai = 1
while guess != nombre_aleatoire:
   guess = int(input('Entrer votre guess, cest entre 1-100'))
   if guess < nombre_aleatoire:
       print('le nombre que vous cherchez est plus grand que votre guess')
   elif guess > nombre_aleatoire:
       print('le nombre que vous cherchez est plus petit que votre guess')


   nb_essai += 1
   print('continuer à deviner')






   if guess == nombre_aleatoire:
       print(f'vous avez trouver le bon nombre: {nombre_aleatoire}')
       print(f'vous avez trouver le bon nombre en: {nb_essai} essai')
       break



chiffre_aleatoire = randint(0,100)
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

