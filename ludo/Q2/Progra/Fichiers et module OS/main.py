#A. Réflexion
## Ouverture et lecture de fichier
## Le module OS et le système de fichiers
#B. Exercices à implémenter
## Exercice 1
def read(file) :
    with open (file,"r") as file :
        text = file.read()
        return text

def write(file, text) :
    with open (file,"w") as file :
        file.write(text)


if __name__ == "__main__" :

    write("exo1-2.txt", read("exo1-1.txt"))
## Exercice 2
import os

scan_iterator = os.scandir("test")
for elem in scan_iterator:

    if elem.is_dir():
        lenght = 0
        folder = os.scandir(elem)

        for files in folder :
            lenght += 1

        print(elem.name,"- dossier (",lenght,"fichiers)")

    else : print(elem.name)
    
scan_iterator.close()
## Exercice 3
import os

class FormatError(Exception) :
    def __init__(self, msg) :
        self.msg = msg

    def __str__(self) :
        return "Problème: "+self.msg

if __name__ == "__main__" :

    os.chdir("5- Fichiers et module OS")

    try :
        with open("descriptions.txt","r") as file :
            names = []
            for line in file :

                if len(line)-1 == 0 : raise FormatError("Le fichier contient au moins une ligne vide")
                elements = line.split(",")
                name = elements[0]
                
                if len(name) < 5 : raise FormatError("Un des nom est trop court")
                names.append(name)

    except FileNotFoundError : print("Le fichier n'existe pas")
    except FormatError as e : print(e.__str__())
    except : print("une erreur inconnue est survenue")

    finally : 
        for name in names : print(name)
#Exercices supplémentaires
import os
#import shutil
#
#shutil.move("5- Fichiers et module OS/test.txt", "5- Fichiers et module OS/test/test.txt")

def lower_case(word) :
    lower_case_word = []
    i = 0
    while i < len(word) :
        if 65 <= ord(word[i]) <= 90 : 
            lower_case_word.append( chr(ord(word[i])+32) )
        else :  lower_case_word.append(word[i])
        i += 1
    return ''.join(lower_case_word)

if __name__ == "__main__" :

    with open ("5- Fichiers et module OS/lorem-ipsum.txt","r") as file :
        text = file.read()

    word_list = text.split()
    new_word_list = []
    for word in word_list :
        new_word_list.append(lower_case(word))
    word_list = new_word_list

    counted = []
    for word in word_list :
        if word not in counted :
            print(word,":",word_list.count(word))
            counted.append(word)
    