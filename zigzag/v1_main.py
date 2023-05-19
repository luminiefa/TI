import os

def load_log_from_file(relative_path):
    try:
        with open(relative_path, "r") as file:
            logs = file.readlines()
        return logs
    except FileNotFoundError:
        print("Le chemin n'existe pas")
        print("Chemin absolu:", os.path.abspath(relative_path))
        return None

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
        print("Le chemin n'existe pas")
        print("Chemin absolu:", os.path.abspath(folder_path))
        return None

def get_folders_and_subfolders(folder_path):
    folder_list = []
    try:
        for root, dirs, files in os.walk(folder_path):
            folder_list.append(root)
            folder_list.extend([os.path.join(root, d) for d in dirs])
        return folder_list
    except Exception as e:
        print("Le chemin n'existe pas")
        print("Chemin absolu:", os.path.abspath(folder_path))
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

class Log:
    def __init__(self, text, source):
        self.text = text
        self.source = source

    def get_program(self):
        if "Program" in self.text:
            return self.text.split(" ")[0]
        else:
            return "Unknown"

    def __str__(self):
        return self.text

class ProgramNotFound(Exception):
    def __init__(self, searched_program, available_programs):
        self.searched_program = searched_program
        self.available_programs = available_programs

    def __str__(self):
        return f"Impossible de trouver le programme {self.searched_program} dans la liste :\n" + "\n".join(self.available_programs)

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
        output.append(program + ":")
        for log in logs:
            output.append("    " + str(log))
    output.append("TOTAL LOGS: " + str(self.nbr_logs))
    return "\n".join(output)

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
    while True:
        choice = menu({
            1: "Charger des logs depuis un fichier",
            2: "Charger des logs depuis un dossier",
            3: "Rechercher des logs par nom de programme",
            4: "Afficher tous les logs",
            5: "Quitter"
        })

        if choice == 1:
            file_path = input("Entrez le chemin relatif du fichier: ")
            logs = load_log_from_file(file_path)
            if logs is not None:
                log_manager.add_logs([Log(log, file_path) for log in logs])
        elif choice == 2:
            folder_path = input("Entrez le chemin relatif du dossier: ")
            logs = load(folder_path)
            if logs is not None:
                log_manager.add_logs([Log(log, folder_path) for log in logs])
        elif choice == 3:
            program_name = input("Entrez le nom du programme: ")
            try:
                searched_logs = log_manager.search_logs(program_name)
                for log in searched_logs:
                    print(log)
            except ProgramNotFound as e:
                print(str(e))
        elif choice == 4:
            print(log_manager)
        elif choice == 5:
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()
