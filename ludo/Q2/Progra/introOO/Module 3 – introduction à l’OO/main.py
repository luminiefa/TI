#A. Réflexion
#1
#2
#3
#4
#5
#6
#7
#B. Un peu de modélisation
## Quelles critiques/remarques pouvez-vous faire sur ces classes ?
## Comment doit-on lire les associations suivantes :
## Modélisez sous la forme de diagrammes UML chacun des points
## Université
#C. Traduire des classes en python
##1. Animal
class Animal :

    def __init__ (self, nom, race, poids, date_naissance) :
        self.nom = nom
        self.race = race
        self.poids = poids
        self.date_naissance = date_naissance
    
    def afficher_résumé(self):
        print("Nom: ",self.nom,", Race: ",self.race,", Poids :",self.poids,", Naissance :",self.date_naissance)

a = Animal("Bob","Chat",12,"21/02/23")

Animal.afficher_résumé(a)
##2. Voiture
class Voiture :

    def __init__(self, proprio, immatriculation, num_chassis) :
        self.proprio = proprio
        self.immatriculation = immatriculation
        self.num_chassis = num_chassis
        self.essence = 0
        self.km = 0
        self.consommation = 0.06

    def plein_essence(self, att) :
        self.essence += att
        
    def trajet(self, km) :
        if self.essence < self.consommation*km :
            print("Erreur, il n'y a pas assez d'essence.")
        else :
            self.km += km
            self.essence += -self.consommation*km

    def prochain_entretient(self) :
        15000-self.km

    def __str__(self) :
        return "Voiture "+self.immatriculation+" de "+self.proprio+" ["+str(self.km)+"] - essence : "+str(self.essence)+" - prochain entretient dans "+str(15000-self.km)+"km"

exemple = Voiture("Mathias","1-abc-123","BR46")

Voiture.plein_essence(exemple, 400)
Voiture.trajet(exemple, 200)
Voiture.prochain_entretient(exemple)

print(exemple.__str__())
##3. Personnage
class Personnage :

    def __init__(self, nom, classe, race, points_vie=20, points_dégat=2, points_armure=1) :
        self.nom = nom
        self.classe = classe
        self.race = race
        self.points_vie = points_vie
        self.points_dégat = points_dégat
        self.points_armure = points_armure

    def __str__(self) :
        return "Nom: "+self.nom+", Classe: "+self.classe+", Race: "+self.race+", Points de vie: "+str(self.points_vie)+", Points de dégat: "+str(self.points_dégat)+", Points d'armure: "+str(self.points_armure)

    def subit(self,dégats) :
        self.points_vie -= max(dégats-self.points_armure,0)
        #max(x,0) = 0 si négative

    def tape(self, quelquun) :
        quelquun.points_vie -= max(self.points_dégat-quelquun.points_armure,0)
        
    def est_mort(self) :
        return self.points_vie <= 0


if __name__ == "__main__" :

    gentil = Personnage("Mathias","Chevalier","Humain",20,4)
    méchant = Personnage("Saihtam","Guerrier","Monstre")
    print(gentil.__str__())
    print(méchant.__str__())

    while not ( Personnage.est_mort(gentil) or Personnage.est_mort(méchant) ) :
        Personnage.tape(gentil, méchant)
        Personnage.tape(méchant, gentil)
        print(gentil.__str__())
        print(méchant.__str__())
#D. Système de gestion de location de propriétés
##Manque la structure dans l'ex
class Person :
    def __init__(self, name:str) :
        self.name = name
        self.home = None
        self.possessions = []

    def __str__(self) :
        return self.name+" ("+self.address+")"
    
    @property
    def is_owner(self) :
        return True if self.possessions != [] else False

    @property
    def address(self) :
        return self.home.building.address

    def show_possessions_details(self) :
        for possession in self.possessions :
            possession.show_details()


class Building :
    def __init__(self, address:str) :
        self.address = address
        self.properties_list = []

    def __str__(self) :
        return "Building "+self.address+" ("+str(self.nb_properties)+")"

    def add_property(self, property) :
        self.properties_list.append(property)
        property.building = self

    @property
    def nb_properties(self) :
        return len(self.properties_list)


class Property :
    def __init__(self, number:int=None, garage:bool=False) :
        self.number = number #if None => House
        self.garage = garage
        self.building = None
        self.owner = None
        self.occupiers = []

    def __str__(self) :
        return ("House "+self.building.address) if self.number is None else ("Apartment "+str(self.number)+", "+self.building.address)

    def add_owner(self, person) :
        self.owner = person
        person.possessions.append(self)

    def add_occupiers(self, person) :
        self.occupiers.append(person)
        person.home = self

    def show_details(self) :
        print( "--- "+self.__str__()+" ---" )
        print("Owner : "+self.owner.name+" ("+self.owner.address+")")
        print("Occupiers :")
        for occupier in self.occupiers :
            print("- "+occupier.name)
        print("Garage : YES") if self.garage == True else print("Garage : NO")
        return None if self.number is None else print("Nb Apart in Building : "+str(self.building.nb_properties))

    def sale_to(self, new_owner) :
        self.owner.possessions.remove(self)
        self.owner = new_owner
        new_owner.possessions.append(self)

    

b1 = Building("Commonstreet nb 5")
b2 = Building("Magicstreet nb 18")
ap1 = Property(1, False)
ap2 = Property(2, False)
ap3 = Property(3, False)
ap4 = Property(4, False)
h = Property(None, True)
bob = Person("Bob")
alice = Person("Alice")
bobby_jr = Person("Bobby Jr")
chris = Person("Chris")
david = Person("David")
elen = Person("Elen")

b1.add_property(ap1)
b1.add_property(ap2)
b1.add_property(ap3)
b1.add_property(ap4)
b2.add_property(h)
h.add_occupiers(bob)
h.add_occupiers(alice)
h.add_occupiers(bobby_jr)
ap1.add_occupiers(chris)
ap3.add_occupiers(david)
ap4.add_occupiers(elen)
h.add_owner(bob)
ap1.add_owner(bob)
ap2.add_owner(bob)
ap3.add_owner(david)
ap4.add_owner(elen)

ap2.sale_to(elen)


print("Bob : ")
bob.show_possessions_details()
print("Elen : ")
elen.show_possessions_details()
## Transformation du schéma
## Traduire en classes Python
#E. Exercice supplémentaire : Jeu du labyrinthe magique
##Manque structure dans l'ex
"""
Jeu du labyrinthe magique

Replay WIP
"""

import random

class Board :
    def __init__(self, size:int=6) :
        self.size = size
        self.wall = [] #liste tuples
        self.player = None
        self.score_list = []

    def draw(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i,j) == self.player.position :
                    print("O", end=" ")
                elif (i,j) in self.wall :
                    print("X", end=" ") 
                else :
                     print(".", end=" ") 
            print()

    def pop_wall(self) :
        new_wall = (random.randrange(0, self.size, 1),random.randrange(0, self.size, 1))
        while new_wall in self.wall or new_wall == (0,0) or new_wall == (self.size-1,self.size-1) :
            new_wall = (random.randrange(0, self.size, 1),random.randrange(0, self.size, 1))
        self.wall.append(new_wall)

    def check_death(self) :
        is_dead = False
        for wall in self.wall :
            if self.player.position == wall : is_dead = True
        if self.player.position[0] == -1\
        or self.player.position[1] == -1\
        or self.player.position[0] == self.size\
        or self.player.position[1] == self.size :
            is_dead = True
        return is_dead

    def check_win(self) :
        return self.player.position == (self.size-1, self.size-1)
    
    def best_player(self) :
        best_score = float('-inf')
        best_player = None  
        for score in self.score_list:
            for player, score_player in score.items():
                if score_player > best_score:
                    best_score = score_player
                    best_player = player
        return best_player

    def play_game(self) :
        print("Hello "+self.player.name+" !")
        while self.check_death() == False and self.check_win() == False :
            self.pop_wall()
            self.draw()
            self.player.move()
            self.player.score -= 1
        if self.check_death() == True :
            print("you are dead, noob")
            print("Your score is : 0")
            self.score_list.append({self.player.name : 0})
            print("The actual best player is "+str(self.best_player())+" !")
        elif self.check_win() == True :
            print("GG, well play")
            print("Your score is : "+str(self.player.score))
            self.score_list.append({self.player.name : self.player.score})
            print("The actual best player is "+str(self.best_player())+" !")          


class Player :
    def __init__(self, name:str) :
        self.name = name
        self.position = (0,0)
        self.keyboard_key = {"z":(-1,0), "d":(0,1), "s":(1,0), "q":(0,-1)}
        self.board = None
        self.score = 30

    def move(self) :
        move = self.keyboard_key[str(input(">>> "))]
        while self.position[0] + move[0] == -1\
        or self.position[1] + move[1] == -1\
        or self.position[0] + move[0] == self.board.size\
        or self.position[1] + move[1] == self.board.size :
            print("Error")
            move = self.keyboard_key[str(input(">>> "))]
        self.position = (self.position[0] + move[0], self.position[1] + move[1])


if __name__ == "__main__" :
    is_want_replay = None

    #Créé nouveau joueur
    player_name = str(input("Enter a player name : "))
    player = Player(player_name)

    #Setup la partie
    game = Board(size=7)
    game.player = player
    player.board = game
    keyboard_key = {"z":(-1,0), "d":(0,1), "s":(1,0), "q":(0,-1)}
    game.play_game()

    #Replay
    is_want_replay = None
    is_want_replay = str(input("Play again ? (y/n): "))
    while is_want_replay != "y" or is_want_replay != "n" :
        is_want_replay = str(input("Play again ? (y/n): "))

        #Créé nouveau joueur
        player_name = str(input("Enter a player name : "))
        player = Player(player_name)

        #Setup la partie
        game.wall.clear()
        game.player = player
        player.board = game
        keyboard_key = {"z":(-1,0), "d":(0,1), "s":(1,0), "q":(0,-1)}
        game.play_game()

        #Replay
        is_want_replay = None
        is_want_replay = str(input("Play again ? (y/n): "))
        while is_want_replay != "y" or is_want_replay != "n" :
            is_want_replay = str(input("Play again ? (y/n): "))
##1. Squelette
##2. Dessiner le plateau
##3. Faire bouger le joueur
##4. Petit test
##5. Faire apparaitre des murs au hasard
##6. Vérifier la victoire ou la défaite
##7. Jouer (enfin presque)
##8. Jouez (vraiment ce coup-ci)
##Quelques questions
##Pour aller plus loin..