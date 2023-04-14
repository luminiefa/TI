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

