class Personnage:
    def __init__(self, nom, classe, race, point_vie=20, point_degat=2, point_armure=1):
        self.nom = nom
        self.classe = classe
        self.race = race
        self.point_vie = point_vie
        self.point_degat = point_degat
        self.point_armure = point_armure
        
    def subit(self, degats):
        degats_subis = degats - self.point_armure
        self.point_vie -= degats_subis
    
    def tape(self, personnage):
        personnage.subit(self.point_degat)
    
    def est_mort(self):
        return (self.point_vie <= 0)

    def __str__(self):
        return f"{self.nom} de la classe {self.classe}({self.point_vie})"