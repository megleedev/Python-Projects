# Creates a class called 'Animal'
# Animal is created with two arguments for creating an Animal object
# Animal is also the Parent class for other classes
class Animal:
    def __init__(self, species, predator):
        self.species = species
        self.predator = True
        

# Creates a Bird class that inherits from the Animal parent class
# Bird is created with two arguments for creating a Bird object
class Bird (Animal):
    def __init__(self, color, size):
        self.color = color
        self.size = size

# Creates an Eagle class that inherits from both the Animal parent class -
# and the Bird class
# Eagle is created with two arguments for creating a Eagle object
class Eagle (Bird, Animal):
    def __init__(self, weight, height):
        self.weight = 0.00
        self.height = 0