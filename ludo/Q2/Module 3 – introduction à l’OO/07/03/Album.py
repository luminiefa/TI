class Album:
    def __init__(self, titre, date_paruption, genre, chansons):
        self.titre = titre
        self.date_paruption = date_paruption
        self.genre = genre
        self.duree = duree
        self.nb_artistes = nb_artistes
        self.chansons = chansons
        
    @property
    def duree(self):
        duree_totale = 0

        for chanson in self.chansons:
            duree_totale += chanson.duree
        return duree_totale

    @property
    def nb_artistes(self):
        artistes = set()
        for chanson in chansons:
            artistes.add(chanson.artiste)

        return len(artistes)


        
