# Creates ProtectedClass with a private and protected variable
class ProtectedClass:
    def __init__ (self):
        self.__privateNum = 24
        self._protectedNum = 42

# Function within ProtectedClass to print the private variable
    def getPrivateNum (self):
        print (self.__privateNum)

    def setPrivateNum (self, private):
        self.__privateNum = private

# Creates a ProtectedClass object
# Calls getPrivateNum, sets PrivateNum to a new value, and then
# calls getPrivateNum again
# Prints protectedNum from the object
if __name__ == "__main__":
    obj = ProtectedClass ()
    obj.getPrivateNum ()
    obj.setPrivateNum (33)
    obj.getPrivateNum ()
    print (obj._protectedNum)