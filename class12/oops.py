# OOPS --> Object Oriented Programmings

    # Class
    # Object
    # Inheritance
    # Encapsulation
    # Polymorphism


    # class Car:
    #     no_of_wheels = 0
    #     color = ""
    #     no_of_sheet = 0
    #     speed = 0

    #     def car_speed(self):
    #         print("My car speed is:", self.speed)

    # honda = Car()

    # honda.no_of_wheels = 4
    # honda.color = "Red"
    # honda.no_of_sheet = 5
    # honda.speed = 180

    # hyundai = Car()

    # hyundai.no_of_wheels = 5
    # hyundai.color = "black"
    # hyundai.no_of_sheet = 4
    # hyundai.speed = 130

    # toyota = Car()

    # toyota.no_of_wheels = 6
    # toyota.color = "white"
    # toyota.no_of_sheet = 7
    # toyota.speed = 260

    # # print(honda.color)
    # # print(hyundai.color)
    # # print(toyota.color)

    # # honda.car_speed()
    # # hyundai.car_speed()
    # # toyota.car_speed()

    # honda.car_speed()

# Constructor method using class

class Car:
    def __init__(self, wheels, color, sheets, speeds, title):
        print("I'm Constructor")

        self.no_of_wheels = wheels
        self.color = color
        self.no_of_sheet = sheets
        self.speed = speeds
        self.title = title

    def __del__(self):
        print("I'm Destructor")

honda = Car(4, "Meroon", 7, 180, "honda")
ford = Car(5, "green", 4, 280, "ford")

print(honda.color, honda.no_of_sheet, honda.no_of_wheels, honda.speed)
print(ford.color, ford.no_of_sheet, ford.no_of_wheels, ford.speed)
