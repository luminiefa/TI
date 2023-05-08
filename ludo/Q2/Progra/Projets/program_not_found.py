"""
This module contains the ProgramNotFound class, which is a custom exception raised when a program
is not found in the list of available logs.
"""
class ProgramNotFound(Exception):
    """
    Exception levée lorsqu'un programme n'est pas trouvé dans la liste des logs.

    Attributes:
        searched_program (str): le programme recherché.
        available_programs (list[str]): ensemble des programmes qui étaient disponibles.
    """

    def __init__(self, searched_program, available_programs):
        """
        Initialise une nouvelle instance de ProgramNotFound.

        Args:
            searched_program (str): le programme recherché.
            available_programs (list[str]): ensemble des programmes qui étaient disponibles.
        """
        super().__init__()
        self.searched_program = searched_program
        self.available_programs = available_programs

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant l'erreur.

        Returns:
            str: la chaîne de caractères représentant l'erreur.

        Exemple :
            Impossible de trouver le programme Prog dans la liste :
            Programme1
            Programme2
            Programme3
        """
        return (
            f"Impossible de trouver le programme {self.searched_program} dans la liste :\n" +
            "\n".join(self.available_programs)
        )
