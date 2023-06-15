# example pick by the game God of War in PS2
import random

class Personnage:
    # constructor
    def __init__(self, nom, points_de_vie, attaque):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque

    # function to attack hero or monster
    def attaquer(self, cible):
        degats = random.randint(1, self.attaque)
        cible.subir_degats(degats)
       
    # function to view the damage take by the hero or monster
    def subir_degats(self, degats):
        self.points_de_vie -= degats

    # function to regenerate the hero
    def steal_life (self, regenerate):
        self.points_de_vie += regenerate
    

# class Hero example of Kratos in God of War
class Heros(Personnage):
    def __init__(self, nom, points_de_vie, attaque):
        super().__init__(nom, points_de_vie, attaque)

# class Kratos with weapons: Axe, Lames
class Kratos(Heros):
    def __init__(self):
        super().__init__("Kratos", 100, 10)


# class Monster
class Monstre(Personnage):
    def __init__(self, nom, points_de_vie, attaque):
        super().__init__(nom, points_de_vie, attaque)

# extension of the class Monster with monsters:Gorgone, Cyclope, Minotaure
class Gorgone(Monstre):
    def __init__(self):
        super().__init__("Gorgone", 50, 5)

class Cyclope(Monstre):
    def __init__(self):
        super().__init__("Cyclope", 75, 10)

class Minotaure(Monstre):
    def __init__(self):
        super().__init__("Minotaure", 100, 15)

# extension of the class Hero with weapons: Axe, Lames
class AxeofLeviathan(Heros):
    def __init__(self):
        super().__init__("Kratos", 100, 10)
        # define the percentage sucess of the attack
        self.pourcentage = 1.0


class LamesofChaos(Heros):
    def __init__(self):
        super().__init__("Kratos", 100, 25)
        # define the percentage sucess of the attack
        self.pourcentage = 0.8

# extensions of the class Heros with magics attacks: wrathofPoseidon, thunderboltofZeus, armyofHades
class wrathofPoseidon(Heros):
    def __init__(self):
        super().__init__("Kratos", 100, 10)
        # define the percentage sucess of the attack
        self.possibility = 0.8

        # function to add supplementary damage betwween 10 and 25
    def degats_supplementaires(self):
        return random.randint(10, 25)
    

class thunderboltofZeus(Heros):
    def __init__(self):
        super().__init__("Kratos", 100, 25)

        # define the percentage sucess of the attack
        self.possibility = 0.7

        # function to allow the hero to not be attacked
    def esquiver(self):
        if random.random() < 0.3:
            # the hero is not attacked
            print("Kratos esquive l'attaque!")
            return True
        else:
            print("Kratos n'a pas esquivé l'attaque!")
            # the hero is attacked
            return False
    
class armyofHades(Heros):
    def __init__(self):
        super().__init__("Kratos", 100, 15)
        # define the percentage sucess of the attack
        self.possibility = 0.8

        # function to regenerate the hero
    def regenerate(self):
        return random.randint(10, 25)
    



# extensions of the class Monster with weapons: RegarddePierre, Massue, Cornes 
class RegarddePierre(Monstre):
    def __init__(self):
        super().__init__("Gorgone", 50, 5)
        # define the percentage sucess of the attack
        self.pourcentage = 0.8

class Massue(Monstre):
    def __init__(self):
        super().__init__("Cyclope", 75, 10)
        # define the percentage sucess of the attack
        self.pourcentage = 0.7

class Cornes(Monstre):
    def __init__(self):
        super().__init__("Minotaure", 100, 15)
        # define the percentage sucess of the attack
        self.pourcentage = 0.5




heros = Kratos()
monstres = [Gorgone(), Cyclope(), Minotaure()]
degats = random.randint(1, heros.attaque)
weapon = [AxeofLeviathan(), LamesofChaos()]
weapon_monstre = [RegarddePierre(), Massue(), Cornes()]
magic = [wrathofPoseidon(), thunderboltofZeus(), armyofHades()]
degats_supplementaires = wrathofPoseidon().degats_supplementaires()
esquiver = thunderboltofZeus().esquiver()
regenerate = armyofHades().regenerate()

# Game loop
while heros.points_de_vie > 0 and len(monstres) > 0:

    # Choose a monster
    monstre = random.choice(monstres)

    # Display the name of the monster which hero is facing
    print(f"{heros.nom} affronte {monstre.nom}!")

    # While the monster and the hero are alive
    while monstre.points_de_vie > 0 and heros.points_de_vie > 0:

        # Choose the attacks of the hero
        choix = input("Attaque légère (1) ou attaque puissante (2)? ")

        # Then Choose attack magic of the hero
        choix_magic = input("Colère de Poséidon  (1) ou Foudre de Zeus (2) ou Armée de Hadès (3)? ")


            # Attack of the hero Kratos with AxeofLeviathan weapon
        if choix == "1":
            # If attack magic is wrathofPoseidon 
            if choix_magic == "1":
                heros.attaquer(monstre)
                degats = random.randint(1, heros.attaque)
                degats = degats * weapon[0].pourcentage
                degats = degats * magic[0].possibility
            
            # Display the damage inflicted by the hero with AxeofLeviathan weapon plus wrathofPoseidon magic and display damage supplementaires
                print(f"{heros.nom} attaque {monstre.nom} et lui inflige {degats} points de dégâts avec l'arme {weapon[0].__class__.__name__} et la magie {magic[0].__class__.__name__}! {degats_supplementaires} points de dégâts supplémentaires!")

        # If attack magic is thunderboltofZeus with AxeofLeviathan
        elif choix_magic == "2":
            heros.attaquer(monstre)
            degats = random.randint(1, heros.attaque)
            degats = degats * weapon[0].pourcentage
            degats = degats * magic[1].possibility
            
            # Display the damage inflicted by the hero with AxeofLeviathan weapon plus thunderboltofZeus magic and display if the hero esquive the attack
            print(f"{heros.nom} attaque {monstre.nom} et lui inflige {degats} points de dégâts avec l'arme {weapon[0].__class__.__name__} et la magie {magic[1].__class__.__name__}! {esquiver} n'est pas touché!")

        # If attack magic is armyofHades with AxeofLeviathan
        elif choix_magic == "3":
            heros.attaquer(monstre)
            degats = random.randint(1, heros.attaque)
            degats = degats * weapon[0].pourcentage
            degats = degats * magic[2].possibility

           
            # Display the damage inflicted by the hero with AxeofLeviathan weapon plus armyofHades magic and display if the hero regenerate his life
            print(f"{heros.nom} attaque {monstre.nom} et lui inflige {degats} points de dégâts avec l'arme {weapon[0].__class__.__name__} et la magie {magic[2].__class__.__name__}! {regenerate} points de vies supplémentaires!")

     
            # Second attack of the hero Kratos with LamesofChaos weapon for heavy attack
        if choix == "2":
            # If attack magic is wrathofPoseidon with LamesofChaos
            if choix_magic == "1":
                heros.attaquer(monstre)
                degats = random.randint(1, heros.attaque)
                degats = degats * weapon[1].pourcentage
                degats = degats * magic[0].possibility

            # Display the damage inflicted by the hero with LamesofChaos weapon plus wrathofPoseidon magic and display damage supplementaires
                print(f"{heros.nom} attaque {monstre.nom} et lui inflige {degats} points de dégâts avec l'arme {weapon[1].__class__.__name__} et la magie {magic[0].__class__.__name__}! {degats_supplementaires} points de dégâts supplémentaires!")

            # If attack magic is thunderboltofZeus with LamesofChaos
        elif choix_magic == "2":
            heros.attaquer(monstre)
            degats = random.randint(1, heros.attaque)
            degats = degats * weapon[1].pourcentage
            degats = degats * magic[1].possibility

    
            # Display the damage inflicted by the hero with LamesofChaos weapon plus thunderboltofZeus magic and display if the hero esquive the attack
            print(f"{heros.nom} attaque {monstre.nom} et lui inflige {degats} points de dégâts avec l'arme {weapon[1].__class__.__name__} et la magie {magic[1].__class__.__name__}! {esquiver} !")
           

            # If attack magic is armyofHades with LamesofChaos
        elif choix_magic == "3":
            heros.attaquer(monstre)
            degats = random.randint(1, heros.attaque)
            degats = degats * weapon[1].pourcentage
            degats = degats * magic[2].possibility
                
            # Display the damage inflicted by the hero with LamesofChaos weapon and armyofHades magic and display if the hero regenerate his life
            print(f"{heros.nom} attaque {monstre.nom} et lui inflige {degats} points de dégâts avec l'arme {weapon[1].__class__.__name__} et la magie {magic[2].__class__.__name__}! {regenerate} points de vies supplémentaires!")

        else:
            print("Choix invalide!")
            continue

        # If the monster has no more life points, he dies
        if monstre.points_de_vie <= 0:

            # Display the death of the monster
            print(f"{heros.nom} a vaincu {monstre.nom}!")
            monstres.remove(monstre)
            break

        # If the monster is still alive, he attacks the hero with his weapon
        # If Gordone, she uses RegarddePierre
        if monstre.nom == "Gorgone":
            monstre.attaquer(heros)
            degats = random.randint(1, monstre.attaque)
            degats = degats * weapon_monstre[0].pourcentage

            # Display the damage inflicted by the monster with RegarddePierre weapon
            print(f"{monstre.nom} attaque {heros.nom} et lui inflige {degats} points de dégâts avec l'arme {weapon_monstre[0].__class__.__name__}!")

        # If Cyclope, he uses Massue
        elif monstre.nom == "Cyclope":
            monstre.attaquer(heros)
            degats = random.randint(1, monstre.attaque)
            degats = degats * weapon_monstre[1].pourcentage

            # Display the damage inflicted by the monster with Massue weapon
            print(f"{monstre.nom} attaque {heros.nom} et lui inflige {degats} points de dégâts avec l'arme {weapon_monstre[1].__class__.__name__}!")
        
        # If Minotaure, he uses Cornes
        elif monstre.nom == "Minotaure":
            monstre.attaquer(heros)
            degats = random.randint(1, monstre.attaque)
            degats = degats * weapon_monstre[2].pourcentage

            # Display the damage inflicted by the monster with Cornes weapon
            print(f"{monstre.nom} attaque {heros.nom} et lui inflige {degats} points de dégâts avec l'arme {weapon_monstre[2].__class__.__name__}!")
        


        # If the hero has no more life points, he dies
        if heros.points_de_vie <= 0:
            break

# Display the end of the game
if heros.points_de_vie > 0:
    print(f"{heros.nom} a vaincu tous les monstres!")
else:
    print(f"{heros.nom} a été vaincu!")
