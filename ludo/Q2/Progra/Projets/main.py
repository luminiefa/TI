import os
from log_manager import LogManager


from log import Log

import os
from log_manager import LogManager
from program_not_found import ProgramNotFound
from log import Log


def load_log_from_file(path):
    try:
        with open(path, 'r') as file:
            logs = [Log(line.strip(), path) for line in file]
            return '\n'.join(str(log) for log in logs)
    except FileNotFoundError:
        return "Le chemin du fichier n'existe pas"



def load_logs_from_folder(folder_path):
    logs = []

    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_logs = load_log_from_file(file_path)
                if file_logs is not None:
                    logs.extend(file_logs)
        return logs
    except FileNotFoundError:
        abs_path = os.path.abspath(folder_path)
        print("Le chemin du dossier n'existe pas")
        print("Chemin absolu:", abs_path)
        return None
    except Exception as e:
        print("Une erreur s'est produite:", e)
        return None


def get_folders_and_subfolders(folder_path):
    folder_list = []
    abs_path = os.path.abspath(folder_path)

    if not os.path.exists(folder_path):
        print("Le chemin du dossier n'existe pas")
        print("Chemin absolu:", abs_path)
        return None

    try:
        for root, dirs, files in os.walk(folder_path):
            for d in dirs:
                relative_path = os.path.join(root, d)
                folder_list.append(os.path.relpath(relative_path, start=os.path.abspath(os.curdir)))
        return [folder_path] + folder_list
    except Exception as e:
        print("Une erreur s'est produite:", e)
        return None


    try:
        for root, dirs, files in os.walk(folder_path):
            for d in dirs:
                relative_path = os.path.join(root, d)
                folder_list.append(os.path.relpath(relative_path, start=folder_path))
        return [folder_path] + folder_list
    except Exception as e:
        print("Une erreur s'est produite:", e)
        return None

def load(path_folder):
    logs = []
    folder_list = get_folders_and_subfolders(path_folder)
    if folder_list is not None:
        for folder in folder_list:
            folder_logs = load_logs_from_folder(folder)
            if folder_logs is not None:
                logs.extend(folder_logs)
    return logs



def menu(available_choices):
    while True:
        for key, value in available_choices.items():
            print(f"{key}: {value}")
        user_choice = input("Entrez le numéro de votre choix: ")
        if user_choice.isdigit() and int(user_choice) in available_choices:
            return int(user_choice)
        else:
            print("Choix invalide. Veuillez réessayer.")

def main():
    log_manager = LogManager()
    #log_manager.add_logs([Log("log1", "/config/data/TI/ludo/Q2/Progra/Projets/dossier/sous_dossier1/syslog.log")])

    while True:
        choice = menu({
            1: "Affiche les logs d'un programme",
            2: "Charger un autre dossier contenant des fichiers de logs (attention, les anciens logs sont supprimés)",
            3: "Test",
            9: "Termine le programme"
        })

        if choice == 1:
            program_name = input("Entrez le nom du programme: ")
            try:
                searched_logs = log_manager.search_logs(program_name)
                for log in searched_logs:
                    print(log)
            except ProgramNotFound as e:
                print(str(e))
        elif choice == 2:
            log_manager.clear()
            folder_path = input("Entrez le chemin relatif du dossier: ")
            logs = load(folder_path)
            if logs is not None:
                log_manager.add_logs([Log(log, folder_path) for log in logs])
        elif choice == 3:
            test = load_log_from_file("ludo/Q2/Progra/Projets/dossier/sous_dossier1/syslog.log")
            #print(test)
            test2 = load_logs_from_folder("ludo/Q2/Progra/Projets/dossier/sous_dossier1")
            #print(test2)
            test3 = get_folders_and_subfolders("ludo/Q2/Progra/Projets/dossier")
            #print(test3)
            test4 = load("ludo/Q2/Progra/Projets/dossier/sous_dossier1")
            #print(test4)
            log1 = Log("Oct 25 02:34:27 kali systemd[1]: logrotate.service: Succeeded.", "ludo/Q2/Progra/Projets/dossier/sous_dossier1/syslog.log")
            log2 = Log("Oct 26 02:34:27 kali kali[1]: logrotate.service: Succeeded.", "ludo/Q2/Progra/Projets/dossier/sous_dossier1/syslog.log")

            test5 = log1.get_program()
            #print(test5)
            test6 = log1.__str__()
            #print(test6)
            logs = [log1, log2]
            logs_trie = log_manager.sort_by_program(logs)
            #print(logs_trie)

            log_manager.add_logs(logs)
            # problème avec add_logs
            # normalement le chemin relatif de dossier est "ludo/Q2/Progra/Projets/dossier" 
            # alors que mon programme renvoie Le chemin n'existe pas
            # Chemin absolu: /config/data/TI/sous_dossier1
            # alors que le chemin absolu est /config/data/TI/ludo/Q2/Progra/Projets/dossier
            # Après /TI est le problème

            chercher_logs = log_manager.search_logs("kali")
            #print(chercher_logs)

            nbrLogs = log_manager.nbr_logs
            #print(nbrLogs)

            #print(log_manager.__str__())
            
        elif choice == 9:
            print("Au revoir !")
            break


if __name__ == "__main__":
    main()
