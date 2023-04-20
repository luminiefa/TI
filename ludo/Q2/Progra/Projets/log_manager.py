import os
from log import Log
from program_not_found import ProgramNotFound
from datetime import datetime

class LogManager:
    @staticmethod
    def sort_by_program(logs):
        sorted_logs = {}
        for log in logs:
            program = log.get_program()
            if program not in sorted_logs:
                sorted_logs[program] = []
            sorted_logs[program].append(log)
        return sorted_logs

    def __init__(self, logs=None):
        if logs is None:
            logs = []
        self.logs = self.sort_by_program(logs)

    def clear(self):
        self.logs = {}

    def add_logs(self, logs):
        new_logs = self.sort_by_program(logs)
        for program, log_list in new_logs.items():
            if program not in self.logs:
                self.logs[program] = []
            self.logs[program].extend(log_list)

    def search_logs(self, program_name):
        if program_name in self.logs:
            return self.logs[program_name]
        else:
            raise ProgramNotFound(program_name, list(self.logs.keys()))

    @property
    def nbr_logs(self):
        return sum([len(logs) for logs in self.logs.values()])

    def __str__(self):
        output = []
        for program, logs in self.logs.items():
            sorted_logs = sorted(logs, key=lambda log: log.datetime)
            output.append(program + ":")
            for log in sorted_logs:
                output.append(f"    {log.datetime} - {log.source} - {log.text}")
        output.append(f"TOTAL LOGS: {self.nbr_logs}")
        return "\n".join(output)
    
def load_log_from_file(relative_path):
    logs = []
    abs_path = os.path.abspath(relative_path)
    try:
        source = os.path.dirname(abs_path)
        with open(relative_path, "r") as file:
            for line in file:
                logs.append(Log(line.strip(), source))
    except FileNotFoundError:
        print("Le chemin n'existe pas")
        print("Chemin absolu:", abs_path)
        return None
    except Exception as e:
        print("Une erreur s'est produite:", e)
        return None
    return logs




def load_logs_from_folder(folder_path):
    logs = []
    abs_path = os.path.abspath(folder_path)
    
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_logs = load_log_from_file(file_path)
                if file_logs is not None:
                    logs.extend(file_logs)
        return logs
    except FileNotFoundError:
        print("Le chemin n'existe pas")
        print("Chemin absolu:", abs_path)
        return None
    except Exception as e:
        print("Une erreur s'est produite:", e)
        return None

def get_folders_and_subfolders(folder_path):
    folder_list = []
    abs_path = os.path.abspath(folder_path)
    
    if not os.path.exists(folder_path):
        print("Le chemin n'existe pas")
        print("Chemin absolu:", abs_path)
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