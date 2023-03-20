from Animal import *
from Voiture import *

from Personnage import *

chien = Animal("médor", "labrador", 50, "02/03/2023")
chat = Animal("catou", "siamois", 5, "01/03/2023")

chien.afficher_résumé()
chat.afficher_résumé()

merco = Voiture("john", 55555555, 3434343434343)
audi = Voiture("Marie", 22222222, 11111111)

print(merco.immatriculation)

perso1 = Personnage("cac", "war", "orc", 100, 10, 2)
perso2 = Personnage("caster", "mago", "humain", 50, 20, 1)

perso1.tape(perso2)
perso1.tape(perso2)
perso1.tape(perso2)
perso1.tape(perso2)
print(perso2.point_vie)