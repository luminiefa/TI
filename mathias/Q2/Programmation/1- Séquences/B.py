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
