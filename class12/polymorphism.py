# Lambda Function:

    # demo = lambda a, b: a * b

    # print(demo(2, 3))

# Polymorphism

class Animal:
    def speak(self):
        print("Animal's are speaking")

class Dog(Animal):
    def speak(self):
        print("Dog is Bow Bow")

class Cat(Animal):
    def speak(self):
        print("Cat is Meow Meow")

for ani in [Animal(), Dog(), Cat()]:
    ani.speak()