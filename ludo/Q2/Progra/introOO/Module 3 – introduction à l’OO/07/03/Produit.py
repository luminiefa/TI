class Produit:
    def __init__(self, ean, libelle, type, est_refrigere, prix, tva):
        self.ean = ean
        self.libelle = libelle
        self.type = type
        self.est_refrigere = est_refrigere
        self.prix = prix
        self.tva = tva
        
    def __str__(self):
        return f"{self.libelle} ()"