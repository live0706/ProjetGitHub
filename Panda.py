import random
mots = ['chat', 'chien', 'éléphant', 'tigre', 'girafe', 'singe', 'koala', 'panda', 'ours', 'loup']
motMystere = random.choice(mots)
monDevine = "*" * len(motMystere)
print(monDevine)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ''
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += '_'
    return mot_cache

def pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = []
    tentatives_restantes = 7

    print("Bienvenue au jeu du Pendu ! Devinez le mot sur l'animal.")
    print(afficher_mot_cache(mot_a_deviner, lettres_trouvees))

