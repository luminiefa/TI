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
            # Diviser la ligne de log en mots
            words = self.text.split()

            # Chercher le premier mot qui se termine par un crochet ouvrant '['
            for word in words:
                if word.endswith('['):
                    # Enlever le crochet ouvrant de la fin du mot
                    program = word.rstrip('[')

                    # Vérifier si le nom du programme est constitué
                    # uniquement de caractères alphanumériques et de soulignements
                    if program.isalnum() or '_' in program:
                        return program

            # Si aucun nom de programme n'a pu être extrait, retourner "Unknown"
            return "Unknown"
        except ValueError:
            return "Unknown"


    def __str__(self):
        """
        Méthode qui permet de renvoyer le contenu du log
        :return: str - Le contenu du log
        """
        return self.text
