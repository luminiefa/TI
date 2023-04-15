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
