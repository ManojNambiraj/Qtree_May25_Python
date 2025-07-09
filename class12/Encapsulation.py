# Access specifiers

    # Public
    # Private
        # getter
        # setter

# Encapsulation

class Car:
    def __init__(self, wheels, color, fuel):
        self.__noOfWheels = wheels
        self.carColor = color
        self.fuelType = fuel

    def setNoOfWheels(self, demoWheels):
        self.__noOfWheels = demoWheels

    def getNoOfWheels(self):
        return self.__noOfWheels


i10 = Car(0, "Meroon", "Petrol")

i10.setNoOfWheels(6)

print(i10.getNoOfWheels())

print(i10.carColor)