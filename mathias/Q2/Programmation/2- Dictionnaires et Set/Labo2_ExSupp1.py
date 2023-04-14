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

