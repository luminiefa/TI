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
