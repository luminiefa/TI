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
        words = self.text.split(" ")
        program = "Unknown"
        for word in words:
            if "]" in word:
                program = word.split("[")[0]
                break
        return program



    def __str__(self):
        """
        :return: String - renvoie le contenu du log
        """
        return self.text
