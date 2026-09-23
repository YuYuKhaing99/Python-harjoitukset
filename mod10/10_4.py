import random

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

    def go(self):
        self.distance += self.current_speed


class Race:
    def __init__(self, name, length,cars):
        self.name = name
        self.length = length
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.go()

    def print_status(self):
        print("\nRace status:")
        print("-" * 55)
        print(f"{'Car':<15}"
              f"{'Speed':<15}"
              f"{'Distance':<15}")
        print("-" * 55)

        for car in self.cars:
            print(
                f"{car.registration_number:<15}"
                f"{car.current_speed:<15}"
                f"{car.distance:<15.1f}"
            )

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.length:
                return True

        return False

cars = []
for i in range(1, 11):
    registration = f"ABC-{i}"
    maximum_speed = random.randint(150, 200)

    car = Car(registration, maximum_speed)
    cars.append(car)

race = Race("Suuri romuralli", 8000,cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"\nAfter {hours} hours:")
        race.print_status()

print(f"\nThe race is finished after {hours} hours!")
race.print_status()