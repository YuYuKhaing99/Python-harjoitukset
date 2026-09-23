import random
class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, change):
        if self.current_speed + change <= 0:
            self.current_speed = 0
        elif self.current_speed + change > self.top_speed:
            self.current_speed = self.top_speed
        else:
            self.current_speed += change
            return self.current_speed
        
    def go(self,hour):
        self.distance_traveled += self.current_speed * hour

    def print_status(self):
        print(
            f"{self.registration_number:<16}"
            f"{self.top_speed:<16}"
            f"{self.current_speed:<16}"
            f"{self.distance_traveled:<16.0f}"
        )

cars = []

for i in range(1, 11):
    registration_number = f"ABC-{i}"
    top_speed = random.randint(100, 200)
    cars.append(Car(registration_number, top_speed))


while True:

    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)

    for car in cars:
        car.go(1)

    if any(car.distance_traveled >= 10000 for car in cars):
        break

print("\nFinal race results:")
print("-" * 55)
print(
    f"{'Registration':<16}"
    f"{'Top speed':<16}"
    f"{'Current speed':<16}"
    f"{'Distance':<16}"
)
print("-" * 55)

for car in cars:
    car.print_status()
        