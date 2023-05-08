"""
This module contains the Log class, which represents an individual log entry and provides
functionality for extracting the program name from the log text.
"""
class Log:
    """
    Classe qui représente un log
    """

    def __init__(self, text, source):
        """
        Constructeur de la classe Log
        :param text: str - Contenu de la ligne de log
        :param source: str - Chemin vers le fichier qui contenait cette ligne de log
        """
        self.text = text
        self.source = source

    def get_program(self):
        """
        Méthode qui permet de récupérer le nom du programme à partir d'une ligne de log
        :return: str - Le nom du programme ou "Unknown" si le nom n'a pas pu être extrait
        """
        try:
            # Trouver la position du premier crochet ouvrant '['
            open_bracket_pos = self.text.index('[')

            # Trouver la position du dernier espace avant le premier crochet ouvrant
            space_pos = self.text.rfind(' ', 0, open_bracket_pos)

            # Extraire le nom du programme en utilisant les positions trouvées
            program = self.text[space_pos + 1:open_bracket_pos].strip()

            # Vérifier si le nom du programme est constitué
            # uniquement de caractères alphanumériques et de soulignements
            if program.isalnum() or '_' in program:
                return program
            else:
                return "Unknown"
        except ValueError:
            return "Unknown"

    def __str__(self):
        """
        Méthode qui permet de renvoyer le contenu du log
        :return: str - Le contenu du log
        """
        return self.text
