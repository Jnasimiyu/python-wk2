# Base class
class Entity:
    def move(self):
        print("This entity moves in some way.")

# Vehicle subclasses
class Car(Entity):
    def move(self):
        print("Driving ")

class Plane(Entity):
    def move(self):
        print("Flying ")

class Boat(Entity):
    def move(self):
        print("Sailing ")

# Animal subclasses
class Dog(Entity):
    def move(self):
        print("Running ")

class Bird(Entity):
    def move(self):
        print("Flying ")

class Fish(Entity):
    def move(self):
        print("Swimming ")

# Demonstrating polymorphism
entities = [Car(), Plane(), Boat(), Dog(), Bird(), Fish()]

for entity in entities:
    entity.move()
