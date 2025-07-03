# Inheritance

class Parent:
    def __init__(self, pName, balance):
        self.bank_balance = balance
        self.name = pName

    def hair_color(self):
        print(f"Parent hair color is brown & parent name is: {self.name}")

class Child(Parent):
    def __init__(self, pName, packet, balance):
        super().__init__(pName, balance)
        self.packet_money = packet

    def college_details(self):
        print("Child studying in XYZ college")

c1 = Child("Siva", 500, 3000)

c1.hair_color()
