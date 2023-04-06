#A. Réflexion
## Set

## Dictionnaires

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
#PAS TERMINÉ

def print_all(dictionary):
    for tup in dictionary.items():
        print(tup[0], " : ", tup[1])

def common_pairs(dico1, dico2):
    return [( dico1.items() & dico2.items() )]

dictionary = {}

item = input("Entrer un produit : ")
while item != "fini":
    quantity = input("Entrer sa quantité : ")
    dictionary[item] = quantity
    item = input("Entrer un produit : ")

print_all(dictionary)
#Exercice2
