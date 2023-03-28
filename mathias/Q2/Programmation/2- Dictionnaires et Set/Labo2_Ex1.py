def update_contact(contacts, name, mail):
    contacts.update(dict([(name, mail)]))



contacts = {"nom1":"adresse1"}
name = "nom2"
mail = "adresse2"

print(contacts)
update_contact(contacts, name, mail)
print("----------------------------")

print(contacts)
