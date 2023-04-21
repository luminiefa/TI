import os
from log_manager import load_log_from_file, load_logs_from_folder, get_folders_and_subfolders, load, menu
from log_manager import LogManager


from log import Log

import os
from log_manager import LogManager
from program_not_found import ProgramNotFound
from log import Log


def menu(available_choices):
    while True:
        for choice, description in available_choices.items():
            print(f"{choice}: {description}")
        user_input = input("Entrez le numéro de votre choix: ")
        if user_input.isnumeric() and int(user_input) in available_choices.keys():
            return int(user_input)
        else:
            print("Entrée non valide. Veuillez entrer un numéro de choix valide.\n")


def main():
    log_manager = LogManager()
    log_manager.add_logs([Log("log1", "/config/data/TI/ludo/Q2/Progra/Projets/dossier/sous_dossier1/syslog.log")])

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
            log = Log("Oct 25 02:34:27 kali systemd[1]: logrotate.service: Succeeded.", "ludo/Q2/Progra/Projets/dossier/sous_dossier1/syslog.log")
            test5 = log.get_program()
            #print(test5)
            test6 = log.__str__()
            print(test6)
        elif choice == 9:
            print("Au revoir !")
            break


if __name__ == "__main__":
    main()
