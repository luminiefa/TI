from program_not_found import ProgramNotFound

def main():
    searched_program = "Programme"
    available_programs = ["Programme1", "Programme2", "Programme3"]

    if searched_program not in available_programs:
        try:
            raise ProgramNotFound(searched_program, available_programs)
        except ProgramNotFound as e:
            print("L'exception ProgramNotFound a été interceptée:")
            print(e)
    else:
        print(f"Le programme {searched_program} a été trouvé dans la liste.")

if __name__ == "__main__":
    main()
