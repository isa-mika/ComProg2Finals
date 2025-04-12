class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(f"{self.brand} is moving...")

class SchoolBus(Vehicle):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def move(self):
        print(f"{self.brand} school bus with {self.capacity} capacity is moving.")

def run_question1():
    bus = SchoolBus("Hyundai", 30)
    print("Is School Bus an instance of Vehicle?", isinstance(bus, Vehicle))
    bus.move()
