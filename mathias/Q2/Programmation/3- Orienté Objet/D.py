class Person :
    def __init__(self, name:str) :
        self.name = name
        self.home = None
        self.possessions = []

    def __str__(self) :
        return self.name+" ("+self.address+")"
    
    @property
    def is_owner(self) :
        return True if self.possessions != [] else False

    @property
    def address(self) :
        return self.home.building.address

    def show_possessions_details(self) :
        for possession in self.possessions :
            possession.show_details()


class Building :
    def __init__(self, address:str) :
        self.address = address
        self.properties_list = []

    def __str__(self) :
        return "Building "+self.address+" ("+str(self.nb_properties)+")"

    def add_property(self, property) :
        self.properties_list.append(property)
        property.building = self

    @property
    def nb_properties(self) :
        return len(self.properties_list)


class Property :
    def __init__(self, number:int=None, garage:bool=False) :
        self.number = number #if None => House
        self.garage = garage
        self.building = None
        self.owner = None
        self.occupiers = []

    def __str__(self) :
        return ("House "+self.building.address) if self.number is None else ("Apartment "+str(self.number)+", "+self.building.address)

    def add_owner(self, person) :
        self.owner = person
        person.possessions.append(self)

    def add_occupiers(self, person) :
        self.occupiers.append(person)
        person.home = self

    def show_details(self) :
        print( "--- "+self.__str__()+" ---" )
        print("Owner : "+self.owner.name+" ("+self.owner.address+")")
        print("Occupiers :")
        for occupier in self.occupiers :
            print("- "+occupier.name)
        print("Garage : YES") if self.garage == True else print("Garage : NO")
        return None if self.number is None else print("Nb Apart in Building : "+str(self.building.nb_properties))

    def sale_to(self, new_owner) :
        self.owner.possessions.remove(self)
        self.owner = new_owner
        new_owner.possessions.append(self)

    

b1 = Building("Commonstreet nb 5")
b2 = Building("Magicstreet nb 18")
ap1 = Property(1, False)
ap2 = Property(2, False)
ap3 = Property(3, False)
ap4 = Property(4, False)
h = Property(None, True)
bob = Person("Bob")
alice = Person("Alice")
bobby_jr = Person("Bobby Jr")
chris = Person("Chris")
david = Person("David")
elen = Person("Elen")

b1.add_property(ap1)
b1.add_property(ap2)
b1.add_property(ap3)
b1.add_property(ap4)
b2.add_property(h)
h.add_occupiers(bob)
h.add_occupiers(alice)
h.add_occupiers(bobby_jr)
ap1.add_occupiers(chris)
ap3.add_occupiers(david)
ap4.add_occupiers(elen)
h.add_owner(bob)
ap1.add_owner(bob)
ap2.add_owner(bob)
ap3.add_owner(david)
ap4.add_owner(elen)

ap2.sale_to(elen)


print("Bob : ")
bob.show_possessions_details()
print("Elen : ")
elen.show_possessions_details()
