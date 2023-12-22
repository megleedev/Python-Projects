# Creates a class called Animal
# Animal is created with two variable names for attributes with default values
# Animal is also the Parent class for other classes
class Animal:
    species = " "
    predator = True

    def description (self):
        message = "\nAnimals are multicellular, eukaryotic organisms in the biological kingdom Animalia."
        return message

# Creates a Bird child class that inherits from the Animal parent class
# Bird is created with two variable names for attributes with default values
# and a polymorphed method
class Bird (Animal):
    color = " "
    size = " "
    
    def description (self):
        message = "\nBirds are a group of warm-blooded vertebrates constituting the class Aves."
        return message

# Creates a LargeBird child class that inherits from both the Animal
# parent class and the Bird child class
# LargeBird is created with two variable names for attributes with default
# values and a polymorphed method
class LargeBird (Bird, Animal):
    weight = 0.00
    height = 0

    def description (self):
        message = "\nThe largest extant species of bird measured by mass is the common ostrich (Struthio camelus)."
        return message
    
# Objects from each class are instantiated and their polymorphed methods
# are printed to the console
if __name__ == "__main__":

    animal = Animal()
    print (animal.description())

    blueBird = Bird()
    print (blueBird.description())

    ostrich = LargeBird()
    print (ostrich.description())