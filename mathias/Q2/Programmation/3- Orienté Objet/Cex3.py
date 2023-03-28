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
