class LigneTicket:
    def __init__(self, produit: Produit, quantite):
        self.produit = produit
        self.quantite = quantite

    @property
    def total(self):
        return (1 + self.produit.tva) * self.produit.prix * self.quantite
    
    def __str__(self):
        return f"{self.produit} X {self.quantite} = {self.total}€ TVAC" 
        
        