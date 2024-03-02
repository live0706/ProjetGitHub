from REE.py import calculate

def main():
    history = []

    while True:
        print("\nChoisissez une opération :")
        print("1 ou A - Addition")
        print("2 ou S - Soustraction")
        print("3 ou M - Multiplication")
        print("4 ou D - Division (Entière)")
        print("Q - Quitter")

        choice = input("Votre choix : ").upper()

        if choice == 'Q':
            print("Au revoir !")
            break

        if choice not in ['1', '2', '3', '4', 'A', 'S', 'M', 'D']:
            print("Choix invalide. Veuillez réessayer.")
            continue

        operation = ''
        if choice in ['1', 'A']:
            operation = 'addition'
        elif choice in ['2', 'S']:
            operation = 'soustraction'
        elif choice in ['3', 'M']:
            operation = 'multiplication'
        elif choice in ['4', 'D']:
            operation = 'division'

        try:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
            continue

        result = calculate(operation, num1, num2)
        print("Le résultat est :", result)
        history.append((num1, num2, operation, result))

    print("\nHistorique des calculs :")
    for entry in history:
        print(f"{entry[0]} {entry[2]} {entry[1]} = {entry[3]}")


if __name__ == "__main__":
    main()
