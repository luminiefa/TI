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
            # Diviser la ligne de log en utilisant l'espace comme séparateur
            split_result = self.text.split()
            # ['Oct', '25', '02:34:27', 'kali', 'systemd[1]:', 'logrotate.service:', 'Succeeded.']
            # Parcourir les éléments de la liste pour trouver le premier élément contenant '['
            for element in split_result:
                if '[' in element:
                    # Extraire le nom du prog en supp les caract non alphanumériques et les chiffres
                    program = ''.join(characters for characters in element if characters.isalpha())
                    return program

            # Si aucun nom de programme n'a été trouvé, retourner "Unknown"
            return "Unknown"

        except ValueError:
            return "Unknown"

    def __str__(self):
        """
        Méthode qui permet de renvoyer le contenu du log
        :return: str - Le contenu du log
        """
        return self.text
