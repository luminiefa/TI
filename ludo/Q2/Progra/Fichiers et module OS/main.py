#A. Réflexion
## Ouverture et lecture de fichier
"""
Les deux techniques permettent de lire le contenu d'un fichier et de l'afficher à l'écran.
Cependant, la deuxième méthode avec la syntaxe "with open..." est préférable car elle garantit la fermeture automatique du fichier,
même en cas d'exception ou d'erreur dans le code. En effet, l'instruction "with" gère automatiquement la gestion des erreurs et la fermeture du fichier,
tandis que la première méthode nécessite l'appel explicite de la méthode close() pour fermer le fichier.

Les différents modes d'ouverture d'un fichier sont les suivants :

    "r" : lecture seule
    "w" : écriture seule (écrase le fichier s'il existe déjà)
    "a" : ajout à la fin du fichier (crée le fichier s'il n'existe pas)
    "x" : création d'un nouveau fichier en écriture seulement (génère une erreur si le fichier existe déjà)
    "b" : mode binaire (pour les fichiers binaires)
    "+" : ouverture en lecture/écriture

Ces modes d'ouverture permettent de spécifier le comportement du fichier en fonction des besoins du programme.
Par exemple, le mode "r" permet la lecture du fichier, tandis que le mode "w" permet l'écriture dans le fichier et écrase le contenu précédent s'il existe déjà. 
Le mode "a" permet d'ajouter du contenu à la fin du fichier sans écraser le contenu précédent,
tandis que le mode "x" permet de créer un nouveau fichier en écriture seulement et génère une erreur si le fichier existe déjà.
Le mode binaire est utilisé pour les fichiers binaires tels que les images ou les fichiers audio, tandis que le mode "+" permet une ouverture en lecture et en écriture simultanément.
"""
## Le module OS et le système de fichiers
"""
Pour lister le contenu d'un dossier en Python, on peut utiliser la fonction os.listdir(). 
Cette fonction prend en paramètre le chemin du dossier que l'on souhaite lister et renvoie une liste contenant le nom de tous les fichiers et dossiers présents dans le dossier spécifié. Voici un exemple :
"""
import os
dossier = "/chemin/vers/mon/dossier"
contenu_dossier = os.listdir(dossier)
print(contenu_dossier)
"""
Notez que la liste renvoyée par la fonction os.listdir() ne contient que les noms des fichiers et des dossiers, et non leur chemin complet. 
Si vous avez besoin du chemin complet de chaque fichier ou dossier, 
vous pouvez utiliser la fonction os.path.join() pour créer le chemin complet à partir du nom de fichier et du chemin du dossier.
Il est impossible d'utiliser un module sans l'importer car l'importation d'un module est ce qui permet à Python de charger le code du module dans la mémoire et de le rendre disponible pour utilisation dans votre programme. 
Lorsque vous importez un module, Python recherche le fichier correspondant sur votre système de fichiers et l'exécute, 
créant ainsi un objet de module qui est stocké en mémoire. Sans cette étape d'importation, 
le code du module n'existerait pas en mémoire et ne pourrait pas être utilisé par votre programme.
"""
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
    