"""
Un compteur de mot qui est une exercice du cours Activité TEchnologie.
Par: Zihao Li
groupe 401
"""

from random import randint


def choisir_bornes():
    """
    Cette fonction sera utiliser quand le jeu vient de demarrer
    Il permet à l'utilisateur de choisir entre bornes personnalisées ou bornes par défaut de 0-100). Si
    lutilisateur choisi de personaliser, le fonction le permettre de entrer le borne personalisé et randomise une
    nombre aleatoire entre les bornes choisi et si l'utilisateur decide de utiliser le borne defaut, cette fonction
    randomise une nombre entre 0-100.
    """

    min_defaut = 0
    max_defaut = 100

    question = input('Voulez-vous personnaliser les bornes (1: Oui, 2: Non, les bornes de defaut sont 0-100) ? ')

    if question == '1':
        print("choisir vos bornes")

        borne_min = int(input("Entrez la borne minimale (un nombre entier) : "))
        borne_max = int(input("Entrez la borne maximale (un nombre entier) : "))

        if borne_min >= borne_max:
            print("Erreur : La borne minimale doit être inférieure à la borne maximale.")
            print(f"Bornes par defaut est : {min_defaut} et {max_defaut}.")
            return min_defaut, max_defaut

        return borne_min, borne_max


    else:
        # Option par défaut (choix 2 ou toute autre entrée)
        print(f" Bornes par defaut est : {min_defaut} et {max_defaut}")
        return min_defaut, max_defaut


def une_partie():
    """
    C'est une fonction qui sera demarrer losrque l'utilisateur fait le choix entre le borne defaut ou personaliser
    Il permet de commencer une partie de jeu,apres un guess de l'utilisateur, cette fonction inquera
    si le guess est trop grand ou petit. Puis il inquera le nb d'utiliser durant le jeu.
    """

    min_borne, max_borne = choisir_bornes()

    nombre_aleatoire = randint(min_borne, max_borne)

    print(f' le jeu commence ')
    print(f'Cest un jeu que vous devez deviner un chiffre aléatoire entre {min_borne} et {max_borne}.')

    nb_essai = 0
    guess = None


    while guess != nombre_aleatoire:
        nb_essai += 1


        guess = int(input(f'Essai n°{nb_essai} - Entrez votre guess : '))



        if guess < nombre_aleatoire:
            print('le nombre que vous cherchez est plus grand que votre guess')
        elif guess > nombre_aleatoire:
            print('le nombre que vous cherchez est plus petit que votre guess')

    print(f'Vous avez trouvé le bon nombre : {nombre_aleatoire} !')
    print(f'Vous avez trouvé le bon nombre en : {nb_essai} essai(s).')


def continuer_partie():
    """
    Cette fonction sera demarrer lorsque l'utilisateur a reussi de deviner le nombre
    Il permet l'utilisateur de choisir si il voudrait refaire une autre partie ou quitter le jeu directement.

    """
    rejouer = input("Voulez vous rejouer une autre partie, oui ou non")

    return rejouer.lower() == "oui"


while True:
    une_partie()

    if not continuer_partie():
        break

print("Merci de votre participation")
