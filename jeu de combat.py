"""
Zihao Li
gr-401
Le jeu de combat est un exercice durant le cours de ATE
"""

import random

'''Les données au début du jeu'''
POINT_VIE_INITIAL = 20
point_vie_actuel = POINT_VIE_INITIAL
match_gagner = 0
match_perdu = 0
numero_adversaire = 0
victoires_consecutives = 0

print('Bienvenue au jeu de combat')
print('Vous avez 20 points de vies au départ')

while point_vie_actuel > 0:

    '''Les résultats possible du niveau de adversaire'''
    force_adversaire = random.randint(2, 11)

    '''ajout d'un boss apres 3 combats gagner'''
    if match_gagner > 0 and match_gagner % 3 == 0:
        print('Vous avez atteint une séquence de 3 victoires! Vous faites face à un BOSS plus fort.')
        force_adversaire = random.randint(5, 11)

    '''Lancement du jeu'''
    print('NOUVEL ADVERSAIRE')
    print(f"Adversaire: numéro {numero_adversaire + 1}")
    print(f"Force de l’adversaire: {force_adversaire}")
    print(f"Niveau de vie de l’usager: {point_vie_actuel} points")
    print(f"Statut des combats: {match_gagner} victoires et {match_perdu} défaites")

    choix = input(
        'Que voulez-vous faire? Tape 1 pour combattre, 2 pour contourner, 3 pour les règles, 4 pour quitter: ')

    '''Le résultat si le joueur choisit l'option 1'''
    if choix == '1':
        numero_adversaire += 1
        force_joueur = random.randint(2, 12)
        print(f"Lancer du dé(force du joueur){force_joueur} points")

        '''Résultat si gagner'''
        if force_joueur > force_adversaire:
            point_vie_actuel += force_adversaire
            match_gagner += 1
            victoires_consecutives += 1

            print("Dernier combat = VICTOIRE")
            print(f"point de vie: {point_vie_actuel} points")
            print(f"Nombre de victoires consécutives: {victoires_consecutives}")

            '''Résultat si perdu'''
        elif force_joueur < force_adversaire:
            point_vie_actuel -= force_adversaire
            match_perdu += 1
            victoires_consecutives = 0

            print("Dernier combat = DÉFAITE")
            print(f"point de vie: {point_vie_actuel} points")


            '''Resultat si egalité'''
        else:
            victoires_consecutives = 0

            print("Dernier combat = PARTIE NULLE ")
            print(f"point de vie(force du joueur){point_vie_actuel} points")

            '''Le résultat si le joueur choisit l'option 2'''
    elif choix == '2':
        numero_adversaire += 1
        point_vie_actuel -= 1
        victoires_consecutives = 0

        print(f"Vous avez contourné l'adversaire. Pénalité de **1 point de vie**.")
        print(f'Niveau de vie de l’usager: {point_vie_actuel} points.')

        '''Le résultat si le joueur choisit option 3'''
    elif choix == '3':
        print(
            'Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.'
            'Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.'
            'Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de '
            'l’adversaire.'
            'Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.'
            'La partie se termine lorsque les points de vie de l’usager tombent sous 0.'
            'L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de '
            '1 point de vie.')


        '''Le résultat si le joueur choisit option 4'''
    elif choix == '4':
        print('Merci de votre participation. À bientôt!')
        break


    else:
        print("Choix invalide. Veuillez taper 1, 2, 3 ou 4.")

if point_vie_actuel <= 0:
    print("Votre personnage est mort! La partie est terminée.")
    print(f"Vous avez vaincu {match_gagner} monstre.")
