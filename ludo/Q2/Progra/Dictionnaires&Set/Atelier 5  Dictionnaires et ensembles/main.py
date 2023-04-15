#A. Réflexion
## Set
""" 1
Non, un set n'est pas une séquence car il n'a pas d'ordre défini. 
Les éléments d'un set sont stockés sans ordre particulier et ne peuvent pas être indexés comme dans une séquence. 
De plus, un set ne peut pas contenir de doublons.
"""

""" 2
Pour créer un set vide en Python, on peut utiliser la fonction set(), sans aucun argument. Voici un exemple :
"""
ensemble_vide = set()

""" 3
    Voici les résultats des expressions suivantes :

    {0,2,4,6} & {1,2,3,4} : Renvoie l'intersection de deux ensembles, c'est-à-dire l'ensemble des éléments communs aux deux ensembles. Ici, le résultat est {2, 4}.

    {0,2,4,6} - {1,2,3,4} : Renvoie la différence de deux ensembles, c'est-à-dire l'ensemble des éléments qui sont dans le premier ensemble mais pas dans le deuxième. Ici, le résultat est {0, 6}.

    {0,2,4,6} | {1,2,3,4} : Renvoie l'union de deux ensembles, c'est-à-dire l'ensemble de tous les éléments qui sont dans l'un ou l'autre des ensembles. Ici, le résultat est {0, 1, 2, 3, 4, 6}.

    2 in {0,2,4,6} : Vérifie si l'élément 2 est présent dans l'ensemble. Ici, le résultat est True.

    {2} in {0,2,4,6} : Vérifie si l'ensemble {2} est présent dans l'ensemble. Ici, le résultat est False car {2} n'est pas égal à {0, 2, 4, 6}.

    {2} <= {0,2,4,6} : Vérifie si tous les éléments de l'ensemble {2} sont également présents dans l'ensemble {0, 2, 4, 6}. Ici, le résultat est True car {2} est inclus dans {0, 2, 4, 6}.
"""
## Dictionnaires
"""
Ce qui est commun aux dictionnaires et aux sets est le fait qu'ils sont tous deux des types de données non séquentiels et mutables en Python. 
Cela signifie que les éléments qu'ils contiennent ne sont pas ordonnés et que les éléments peuvent être ajoutés, supprimés ou modifiés après leur création.
En outre, les sets et les dictionnaires ne peuvent pas contenir de doublons. 
Dans un set, chaque élément doit être unique et dans un dictionnaire, chaque clé doit être unique.
"""
#B. Exercices à implémenter
#Exercice1
def update_contact(contacts, name, mail):
    contacts.update(dict([(name, mail)]))
contacts = {"nom1":"adresse1"}
name = "nom2"
mail = "adresse2"
print(contacts)
update_contact(contacts, name, mail)
print("----------------------------")
print(contacts)
#Exercice2
def print_mail(contacts, name):
    print(contacts[name])
contacts = {'nom1': 'adresse1', 'nom2': 'adresse2'}
print_mail(contacts, "nom2")
#Exercice3
def print_all(contacts):
    for tup in contacts.items():
        print("Nom: ", tup[0], " - Mail: ", tup[1])
contacts = {'nom1': 'adresse1', 'nom2': 'adresse2'}
print_all(contacts)
#Exercice4
def update_contact(contacts, name, mail):
    contacts.update(dict([(name, mail)]))
def print_all(contacts):
    for tup in contacts.items():
        print("Nom: ", tup[0], " - Mail: ", tup[1])
contacts = {}
update_contact(contacts,"Smal","anne.smal@henallux.be")
update_contact(contacts,"Valentin","didier.valentin@henallux.be")
update_contact(contacts,"Duvillé","guillerme.duville@henallux.be")
update_contact(contacts,"Schovaers","corentin.schovaers@henallux.be")
print_all(contacts)
#Exercice5
def dict_count(word):
    dictionary = {}
    letters = []
    for letter in word:
        letters.append(letter)
    i = 0
    while i < len(letters):
        dictionary.update(dict([(letters[i], letters.count(letters[i]))]))
        i += 1
    return dictionary

word = "hello"
print(dict_count(word))
#Exercice6
def  common_people(ensemble1, ensemble2):
    return ensemble1 & ensemble2
#Exercice7
def xor(ensemble1, ensemble2):
    return ( ensemble1 | ensemble2) - ( ensemble1 & ensemble2)
print ( xor({0,1,2,3,4,5}, {1,2}) )
#Exercice8
def common_pairs(dico1, dico2):
    return [( dico1.items() & dico2.items() )]
dico1 = {"Pain" : 4, "Fraises" : 3, "Chips" : 2, "Chocolat" : 1}
dico2 = {"Pain" : 4, "Fraises" : 3, "Lait" : 5}
print(common_pairs(dico1, dico2))
#Exercice9
def dict_count(word):
    dictionary = {}
    letters = []
    for letter in word:
        letters.append(letter)
    i = 0
    while i < len(letters):
        dictionary.update(dict([(letters[i], letters.count(letters[i]))]))
        i += 1
    return dictionary
def nb_different_char(word):
    return len(dict_count(word))

word = "hello"
print(nb_different_char(word))
#C. Exercices supplémentaires
#Exercice1
def print_all(dictionary):
    for item, quantity in dictionary.items():
        print(item, " : ", quantity)

dictionary = {}
item = input("Entrer un produit : ")
while item != "fini":
    quantity = int(input("Entrer sa quantité : "))
    if item in dictionary:
        dictionary[item] += quantity
    else:
        dictionary[item] = quantity
    item = input("Entrer un produit : ")

print_all(dictionary)
#Exercice2
##1
{
    "nom": "Formatique",
    "année_naissance": 1998,
    "sexe": "G",
    "annee_arrivee": 2017,
    "points_premiere_session": 15,
    "points_deuxieme_session": 15
}
##2
def demander_informations_personne():
    personne = {}
    personne["nom"] = input("Entrez le nom de la personne : ")
    personne["année_naissance"] = int(input("Entrez l'année de naissance de la personne : "))
    personne["sexe"] = input("Entrez le sexe de la personne (F, G ou A) : ")
    personne["annee_arrivee"] = int(input("Entrez l'année d'arrivée de la personne : "))
    personne["points_premiere_session"] = int(input("Entrez les points obtenus en première session : "))
    if personne["points_premiere_session"] >= 10:
        personne["points_deuxieme_session"] = 0
    else:
        personne["points_deuxieme_session"] = int(input("Entrez les points obtenus en deuxième session : "))
    return personne
##3
personnes = [
    {
        "nom": "Compranrien",
        "année_naissance": 1998,
        "sexe": "F",
        "annee_arrivee": 2017,
        "points_premiere_session": 4,
        "points_deuxieme_session": 8
    },
    {
        "nom": "Honette",
        "année_naissance": 1999,
        "sexe": "F",
        "annee_arrivee": 2017,
        "points_premiere_session": 10,
        "points_deuxieme_session": 10
    },
    {
        "nom": "Wiperdu",
        "année_naissance": 1999,
        "sexe": "F",
        "annee_arrivee": 2017,
        "points_premiere_session": 13,
        "points_deuxieme_session": 13
    },
    {
        "nom": "Formatique",
        "année_naissance": 1998,
        "sexe": "G",
        "annee_arrivee": 2017,
        "points_premiere_session": 15,
        "points_deuxieme_session": 0
    },
    {
        "nom": "Rémalin",
        "année_naissance": 1995,
        "sexe": "G",
        "annee_arrivee": 2017,
        "points_premiere_session": "Signé",
        "points_deuxieme_session": 10
    }
]
##4
def display_person_info(students, name):
    for student in students:
        if student['name'] == name:
            print(f"Nom : {student['name']}\n"
                  f"Prénom : {student['first_name']}\n"
                  f"Année de naissance : {student['birth_year']}\n"
                  f"Sexe : {student['gender']}\n"
                  f"Année d'arrivée : {student['arrival_year']}\n"
                  f"Points en première session : {student['first_session_points']}\n"
                  f"Points en seconde session : {student['second_session_points']}\n")
            break
##5
def mean_first_session(students):
    sum_points = 0
    num_students = 0
    for student in students:
        if 'first_session_points' in student:
            sum_points += student['first_session_points']
            num_students += 1
    if num_students == 0:
        return 0
    else:
        return sum_points / num_students
##6
def best_student(students):
    max_points = -1
    best_student_name = ""
    for student in students:
        if 'first_session_points' in student and student['first_session_points'] > max_points:
            max_points = student['first_session_points']
            best_student_name = student['name']
    return best_student_name
##7
def best_by_year(students):
    best_students = {}
    for student in students:
        year = student['arrival_year']
        if year in best_students:
            if 'first_session_points' in student and student['first_session_points'] > best_students[year]['points']:
                best_students[year] = {'name': student['name'], 'points': student['first_session_points']}
        else:
            best_students[year] = {'name': student['name'], 'points': student['first_session_points']}
    return best_students
##8
class Student:
    def __init__(self, firstname, lastname, birthyear, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.grade = grade

students = {
    2018: [Student("Gene", "Doe", 2001, 10),
           Student("Camille", "Honette", 2000, 16),
           Student("Jess", "Lee", 1999, 12),
           Student("Alain", "Turing", 2002, 8),
           Student("Pat", "Smith", 2001, 14)],
    2019: [Student("Gene", "Doe", 2001, 14),
           Student("Camille", "Honette", 2000, 18),
           Student("Jess", "Lee", 1999, 16),
           Student("Alain", "Turing", 2002, 12),
           Student("Pat", "Smith", 2001, 20),
           Student("Marie", "Honette", 2000, 12)]
}
##9
def print_student_info(student_records, first_name, last_name):
    for student in student_records:
        if student["first_name"] == first_name and student["last_name"] == last_name:
            print("First Name:", student["first_name"])
            print("Last Name:", student["last_name"])
            print("Year of Entry:", student["year"])
            print("Session 1 Score:", student["session1"])
            print("Session 2 Score:", student["session2"])
            break
    else:
        print("No student found with that name.")
