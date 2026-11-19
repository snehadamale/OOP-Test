
class Vehicle:
    def __init__(self, persons):
        self.persons = persons

    def calculate_toll(self):
        pass
class TwoWheeler(Vehicle):
    def calculate_toll(self):
        toll = 20
        if self.persons > 2:
            toll += (self.persons - 2) * 10
        return toll
class ThreeWheeler(Vehicle):
    def calculate_toll(self):
        toll = 30
        if self.persons > 3:
            toll += (self.persons - 3) * 20
        return toll
class FourWheeler(Vehicle):
    def calculate_toll(self):
        toll = 40
        if self.persons > 4:
            toll += (self.persons - 4) * 40
        return toll
class HeavyVehicle(Vehicle):
    def calculate_toll(self):
        toll = 60
        if self.persons > 6:
            toll += (self.persons - 6) * 100
        return toll
while True:
    print("\n1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")
    ch = int(input("Enter choice: "))

    if ch == 5:
        break

    persons = int(input("Enter number of persons: "))

    if persons <= 0:
        print("Invalid persons")
        continue

    if ch == 1:
        v = TwoWheeler(persons)

    elif ch == 2:
        v = ThreeWheeler(persons)

    elif ch == 3:
        v = FourWheeler(persons)

    elif ch == 4:
        v = HeavyVehicle(persons)

    else:
        print("Invalid choice")
        continue

    print("Total Toll =", v.calculate_toll())
