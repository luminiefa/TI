class Voiture :
    def __init__(self, proprio, immatriculation, num_chassis) :
        self.proprio = proprio
        self.immatriculation = immatriculation
        self.num_chassis = num_chassis
        self.essence = 0
        self.km = 0

    def plein_essence(self, quantité) :
        self.essence = quantité

    def trajet(self, distance) :
        consommation = 0.06 * distance
        if consommation < self.essence :
            self.km = distance
        else:
            print("erreur")

    # problème ici si l'entretien a été fait faut reset la distance à chaque entretien
    def prochain_entretient(self) :
        distance_entretien = 15000
        return distance_entretien - self.km
    
    def __str__(self) :
        return "Voiture "
        + str(self.immatriculation) + " " + "de" 
        + " " + self.proprio + "[" + str(self.km) + "]"
        + "- essence: " + str(self.essence) + " "
        + "prochain entretient dans" + str(self.prochain_entretient)
            