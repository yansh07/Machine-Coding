# Beginners hamesha Inheritance (class Child(Parent)) ke peeche bhagte hain, 
# jabki LLD aur Machine Coding mein Composition (Has-a relationship) hamesha jeetta hai.

# Golden Rule: Favor Composition over Inheritance.

# Inheritance (Is-A): Dog is a Animal.
# Composition (Has-A): Car has an Engine.

#bad practice
class Vehicle:
    def drive(self): pass

class ElectricCar(Vehicle):
    def charge(self): pass

#good practice - composition
from abc import ABC, abstractmethod
class Engine(ABC):
    @abstractmethod
    def start(self): pass

class ElectricEngine(Engine):
    def start(self):
        print("Silent battery start")

class Car:
    def __init__(self, engine: Engine): # Injection
        self.engine = engine # CAR has an engine

        def start_car(self):
            self.engine.start() #Fayda: Kal ko Car ko GasEngine se replace karna ho, toh Car class todni nahi padegi.