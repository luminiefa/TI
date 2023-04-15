## Il n'y a pas une erreur de nommage fichier ?

import os

#try :
#    with open ("test.txt","r") as file :
#        for line in file :
#            print(line)
#            print(len(line)-1," caractères")
#
#except FileNotFoundError : print("Le fichier n'existe pas")


class FormatError (Exception) :
    def __init__(self, message) :
        self.message = message

    def __str__(self) :
        return "Problème : "+str(self.message)
    

if __name__ == "__main__" :

    os.chdir("4- Héritage et Exceptions")

    try :
        with open ("test.txt","r") as file :
            names = []
            for line in file :
                if len(line)-1 == 0 : raise FormatError("Le fichier contient au moins une ligne vide")
                elements = line.split(",")
                name = elements[0]
                if len(name) <= 5 : raise FormatError("Un des nom est trop court")
                names.append(name)

    except FileNotFoundError : print("Le fichier n'existe pas")
    except FormatError as e : print(e.__str__())
    except : print("une erreur inconnue est survenue")

    finally : 
        for name in names : print(name)
