# Creates ProtectedClass with a private and protected variable
class ProtectedClass:
    def __init__ (self):
        self.__privateNum = 24
        self._protectedNum = 42

# Function within ProtectedClass to print the private variable
    def getPrivateNum (self):
        print (self.__privateNum)

# Function within ProtectedClass to print the protected variable
    def getProtectedNum (self):
        print (self._protectedNum)

# Creates a ProtectedClass object
# Calls the getPrivateNum and the getProtectedNum functions
if __name__ == "__main__":
    obj = ProtectedClass ()
    obj.getPrivateNum()
    obj.getProtectedNum()