class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        self.distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class CombustionCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_size):
        super().__init__(registration_number, maximum_speed)
        self.tank_size = tank_size



electric_car = ElectricCar("ABC-15",180,52.5)
combustion_car = CombustionCar("ACD-123",165,32.3)

electric_car.current_speed = 100
combustion_car.current_speed = 120

electric_car.drive(3)
combustion_car.drive(3)

print("Electric car:")
print(f"Registration: {electric_car.registration_number}")
print(f"Distance: {electric_car.distance} km")

print()

print("Combustion car:")
print(f"Registration: {combustion_car.registration_number}")
print(f"Distance: {combustion_car.distance} km")
