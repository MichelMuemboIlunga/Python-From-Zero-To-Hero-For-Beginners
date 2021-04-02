class ClassName:
    """ code to execute """
    pass


# Instance of Sample
x = ClassName()

print(type(x))
print("-------------- Done -------------------")

""" dog class """


class Dog:
    # This method is used to initialize the attributes of an object
    def __init__(self, name, bark):
        self.name = name
        self.bark = bark


# instantiate

black = Dog("black", 'woof')
print(black)
print(type(black))
print(black.name)

""" More about dog class """


class Dog:
    # This method is used to initialize the attributes of an object
    def __init__(self, name, bark, color):
        self.name = name
        self.bark = bark
        self.color = color

    def eat(self):
        print(self.name + " is eating")

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return self.name + " is " + self.bark + " because " + self.color + " dogs like to bark"


my_dog = Dog("black", 'barking', "white")
print(my_dog)
Dog.eat(my_dog)

""" inheritance"""


class Vehicle:
    def __init__(self, make, model, year, needs_maintenance=False, trips_since_maintenance=0):
        self.make = make
        self.model = model
        self.year = year
        self.needs_maintenance = needs_maintenance
        self.trips_since_maintenance = trips_since_maintenance

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year


# creating a cars sub class that inherit from a vehicle parent(super) class
class Cars(Vehicle):
    def __init__(self, make, model, year, needs_maintenance, trips_since_maintenance, is_driving):
        super().__init__(make, model, year, needs_maintenance, trips_since_maintenance)
        self.is_driving = is_driving

    def drive(self, is_driving=True):
        self.is_driving = is_driving
        print(f"Is {self.model} car driving {self.is_driving}")

    def stop(self, is_driving=False):
        self.is_driving = is_driving
        if not self.is_driving:
            self.trips_since_maintenance += 1
            print(f"your car is made at {self.make} at {self.year} the model is {self.model} "
                  f"and the distance drove is {self.trips_since_maintenance}")
            if self.trips_since_maintenance > 100:
                self.needs_maintenance = True
                print(f"You need maintenance {self.needs_maintenance} ")
            else:
                print(f"your cars is in a good maintenance {self.trips_since_maintenance}")
        else:
            print("You are driving")

    def repair(self):
        self.trips_since_maintenance = 0
        self.needs_maintenance = False
        print(f"Your trip is {self.trips_since_maintenance} and your maintenance state is {self.needs_maintenance} ")


# creating a plane sub class
class Plane(Vehicle):
    def __init__(self, make, model, year, needs_maintenance, trips_since_maintenance, flying, landing):
        super().__init__(make, model, year, needs_maintenance, trips_since_maintenance)
        self.flying = flying
        self.landing = landing

    def fly(self, flying=True):
        self.flying = flying
        self.flying = flying
        print(f"Is {self.model} plane flying {self.flying}")

    def land(self, landing=False):
        self.landing = landing
        if not self.landing:
            self.trips_since_maintenance += 1
            print(f"your plane is made at {self.make} at {self.year} the model is {self.model} "
                  f"and the distance drive is {self.trips_since_maintenance}")

            while self.trips_since_maintenance > 100:
                self.needs_maintenance = True
                print(f"You need maintenance {self.needs_maintenance} you can not fly land now ")
                break

            else:
                print(f"your Plane is in a good maintenance {self.trips_since_maintenance}")
        else:
            print("You are flying")


# creating cars

myCar1 = Cars("New york", "Benz", 1995, False, 10, True)
myCar1.drive()
print("----------------------------------------------------")

myCar2 = Cars("Canada", "Audi", 2000, True, 99, False)
myCar2.stop()
print("----------------------------------------------------")

myCar3 = Cars("Germany", "Porches", 1993, False, 101, True)
myCar3.stop()
myCar3.repair()
print("----------------------------------------------------")

myPlane = Plane("Europe", "B52", 2001, True, 101, False, True)
myPlane.fly()
myPlane.land()
print("----------------------------------------------------")

myPlane2 = Plane("Europe", "B52", 2001, True, 10, True, True)
myPlane2.land()
