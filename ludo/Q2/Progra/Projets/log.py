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
