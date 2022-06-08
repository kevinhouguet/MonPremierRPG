import random

monstres = ["Kobold", "Goblin", "Troll", "Mort-vivant"]
qualite_monstre = ["commun", "chef", "élite", "légendaire"]
qualite_objet = ["commun", "magique", "rare", "épique", "légendaire", "unique"]

classes = ["Guerrier", "Mage", "Voleur"]


class Personnage:
    caracs = {"force": 1, "mana": 1, "dextérité": 1}

    def __init__(self, nom, classe="", niveau=0, vie=0):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.vie = vie
        print("Le personnage " + self.nom + " a été créé")
        self.afficher_informations_personnage()
        self.calcul_vie()

    def get_classe(self):
        return self.classe

    def get_niveau(self):
        return self.niveau

    def get_vie(self):
        return self.vie

    def get_nom(self):
        return self.nom

    def get_force(self):
        return self.caracs["force"]

    def get_mana(self):
        return self.caracs["mana"]

    def get_dext(self):
        return self.caracs["dextérité"]

    def get_caracs(self):
        return self.caracs

    def afficher_informations_personnage(self):
        print(">>> Voici les informations de votre personnage : <<<")
        print("Votre nom est " + self.nom)
        print(f"Vous êtes un {self.classe} de niveau {self.niveau} avec {self.get_vie()} de vie")
        print(f"Voici vos caractéristiques liées à votre classe : {self.caracs}")

    def calcul_vie(self):
        self.vie = self.caracs["force"] * self.niveau * 10

    def recalcul_vie(self, montant, ordre):
        if ordre == "retrait":
            self.vie -= montant
        else:
            self.vie += montant


class PersonnageJoueur(Personnage):
    NIVEAUX = [60, 120, 240, 480, 960]

    def __init__(self):
        self.niveau = 1
        self.experience = 1

    def afficher_niveau_personnage(self):
        print(f"Votre niveau est de {self.niveau}")

    def monter_niveau(self):
        self.experience += random.randint(1, 30)
        for i in range(len(self.NIVEAUX)):
            if self.experience > self.NIVEAUX[i]:
                self.niveau += 1
                self.calcul_vie()
                print(f"Bravo vous venez de prendre un niveau, vous êtes maintenant niveau {self.get_niveau()}")
                print(f"Vous avez maintenant {self.get_vie()} de vie")



class PersonnageNonJoueur(Personnage):
    def __init__(self, nom, niveau_min, niveau_max, classe, qualite=qualite_monstre[0]):
        self.nom = nom
        self.classe = classe
        self.niveau_min = niveau_min
        self.niveau_max = niveau_max
        self.niveau = random.randint(niveau_min, niveau_max)
        self.qualite = qualite
        self.calcul_vie()
        print(f"{self.nom} de niveau {self.niveau} et de classe {self.classe} est apparu")

    def afficher_niveau_pnj(self):
        print(f"Son niveau est de {self.niveau}")

    def afficher_classe_pnj(self):
        print(f"Son classe est {self.classe}")

    def afficher_informations_personnage(self):
        super().afficher_informations_personnage()
        print(f"Le pnj est de qualité {self.qualite}")



class Guerrier(PersonnageJoueur):
    caracs = {"force": 8, "mana": 1, "dextérité": 1}

    def __init__(self, nom):
        self.nom = nom
        self.classe = "Guerrier"
        self.niveau = 1
        self.experience = 1
        self.vie = self.caracs["force"] * self.niveau * 10

    def monter_niveau(self):
        super().monter_niveau()



class Mage(PersonnageJoueur):
    caracs = {"force": 1, "mana": 8, "dextérité": 1}

    def __init__(self, nom):
        self.nom = nom
        self.classe = "Mage"


class Voleur(PersonnageJoueur):
    caracs = {"force": 3, "mana": 1, "dextérité": 6}

    def __init__(self, nom):
        self.nom = nom
        self.classe = "Voleur"


class Combat:
    def __init__(self, pj: Personnage, pnj: Personnage):
        self.ecart_niveau = None
        self.bonus_malus = None
        self.pj = pj
        self.pnj = pnj
        print(f"Vous combattez contre {self.pnj.get_nom()}")

    def attaquer(self, attaquant: Personnage, defenseur: Personnage):
        self.ecart_niveau = attaquant.get_niveau() - defenseur.get_niveau()
        if self.ecart_niveau >= 5:
            print("Gros bonus")
            self.bonus_malus = 0.1
        elif self.ecart_niveau >= 2:
            print("Petit bonus")
            self.bonus_malus = 0.3
        elif -1 <= self.ecart_niveau >= 1:
            print("pas de bonus ni de malus")
            self.bonus_malus = 0
        elif -4 <= self.ecart_niveau <= -2:
            print("Petit malus")
            self.bonus_malus = 0.6
        elif self.ecart_niveau <= -5:
            print("Gros malus")
            self.bonus_malus = 0.9

        print(f"self.bonus_malus : {self.bonus_malus} self.ecart_niveau : {self.ecart_niveau}")
        print(f"Malus d'attaque : {attaquant.get_force()} * {self.bonus_malus} = {attaquant.get_force() * self.bonus_malus}")

        defenseur.recalcul_vie(attaquant.get_force() - (round(attaquant.get_force() * self.bonus_malus)), "retrait")
        if defenseur.get_vie() < 1:
            print(f"{defenseur.get_nom()} est mort !")
        else:
            print(f"{defenseur.get_nom()} n'a plus que {defenseur.get_vie()} de vie")


def creation_personnage():
    nom = input("Quel est le nom de votre personnage ? ")
    print("Merci de choisir votre classe parmis les classes suivantes :")
    for i in range(len(classes)):
        print(str(i) + ". " + classes[i] + " ")
    classe_choisis = int(input("Votre classe ? "))
    classe = classes[classe_choisis]
    # Personnage(nom, classe)
    if classe == 'Guerrier':
        personnage = Guerrier(nom)
    elif classe == 'Mage':
        personnage = Mage(nom)
    elif classe == "Voleur":
        personnage = Voleur(nom)
    else:
        print("ne rien faire")

    return personnage


def creation_monstre():
    # PersonnageNonJoueur(monstres[random.randint(0, 3)], 1, 10, "Guerrier", 60)
    nom = monstres[random.randint(0, len(monstres) - 1)]
    if int(personnage1.get_niveau() - 10) < 1:
        niveau_min = 1
    else:
        niveau_min = int(personnage1.get_niveau() - 10)
    niveau_max = int(personnage1.get_niveau() + 10)
    classe = "Guerrier"

    monstre = PersonnageNonJoueur(nom, niveau_min, niveau_max, classe,
                                  qualite_monstre[random.randint(0, len(qualite_monstre) - 1)])

    return monstre


# Début du jeu
boucle = True

while boucle:
    print("Bienvenue dans le jeu")
    print()
    print("Voici le menu principal :")
    print("1. Commencer le jeu")
    print("2. Quitter le jeu")
    print()
    choix = 0
    while choix != 1 and choix != 2:
        choix = int(input("Que voulez-vous faire ? (1 ou 2)"))

    if choix == 1:
        personnage1 = creation_personnage()
        personnage1.afficher_informations_personnage()
        boucle2 = True
        while boucle2:
            # personnage1.monter_niveau()
            # personnage1.afficher_niveau_personnage()
            print()
            print("Que voulez vous faire ? ")
            print("1. Accéder au menu principal")
            print("2. Monter de niveaux")
            print("3. Afficher les informations de votre personnage")
            print("4. Chasser des monstres")
            print()
            choix_du_personnage = int(input())
            if choix_du_personnage == 1:
                boucle2 = False
            elif choix_du_personnage == 2:
                personnage1.monter_niveau()
            elif choix_du_personnage == 3:
                personnage1.afficher_informations_personnage()
            elif choix_du_personnage == 4:
                monstre_a_chasser = creation_monstre()
                monstre_a_chasser.afficher_informations_personnage()
                menu_chasse_aux_monstre = True
                while menu_chasse_aux_monstre:
                    print()
                    print("Que voulez vous faire ? ")
                    print("1. Accéder au menu principal")
                    print("2. Attaquer le monstre")
                    print()
                    menu_chasse_aux_monstre_choix = int(input())
                    if menu_chasse_aux_monstre_choix == 1:
                        monstre_a_chasser = ""
                        menu_chasse_aux_monstre = False
                    elif menu_chasse_aux_monstre_choix == 2:
                        combat = Combat(personnage1, monstre_a_chasser)
                        combat.attaquer(personnage1, monstre_a_chasser)
                        combat.attaquer(monstre_a_chasser, personnage1)
                        if personnage1.get_vie() < 1:
                            print(f"Vous êtes mort !")
                        elif monstre_a_chasser.get_vie() < 1:
                            monstre_a_chasser = ""
                            menu_chasse_aux_monstre = False
    elif choix == 2:
        print()
        print("Merci !")
        boucle = False
