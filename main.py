class Vehicle:
    def __init__(self, brand: str, speed: int):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, brand: str, speed: int, fuel_type: str):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type


class Bike(Vehicle):
    def __init__(self, brand: str, speed: int, bike_type: str):
        super().__init__(brand, speed)
        self.bike_type = bike_type


car = Car("Toyota", 120, "Petrol")
bike = Bike("Giant", 35, "Mountain")

car.move()
bike.move()
