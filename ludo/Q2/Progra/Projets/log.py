import re
class Log:
    def __init__(self, text, source):
        """
        Constructeur de la classe Log
        :param text: String - Contenu de la ligne de log
        :param source: String - Chemin vers le fichier qui contenait
        cette ligne de log
        """
        self.text = text
        self.source = source

    

    def get_program(self):
        pattern = r"\w+(?=\[\d+\])"
        match = re.search(pattern, self.text)
        if match:
            program = match.group().split('[')[0]  # Prendre seulement la partie avant les crochets
        else:
            program = "Unknown"
        return program




    def __str__(self):
        """
        :return: String - renvoie le contenu du log
        """
        return self.text