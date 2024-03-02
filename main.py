import random

print('Bienvenue dans Morpion !')
continuer = input('Voulez-vous continuer le jeu? (Oui/Non)')
# Vérifier si l'utilisateur veut continuer
if continuer.lower() == 'oui':
    print('Continuons!')
elif continuer.lower() == 'non':
    print('Vous avez quitter le jeu!')
    quit()


def afficher_grille(grille):
    """Affiche la grille de Morpion."""
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 4 * len(grille[0]))


def creer_grille(taille):
    """Crée une grille de Morpion vide avec la taille spécifiée."""
    return [[" " for _ in range(taille)] for _ in range(taille)]


def placer_pion(grille, ligne, colonne, joueur):
    """Place un pion du joueur sur la grille."""
    if grille[ligne - 1][colonne - 1] == " ":
        grille[ligne - 1][colonne - 1] = joueur
        return True
    else:
        print("Emplacement déjà occupé. Choisissez un autre.")
        return False


def verifier_ligne(grille, joueur):
    """Vérifie s'il y a une ligne complète pour le joueur."""
    for ligne in grille:
        if all(cell == joueur for cell in ligne):
            return True
    return False


def verifier_colonne(grille, joueur):
    """Vérifie s'il y a une colonne complète pour le joueur."""
    for j in range(len(grille)):
        if all(grille[i][j] == joueur for i in range(len(grille))):
            return True
    return False


def verifier_diagonale(grille, joueur):
    """Vérifie s'il y a une diagonale complète pour le joueur."""
    taille = len(grille)
    if all(grille[i][i] == joueur for i in range(taille)):
        return True
    if all(grille[i][taille - i - 1] == joueur for i in range(taille)):
        return True
    return False


def adversaire_intelligent(grille, joueur):
    """L'adversaire intelligent place un pion."""
    taille = len(grille)
    # Vérifie s'il peut gagner en une étape
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == " ":
                grille[i][j] = joueur
                if est_victoire(grille, joueur):
                    return True
                grille[i][j] = " "
    # S'il ne peut pas gagner, place un pion aléatoirement
    while True:
        ligne = random.randint(1, taille)
        colonne = random.randint(1, taille)
        if grille[ligne - 1][colonne - 1] == " ":
            grille[ligne - 1][colonne - 1] = joueur
            break


def est_victoire(grille, joueur):
    """Vérifie si le joueur a gagné."""
    return (verifier_ligne(grille, joueur) or
            verifier_colonne(grille, joueur) or
            verifier_diagonale(grille, joueur))


def jouer_morpion(taille):
    """Fonction principale pour jouer au Morpion."""
    grille = creer_grille(taille)
    joueurs = ["X", "O"]
    joueur_actuel = 0

    while True:
        afficher_grille(grille)
        joueur = joueurs[joueur_actuel]
        print(f"C'est au tour du joueur {joueur}")

        if joueur == "X":
            while True:
                try:
                    ligne = int(input("Entrez le numéro de ligne : "))
                    colonne = int(input("Entrez le numéro de colonne : "))
                    if 1 <= ligne <= taille and 1 <= colonne <= taille:
                        if placer_pion(grille, ligne, colonne, joueur):
                            break
                    else:
                        print("Coordonnées invalides. Veuillez réessayer.")
                except ValueError:
                    print("Veuillez entrer un nombre entier.")
        else:
            adversaire_intelligent(grille, joueur)

        if est_victoire(grille, joueur):
            afficher_grille(grille)
            print(f"Le joueur {joueur} a gagné !")
            break
        elif all(all(cell != " " for cell in ligne) for ligne in grille):
            afficher_grille(grille)
            print("Match nul !")
            break

        joueur_actuel = (joueur_actuel + 1) % 2

    while True:
        choix = input("Voulez-vous recommencer ? (Oui/Non) : ").strip().lower()
        if choix in ("oui", "non"):
            return choix == "oui"
        else:
            print("Réponse invalide. Veuillez entrer 'Oui' ou 'Non'.")


def main():
    """Fonction principale."""
    while True:
        try:
            taille = int(input("Entrez la taille de la grille : "))
            if taille < 3:
                print("La taille minimale de la grille est 3.")
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    recommencer = True
    while recommencer:
        recommencer = jouer_morpion(taille)


if __name__ == "__main__":
    main()
