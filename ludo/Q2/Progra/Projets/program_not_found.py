class ProgramNotFound(Exception):
    def __init__(self, searched_program, available_programs):
        """
        :param searched_program: String - le programme recherché
        :param available_programs: Liste de String - ensemble des
        programmes qui étaient disponibles
        """
        super().__init__()
        self.searched_program = searched_program
        self.available_programs = available_programs

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant l'erreur
        Exemple :
        Impossible de trouver le programme Prog dans la liste :
        Programme1
        Programme2
        Programme3
        :return: String
        """
        return f"Impossible de trouver le programme {self.searched_program} dans la liste :\n" + "\n".join(self.available_programs)