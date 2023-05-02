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
        pattern = r'\w+(?=\[\d+\])'
        print(f"self.text: {self.text}, type: {type(self.text)}")  # Ajoutez cette ligne
        match = re.search(pattern, self.text)  # Utilisez self.text au lieu de self
        return match.group(0) if match else None




    def __str__(self):
        """
        :return: String - renvoie le contenu du log
        """
        return self.text
