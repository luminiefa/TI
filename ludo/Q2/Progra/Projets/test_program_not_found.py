import os

from program_not_found import ProgramNotFound

SEARCHED_PROGRAM = "Programme X"
AVAILABLE_PROGRAMS = ["Programme A", "Programme B", "Programme C"]
exception = ProgramNotFound(SEARCHED_PROGRAM, AVAILABLE_PROGRAMS)


def test_init():
    assert isinstance(exception, Exception), "La classe ProgramNotFoundError devrait héritée de la classe Exception"
    assert exception.searched_program == SEARCHED_PROGRAM
    assert exception.available_programs == AVAILABLE_PROGRAMS


def test_str():
    message = f"Impossible de trouver le programme {exception.searched_program} dans la liste :"
    for program in exception.available_programs:
        message += f"{os.linesep}{program}"
    assert exception.__str__() == message
