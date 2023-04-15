def update_contact(contacts, name, mail):
    contacts.update(dict([(name, mail)]))

def print_all(contacts):
    for tup in contacts.items():
        print("Nom: ", tup[0], " - Mail: ", tup[1])


contacts = {}
update_contact(contacts,"Smal","anne.smal@henallux.be")
update_contact(contacts,"Valentin","didier.valentin@henallux.be")
update_contact(contacts,"Duvillé","guillerme.duville@henallux.be")
update_contact(contacts,"Schovaers","corentin.schovaers@henallux.be")
print_all(contacts)
