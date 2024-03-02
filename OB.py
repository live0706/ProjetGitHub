class Personnage:
    def __init__(self, nom, age, arme, armure, inventaire):
        self.nom = nom
        self.age = age
        self.arme = arme
        self.armure = armure
        self.inventaire = inventaire

    def attaquer(self):
        pass  # Méthode à implémenter dans les classes héritées

    def defendre(self):
        pass  # Méthode à implémenter dans les classes héritées


class Guerrier(Personnage):
    def __init__(self, nom, age, arme, armure, inventaire):
        super().__init__(nom, age, arme, armure, inventaire)

    def attaquer(self):
        print(f"{self.nom} attaque avec {self.arme}!")

    def defendre(self):
        print(f"{self.nom} se défend avec {self.armure}!")


class Mage(Personnage):
    def __init__(self, nom, age, arme, armure, inventaire):
        super().__init__(nom, age, arme, armure, inventaire)

    def attaquer(self):
        print(f"{self.nom} lance un sort avec {self.arme}!")

    def defendre(self):
        print(f"{self.nom} invoque une barrière magique avec {self.armure}!")


class Arme:
    def __init__(self, nom, type_):
        self.nom = nom
        self.type = type_


class Armure:
    def __init__(self, casque, plastron, jambieres):
        self.casque = casque
        self.plastron = plastron
        self.jambieres = jambieres


class Inventaire:
    def __init__(self, objets):
        self.objets = objets


# Création des objets
epee = Arme("Épée", "à une main")
arc = Arme("Arc", "à deux mains")
armure_guerrier = Armure("Casque en acier", "Plastron en fer", "Jambières en cuir renforcé")
armure_mage = Armure("Chapeau de mage", "Robe d'étoffe", "Pantalon de mage")
inventaire_guerrier = Inventaire(["Potion de soin", "Pain"])
inventaire_mage = Inventaire(["Potion de mana", "Parchemin de sort"])

# Création des personnages
guerrier1 = Guerrier("Conan", 30, epee, armure_guerrier, inventaire_guerrier)
mage1 = Mage("Gandalf", 200, arc, armure_mage, inventaire_mage)

# Test des méthodes
guerrier1.attaquer()
mage1.attaquer()
