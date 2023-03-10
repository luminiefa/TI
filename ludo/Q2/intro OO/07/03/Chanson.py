class Chanson:
    def __init__(self, titre, duree, artiste):
        self.titre = titre
        self.duree = duree
        self.artiste = artiste
        
    def __str__(self):
        return f"{self.titre} interpretété par {self.artiste}({self.duree})"