def print_all(contacts):
    for tup in contacts.items():
        print("Nom: ", tup[0], " - Mail: ", tup[1])


contacts = {'nom1': 'adresse1', 'nom2': 'adresse2'}

print_all(contacts)