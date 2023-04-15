#Introduction à l’héritage
## • Complètez ce diagramme UML qui correspond à l’énoncé suivant :
## • Quelle(s) critique(s) pouvez-vous faire de cette solution ?
#L’héritage
## • Regardez si, dans la solution, il n’est pas possible de généraliser certaines choses.
## • Corrigez votre schéma pour y introduire l’héritage.
#Exercices
##A
"""
+-------------------+
|     Bâtiment      |
+-------------------+
| adresse           |
| propriétaire      |
| superficie        |
|-------------------|
| + afficherInfos() |
+-------------------+

       ^
       |
       |
+-------------------+                 +------------------+
|     Immeuble      |-----------------|      Bureau      |
+-------------------+                 +------------------+
| nbEtages          |                 | nomSociete       |
| nbAppartements    |                 +------------------+
|-------------------|
| + afficherInfos() |
+-------------------+
"""
##B
"""
+-------------------+
|     Animal        |
+-------------------+
| nom               |
| dateNaissance     |
| numéroPuce        |
| taille            |
| animalConcours    |
|-------------------|
| + dormir()        |
| + manger()        |
+-------------------+

       ^
       |
       |
+-------------------+                  +---------------+
|       Chien       |------------------|      Chat     |
+-------------------+                  +---------------+
|                   |                  | tailleOreilles|
+-------------------+                  +---------------+

       ^
       |
       |
+-------------------+
|      Lapin        |
+-------------------+
"""
##C
"""
+------------------+
|   Personnage     |
+------------------+
| nom              |
| force            |
| vie              |
| armure           |
|------------------|
| + attaquer()     |
| + prendreDegats()|
| + seSoigner()    |
+------------------+

       ^
       |
       |
+------------------+
|      Mage        |
+------------------+
| mana             |
|------------------|
| + attaqueMagique()|
+------------------+

       ^
       |
       |
+------------------+
|     Guerrier     |
+------------------+
| rage             |
|------------------|
| + attaqueEnragee()|
+------------------+

       ^
       |
       |
+------------------+
|     Chasseur     |
+------------------+
| animalCompagnie  |
|------------------|
| + attaqueChasse()|
+------------------+

       ^
       |
       |
+------------------+
|      Animal      |
+------------------+
|------------------|
| + sauter()       |
+------------------+
"""
#Rappel
## Rabbit (Lapin)
class Animal :
    def __init__(self, name, bd, ship_nb, size):
        self.name = name
        self.birthday = bd
        self.ship_nb = ship_nb
        self.size = size

    def sleep(self):
        print(self.name, ": ZzzzzzZzzzzz...")

    def eat(self):
        print(self.name, ": *Crounch*")


class Rabbit (Animal):
    def __init__(self, name, bd, ship_nb, size, ear_size):
        super().__init__(name, bd, ship_nb, size)
        self.ear_size = ear_size

    def jump(self):
        print(self.name, ": *Bwing*")
## Dog (Chien)
class Dog (Animal) :
    def __init__(self, name, bd, ship_nb, size):
        super().__init__(name, bd, ship_nb, size)
    def bark(self):
        print(self.name, ": WOOOUF !")
## Cat (Chat)
class Cat (Animal) :
    def __init__(slef, name, bd, ship_nb, size):
        super().__init__(name, bd, ship_nb, size)

    def meow(self) :
        print(self.name, ": Meeoooow")

    def purr(self) :
        print(self.name, ": *Purr*")

    def eat(self):
        self.purr()
        print(self.name, ": *Crounch*")
## Test
if __name__ == "__main__" :
    c = Cat("Tesla", "1/04/2017", 12568743, 35)
    d = Dog("Pixel", "16/10/2019", 58963217, 70)
    r = Rabbit("Pong", "11/02/2010", 25874136, 20,15)

    print(c.__dict__)
    print(d.__dict__)
    print(r.__dict__)

    c.sleep()
    d.sleep()
    r.sleep()

    c.eat()
    d.eat()
    r.eat()

    d.bark()
    c.meow()
    r.jump()
#Introduction aux exceptions

##Les exceptions sont des objets
###• Essayez le code suivant :

#try :
#    print("Bonjour")
#
#    num = int(input("Numérateur : "))
#    den = int(input("Dénominateur : "))
#    print(num,"/",den,"=",num/den)
#
#except ValueError as e:
#    print("Problème de valeur")
#    print(e.__dir__())
#    print(e.__str__())
#
#except ZeroDivisionError :
#    print("on ne peut pas diviser par 0 ! ")
#
#finally :
#    print("Merci et à bientôt")
###• Testez en faisant en sorte de faire une ValueError. Que se passe-t-il ?

class Mon_exception (Exception):
    def __init__(self, message:str="Message d'erreur") :
        self.message = message

    def __str__(self) :
        return self.message

try:
    n = int(input("Entrez un nombre entre 1 et 10 : "))
    if n>10 or n<1 :
        raise Mon_exception()
    print("ok")

except Mon_exception as e:
    print(e)
##Lancer une exception
try:
    x = int(input("Entrez un nombre entre 1 et 10 : "))
    if x < 1 or x > 10:
        raise Exception("Le nombre doit être entre 1 et 10")
except Exception as e:
    print("Erreur :", e)
"""
Si l'utilisateur entre un nombre en dehors de l'intervalle demandé (par exemple, 20), l'exception sera lancée et le message d'erreur "Le nombre doit être entre 1 et 10" sera affiché. Si l'utilisateur entre un nombre correct, aucune exception ne sera lancée et le programme continuera normalement.
"""