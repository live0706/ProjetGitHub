def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)


def verifier_victoire(plateau, symbole):
    # Vérification des lignes et des colonnes
    for i in range(3):
        if all(plateau[i][j] == symbole for j in range(3)) or all(plateau[j][i] == symbole for j in range(3)):
            return True

    # Vérification des diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True

    return False


def morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    symboles = ['X', 'O']
    tour = 0

    while True:
        afficher_plateau(plateau)
        symbole = symboles[tour % 2]
        print(f"C'est au tour du joueur {symbole}")

        ligne = int(input("Entrez le numéro de ligne (0, 1, ou 2) : "))
        colonne = int(input("Entrez le numéro de colonne (0, 1, ou 2) : "))

        if plateau[ligne][colonne] == " ":
            plateau[ligne][colonne] = symbole

            if verifier_victoire(plateau, symbole):
                afficher_plateau(plateau)
                print(f"Le joueur {symbole} a gagné !")
                break
            elif all(plateau[i][j] != " " for i in range(3) for j in range(3)):
                afficher_plateau(plateau)
                print("Match nul !")
                break
            else:
                tour += 1
        else:
            print("Case déjà occupée, veuillez rejouer.")


if __name__ == "__main__":
    morpion()