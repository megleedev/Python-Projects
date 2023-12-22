# Creates a class called 'Animal'
# Animal is created with two variable names for attributes with default values
# Animal is also the Parent class for other classes
class Animal:
    species = " "
    predator = True

# Creates a Bird class that inherits from the Animal parent class
# Bird is created with two variable names for attributes with default values
class Bird (Animal):
    color = " "
    size = " "

# Creates an Eagle class that inherits from both the Animal parent class -
# and the Bird class
# Eagle is created with two variable names for attributes with default values
class LargeBird (Bird, Animal):
    weight = 0.00
    height = 0

# I got concerned that the above didn't work so I made sure
if __name__ == "__main__":

    LargeCat = Animal ()
    LargeCat.species = "Tiger"
    LargeCat.predator = True

    print (LargeCat.species)
    print (LargeCat.predator)


    SmallBird = Bird ()
    SmallBird.species = "Pidgeon"
    SmallBird.predator = False
    SmallBird.color = "White"
    SmallBird.size = "Small"

    print (SmallBird.species)
    print (SmallBird.predator)
    print (SmallBird.color)
    print (SmallBird.size)

    Eagle = LargeBird ()
    Eagle.species = "Eagle"
    Eagle.predator = True
    Eagle.color = "Brown/White"
    Eagle.size = "Large"
    Eagle.weight = 13.5
    Eagle.height = 30

    print (Eagle.species)
    print (Eagle.predator)
    print (Eagle.color)
    print (Eagle.size)
    print (Eagle.weight)
    print (Eagle.height)