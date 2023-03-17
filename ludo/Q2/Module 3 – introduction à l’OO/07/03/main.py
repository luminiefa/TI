from Artiste import *
from Chanson import *
from Album import *

vangog = Artiste("vangog", True)
chanson1 = Chanson("titre1", 60, vangog)
album1 = Album("titre1", "mars", "rock", 40, 1, chanson1)

print(album1.chanson.artiste.nom)