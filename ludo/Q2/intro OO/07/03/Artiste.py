class Artiste:
    def __init__(self, nom, est_groupe):
        self.nom = nom
        self.est_groupe = est_groupe
        
    #({'' if condition else''})"
    def __str__(self):
        type = ""
        if self.est_groupe:
            type = "groupe"
        else:
            type = "solo"

        return f"{self.nom} ({type})"