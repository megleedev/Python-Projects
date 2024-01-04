from abc import ABC, abstractmethod

# Class Movie contains one abstract method and one regular method
class movie (ABC):
    def movieTime1 (self, time):
        print ("The time of the movie is: ", time)

    @abstractmethod
    def arrivalTime (self, time):
        pass

# Class Arrival is a child class of Movie that defines the implementation
# of its parent abstract method
class arrival (movie):
    def arrivalTime (self, time):
        print ("Your arrival time of {} exceeded the start time of Movie 1. See Movie 2.".format (time))

# Create an object that utilizes both the parent and child methods
if __name__ == "__main__":
    obj = arrival ()
    obj.movieTime1 ("18")
    obj.arrivalTime ("19")