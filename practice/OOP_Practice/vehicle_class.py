class Vehicle:
    color = "White"
    
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity}."

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)

    def fare(self):
        normal_fare = super().fare()
        normal_fare += normal_fare * .10
        return normal_fare


def main():
    car1 = Vehicle('Volvo', 36, 6)
    bus1 = Bus('Big Yellow Bus', 12, 50)

    print(bus1.fare())
    print(bus1.seating_capacity())


if __name__ == '__main__':
    main()