while True:
    nombre = int(input("Entrer un nombre : "))
    print(nombre)
    
    for i in range(1, 11):
        resultat = nombre * i
        print(f"{nombre} x {i} = {resultat}")

    print("Fin de l'affichage")
    
    choix = input("Appuyez sur 'P' pour recommencer, ou une autre touche pour sortir : ").upper()

    if choix != 'P':
        break
