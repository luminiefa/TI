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
