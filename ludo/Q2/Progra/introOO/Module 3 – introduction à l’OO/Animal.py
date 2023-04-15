class Animal :
    def __init__(self, nom, race, poids, date_naissance) :
        self.nom = nom
        self.race = race
        self.poids = poids
        self.date_naissance = date_naissance

    def afficher_résumé(self) :
        # il faut caster le poids en string
        print(self.nom + "(" + self.race + ")" + "né le " + self.date_naissance + "pèse" + str(self.poids) + "kg")
