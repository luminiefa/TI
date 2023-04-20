class ProgramNotFound(Exception):
    def __init__(self, searched_program, available_programs):
        self.searched_program = searched_program
        self.available_programs = available_programs

    def __str__(self):
        return f"Impossible de trouver le programme {self.searched_program} dans la liste :\n" + "\n".join(self.available_programs)
