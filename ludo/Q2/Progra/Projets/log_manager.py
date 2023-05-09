"""
This module contains the LogManager class, which is responsible for managing and organizing logs.
"""
from program_not_found import ProgramNotFound

class LogManager:
    """
    Classe qui gère les logs.
    """

    @staticmethod
    def sort_by_program(logs):
        """
        Trie les logs par programme.
        """
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
        """
        Efface les logs.
        """
        self.logs = {}

    def add_logs(self, logs):
        """
        Ajoute des logs à la liste de logs existante.

        Args:
            logs (list[Log]): Une liste d'instances de la classe Log.

        Returns:
            None
        """
        new_logs = self.sort_by_program(logs)
        for program, log_list in new_logs.items():
            if program not in self.logs:
                self.logs[program] = []
            self.logs[program].extend(log_list)

    def search_logs(self, program_name):
        """
        Recherche des logs pour un programme spécifique.
        """
        if program_name in self.logs:
            return self.logs[program_name]
        else:
            raise ProgramNotFound(program_name, list(self.logs.keys()))

    @property
    def nbr_logs(self):
        """
        Nombre total de logs.
        """
        return sum([len(logs) for logs in self.logs.values()])

    def __str__(self):
        """
        Représentation sous forme de chaîne de caractères de tous les logs.
        """
        output = []
        for program, logs in self.logs.items():
            output.append(program + ":")
            output.append("=" * len(program))
            for log in logs:
                # Supprimez les espaces et les sauts de ligne avant et après
                log_str = str(log).strip()
                if log_str:  # Vérifiez si la chaîne n'est pas vide
                    output.append(log_str) 
        output.append("TOTAL LOGS: " + str(self.nbr_logs))
        return "\n".join(output)
