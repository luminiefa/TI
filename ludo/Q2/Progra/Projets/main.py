import os
from log import Log
from log_manager import LogManager
from program_not_found import ProgramNotFound

# Les fonctions load_log_from_file, load_logs_from_folder, get_folders_and_subfolders et load restent inchangées.

# La fonction menu reste inchangée.

def main():
    log_manager = LogManager()
    while True:
        choice = menu({
            1: "Charger des logs depuis un fichier",
            2: "Charger des logs depuis un dossier",
            3: "Rechercher des logs par nom de programme",
            4: "Afficher tous les logs",
            5: "Quitter"
        })

        # Le contenu de la boucle if-elif reste inchangé.
