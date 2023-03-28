class Animal :
    def __init__(self, name, bd, ship_nb, size):
        self.name = name
        self.birthday = bd
        self.ship_nb = ship_nb
        self.size = size

    def sleep(self):
        print(self.name, ": ZzzzzzZzzzzz...")

    def eat(self):
        print(self.name, ": *Crounch*")


class Rabbit (Animal):
    def __init__(self, name, bd, ship_nb, size, ear_size):
        super().__init__(name, bd, ship_nb, size)
        self.ear_size = ear_size

    def jump(self):
        print(self.name, ": *Bwing*") 


class Dog (Animal) :
    def __init__(self, name, bd, ship_nb, size):
        super().__init__(name, bd, ship_nb, size)
    def bark(self):
        print(self.name, ": WOOOUF !")


class Cat (Animal) :
    def __init__(slef, name, bd, ship_nb, size):
        super().__init__(name, bd, ship_nb, size)

    def meow(self) :
        print(self.name, ": Meeoooow")

    def purr(self) :
        print(self.name, ": *Purr*")

    def eat(self):
        self.purr()
        print(self.name, ": *Crounch*")



if __name__ == "__main__" :
    c = Cat("Tesla", "1/04/2017", 12568743, 35)
    d = Dog("Pixel", "16/10/2019", 58963217, 70)
    r = Rabbit("Pong", "11/02/2010", 25874136, 20,15)

    print(c.__dict__)
    print(d.__dict__)
    print(r.__dict__)

    c.sleep()
    d.sleep()
    r.sleep()

    c.eat()
    d.eat()
    r.eat()

    d.bark()
    c.meow()
    r.jump()
