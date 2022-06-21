#Abstract Class

from abc import ABC, abstractmethod

#defining abstract class to ensure enginetype method is created in all child class built from Vehicle abstract class
class Vehicle(ABC):
    @abstractmethod
    def enginetype(self):
        pass
class Car(Vehicle):
    def enginetype(self):
        print("petrol")
class Bike(Vehicle):
    def enginetype(self):
        print("petrol")

baleno = Car()
baleno.enginetype()
apache = Bike()
apache.enginetype()
