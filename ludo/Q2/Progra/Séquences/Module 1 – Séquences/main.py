#A. Exercices de réflexion
#Exercice 1
#Exercice 2
#Exercice 3
#Exercice 4
"""1
    t[1] = "Bobby" : une erreur de type TypeError sera levée, car les tuples sont immuables et ne peuvent pas être modifiés une fois créés.
    l[4] = min(t) : une erreur de type TypeError sera levée, car les types de données ne sont pas compatibles, car t est un tuple et l est une liste.
"""
"""2
("Alice", "Bob", "Chris") : le tuple t reste inchangé car il est immuable.
"Hlowrd!": chaque deuxième caractère de la chaîne s est affiché.
[0, 2, 3, 4, -1, "Alice", "Bob", "Chris"] : la liste l a été modifiée avec l'assignation de l[0] et l[-1] et la concaténation de l et t.
2 : le nombre d'éléments dans le tuple t.
"""
#B. Exercices à implémenter
#Exercice 1
def is_empty(sequence) :
    return len(sequence) == 0

#Exercice 2
def print_max(sequence) :

    if is_empty(sequence) == True :
        print("Problème: La séquence est vide")

    else :
        print(max(sequence))
    
#Exercice 3
def is_in_list(element, list) :
    return element in list

#Exercice 4
def reverse_str(str) :
    return str[::-1]

#Exercice 5
def list_without_zero(list) :
    new_list = []
    i = 0
    while i < len(list) :
        if list[i] == 0 : new_list.append(1)
        else : new_list.append(list[i])
        i += 1
    return new_list

#Exercice 6
def lower_case(word) :
    lower_case_word = []
    i = 0
    while i < len(word) :
        if 65 <= ord(word[i]) <= 90 : 
            lower_case_word.append( chr(ord(word[i])+32) )
        else :  lower_case_word.append(word[i])
        i += 1
    return ''.join(lower_case_word)

#Exercice 7
def negatives_removed(list) :
    new_list = []
    i = 0
    while i < len(list) :
        if list[i] >= 0: new_list.append(list[i])
        i += 1
    return new_list

#Exercice 8
def students_list() :
    list = []
    name = str(input("Entrer un nom ('fini' pour terminer): "))
    while name != "fini" :
        list.append(name)
        name = str(input("Entrer un nom ('fini' pour terminer): "))    
    return list
#Exercice 9
students_list = ["Alice", "Bob", "Chris", "David", "Emma", "Frank"]
students_dict = {student: False for student in students_list}

print("Liste des étudiants :")
print(students_list)

while True:
    name = input("Entrez le nom d'un étudiant (ou 'fini' pour terminer) : ")
    if name.lower() == "fini":
        break
    if name in students_dict:
        students_dict[name] = True
        print(f"{name} est dans la liste.")
    else:
        print(f"{name} n'est pas dans la liste.")

print("Récapitulatif :")
for name, present in students_dict.items():
    if not present:
        print(f"{name} n'a pas été cité.")

#Exercice 10
## La fonction pour chiffrer un message :
def chiffrer(message):
    chaine_paire = message[::2]  # caractères d'indice pair
    chaine_imp = message[1::2]  # caractères d'indice impair
    return (chaine_paire, chaine_imp)
## La fonction pour déchiffrer un message :
def dechiffrer(chaine_paire, chaine_imp):
    # On suppose que les deux chaînes ont la même longueur
    message = ""
    for i in range(len(chaine_paire)):
        message += chaine_paire[i] + chaine_imp[i]
    # Si la chaîne impaire est plus longue que la chaîne paire, on ajoute le dernier caractère de la chaîne impaire
    if len(chaine_imp) > len(chaine_paire):
        message += chaine_imp[-1]
    return message
## Le script pour utiliser ces fonctions :
message = input("Entrez un message à chiffrer : ")
chaine_paire, chaine_imp = chiffrer(message)
print("Chaine paire : ", chaine_paire)
print("Chaine impaire : ", chaine_imp)
message_dechiffre = dechiffrer(chaine_paire, chaine_imp)
print("Message déchiffré : ", message_dechiffre)
#Exercices supplémentaires
#Exercice 1
def is_palindrome(string):
    return string == string[::-1]
#Exercice 2
def get_weekday(num):
    days = {1: "Lundi", 2: "Mardi", 3: "Mercredi", 4: "Jeudi", 5: "Vendredi", 6: "Samedi", 7: "Dimanche"}
    return days.get(num, "Invalid input")

# Exemple d'utilisation
print(get_weekday(3)) # "Mercredi"
print(get_weekday(8)) # "Invalid input"
#Exercice 3
students_list = [("Jean", "Dupont"), ("Marie", "Martin"), ("Pierre", "Durand")]

# Demander les prénoms des étudiants à rechercher
searched_names = []
name = input("Entrez un prénom d'étudiant (ou 'fini' pour terminer) : ")
while name != "fini":
    searched_names.append(name)
    name = input("Entrez un prénom d'étudiant (ou 'fini' pour terminer) : ")

# Vérifier si les prénoms se trouvent dans la liste
for name in searched_names:
    found = False
    for student in students_list:
        if student[0] == name:
            print(f"{name} se trouve dans la liste (c'est {student[1]} {student[0]})")
            found = True
            break
    if not found:
        print(f"{name} ne se trouve pas dans la liste")

# Adaptation pour gérer les étudiants avec le même prénom
students_list = [("Jean", "Dupont"), ("Marie", "Martin"), ("Pierre", "Durand"), ("Jean", "Martin")]

# Demander les prénoms des étudiants à rechercher
searched_names = []
name = input("Entrez un prénom d'étudiant (ou 'fini' pour terminer) : ")
while name != "fini":
    searched_names.append(name)
    name = input("Entrez un prénom d'étudiant (ou 'fini' pour terminer) : ")

# Vérifier si les prénoms se trouvent dans la liste
for name in searched_names:
    found = False
    for student in students_list:
        if student[0] == name:
            if found:
                print(f"{name} se trouve plusieurs fois dans la liste")
            else:
                print(f"{name} se trouve dans la liste (c'est {student[1]} {student[0]})")
                found = True
    if not found:
        print(f"{name} ne se trouve pas dans la liste")
#Exercice 4
##1
nombre = int(input("Entrez un nombre : "))

for i in range(1, 11):
    print(nombre, "x", i, "=", nombre*i)
##2
nombre = int(input("Entrez un nombre : "))

print(nombre, "x 1 =", nombre*1)
print(nombre, "x 2 =", nombre*2)
print(nombre, "x 3 =", nombre*3)
print(nombre, "x 4 =", nombre*4)
print(nombre, "x 5 =", nombre*5)
print(nombre, "x 6 =", nombre*6)
print(nombre, "x 7 =", nombre*7)
print(nombre, "x 8 =", nombre*8)
print(nombre, "x 9 =", nombre*9)
print(nombre, "x 10 =", nombre*10)
##3
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))

if nombre1 % 2 == 1:
    nombre1 += 1  # On arrondit à l'entier pair supérieur

for i in range(nombre1, nombre2+1, 2):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()  # Saut de ligne entre chaque table
#Exercice 5
def count_chars(s1, s2):
    count = 0
    for c in s1:
        count += s2.count(c)
    return count
#Exercice 6
import random

def random_sentence():
    sujets = ['mon chat', 'le pape', 'Johnny', 'Eden Hazard', 'un serpent', 'un magicien', 'mon voisin']
    verbes = ['chanteront', 'joueront', 'danseront', 'travailleront', 'feront un marathon']
    temps = ['Aujourd’hui', 'Dans cent ans', 'Demain', 'Quand les poules auront des dents']
    lieux = ['à Bruxelles', 'à l’école', 'au magasin', 'à la mer', 'chez moi', 'ici']
    objets = ['une balle', 'un tuba', 'un ananas', 'un sac à main', 'des palmes', 'de l’or']

    temps_choisi = random.choice(temps)
    sujets_choisis = random.sample(sujets, k=2)
    verbe_choisi = random.choice(verbes)
    objet_choisi = random.choice(objets)
    lieu_choisi = random.choice(lieux)

    sujet1, sujet2 = sujets_choisis[0], sujets_choisis[1]

    print(f"{temps_choisi}, {sujet1} et {sujet2} {verbe_choisi} avec {objet_choisi} {lieu_choisi}")

# Exemple d'utilisation
random_sentence()
#Exercice 7
def print_antipode(coords):
    if not (-90 <= coords[0] <= 90) or not (-180 <= coords[1] <= 180):
        print("Erreur: Coordonnées invalides")
        return
    lat, lon = coords[0], coords[1]
    antipode_lat = -1 * lat
    antipode_lon = (lon + 180) % 360 - 180
    antipode = (antipode_lat, antipode_lon)
    print(antipode)
#Exercice 8
import random

def merge_uniques(lst1, lst2):
    count = 0
    for elem in lst1:
        if elem not in lst2:
            lst2.append(elem)
            count += 1
    print("Liste fusionnée :", lst2)
    print("Nombre d'éléments ajoutés :", count)
#Exercice 9
courses = {}
produit = input("Entrez un produit : ")
while produit != "fini":
    quantite = int(input("Entrez la quantité : "))
    if produit in courses:
        courses[produit] += quantite
    else:
        courses[produit] = quantite
    produit = input("Entrez un produit : ")

print("Liste de courses : ")
for produit, quantite in courses.items():
    print(f"{produit} : {quantite}")
#Exercice 10
import math
def distance(coords1, coords2):
    lat1, lon1 = math.radians(coords1[0]), math.radians(coords1[1])
    lat2, lon2 = math.radians(coords2[0]), math.radians(coords2[1])
    R = 6378.0  # Rayon de la Terre en km
    d = R * math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(abs(lon1-lon2)))
    return d

coords1 = (48.8566, 2.3522)  # Paris, France
coords2 = (51.5072, -0.1276)  # Londres, Royaume-Uni
d = distance(coords1, coords2)
print(f"La distance entre Paris et Londres est d'environ {d:.1f} km.")

# Cela affichera : La distance entre Paris et Londres est d'environ 343.8 km.


