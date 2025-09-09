"""
Un compteur de mot qui est une exercice du cours Activité TEchnologie.
Par: Zihao Li
groupe 401
"""


def count_word(phrase):
    mot = phrase.split()
    return len(mot)


phrase_entree = input("Entrer une phrase.")
nombre_de_mots = count_word(phrase_entree)

print(f'La phrase que vous avez taper est {phrase_entree}')
print(f'Le nombre de mot entrer est {nombre_de_mots}')
