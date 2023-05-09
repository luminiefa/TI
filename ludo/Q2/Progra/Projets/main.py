"""
Module principal contenant la fonction main() qui gère les interactions avec l'utilisateur.
"""
import os
from log_manager import LogManager
from program_not_found import ProgramNotFound
from log import Log


def load_log_from_file(path):
    """
    Charge les logs contenus dans le fichier situé au chemin `path` et retourne une liste de lignes.

    Args:
        path (str): Le chemin relatif du fichier.

    Returns:
        list: Une liste de chaînes de caractères, chaque chaîne correspondant à une ligne de logs.

    Raises:
        FileNotFoundError: Si le chemin du fichier n'existe pas.
        Exception: Si une error autre que FileNotFoundError se produit.

    """
    try:
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("Le chemin du fichier n'existe pas")
        return None
    except Exception as error:
        print(f"Une erreur s'est produite: {error}")
        return None

def load_logs_from_folder(folder_path):
    """
    Charge les logs contenus dans tous les fichiers situés dans le dossier
    spécifié par `folder_path`
    et ses sous-dossiers, et retourne une liste de lignes.

    Args:
        folder_path (str): Le chemin relatif du dossier.

    Returns:
        list: Une liste de chaînes de caractères, chaque chaîne correspondant à une ligne de logs.

    Raises:
        FileNotFoundError: Si le chemin du dossier n'existe pas.
        Exception: Si une error autre que FileNotFoundError se produit.

    """
    try:
        logs = []

        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_file():
                    file_logs = load_log_from_file(entry.path)
                    if file_logs is not None:
                        logs.extend(file_logs)
        return logs
    except FileNotFoundError:
        abs_path = os.path.abspath(folder_path)
        print("Le chemin du dossier n'existe pas")
        print("Chemin absolu:", abs_path)
        return None
    except Exception as error:
        print(f"Une erreur s'est produite: {error}")
        return None

def get_folders_and_subfolders(folder_path):
    """
    Retourne une liste de tous les dossiers situés dans `folder_path` et ses sous-dossiers.

    Args:
        folder_path (str): Le chemin absolu ou relatif du dossier.

    Returns:
        list: Une liste de chaînes de caractères, chaque chaîne correspondant
        au chemin relatif d'un dossier.

    Raises:
        None.

    """

    folder_list = []
    abs_path = os.path.abspath(folder_path)

    if not os.path.exists(folder_path):
        print("Le chemin du dossier n'existe pas")
        print("Chemin absolu:", abs_path)
        return None

    try:
        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    relative_path = os.path.relpath(entry.path, start=os.path.abspath(os.curdir))
                    folder_list.append(relative_path)
        return [folder_path] + folder_list
    except Exception as error:
        print("Une error s'est produite:", error)
        return None

def load(path_folder):
    """
    Charge les logs de tous les fichiers situés dans le dossier spécifié par `path_folder`
    et ses sous-dossiers, et les retourne sous forme de liste d'objets Log.

    Args:
        path_folder (str): Le chemin absolu ou relatif du dossier.

    Returns:
        list: Une liste d'objets Log, chaque objet représentant une ligne de log.

    Raises:
        None.

    """
    logs = []
    folder_list = get_folders_and_subfolders(path_folder)
    if folder_list is not None:
        for folder in folder_list:
            folder_logs = load_logs_from_folder(folder)
            if folder_logs is not None:
                logs.extend(folder_logs)
    return logs

def menu(available_choices):
    """
    Affiche le menu des choix disponibles pour l'utilisateur, lui permet de faire un choix,
    et retourne le numéro de choix sélectionné.

    Args:
        available_choices (dict): Un dictionnaire contenant
        les choix disponibles pour l'utilisateur.

    Returns:
        int: Le numéro du choix sélectionné.

    Raises:
        None.

    """
    while True:
        for key, value in available_choices.items():
            print(f"{key}: {value}")
        user_choice = input("Entrez le numéro de votre choix: ")
        if user_choice.isdigit() and int(user_choice) in available_choices:
            return int(user_choice)
        else:
            print("Choix invalide. Veuillez réessayer.")

def main():
    """
    Fonction principale qui gère les interactions avec l'utilisateur.
    Permet de rechercher les logs d'un programme,
    de charger un dossier contenant des fichiers de logs,
    et de quitter le programme.

    Args:
        None.

    Returns:
        None.

    Raises:
        None.

    """
    log_manager = LogManager()

    while True:
        choice = menu({
            1: "Affiche les logs d'un programme",
            2: (
                "Charger un autre dossier contenant des fichiers de logs "
                "(! les anciens logs sont supprimés)"
                ),
            3: "Test",
            9: "Termine le programme"
        })

        if choice == 1:
            program_name = input("Entrez le nom du programme: ")
            try:
                searched_logs = log_manager.search_logs(program_name)
                for log in searched_logs:
                    print(log)
            except ProgramNotFound as error:
                print(str(error))
        elif choice == 2:
            log_manager.clear()
            folder_path = input("Entrez le chemin relatif du dossier: ")
            logs = load(folder_path)
            if logs is not None:
                log_manager.add_logs([Log(log, folder_path) for log in logs])
        elif choice == 3:
            print("test")
        elif choice == 9:
            print("Au revoir !")
            break


if __name__ == "__main__":
    main()
