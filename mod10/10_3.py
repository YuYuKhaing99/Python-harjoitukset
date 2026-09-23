class Elevator:

    def __init__(self, lowestfloor, highestfloor):
        self.lowestfloor = lowestfloor
        self.highestfloor = highestfloor
        self.curretfloor = lowestfloor

    def moveto_targetfloor(self, targetfloor):
        if targetfloor < self.lowestfloor or targetfloor > self.highestfloor:
            print("Invalid floor")
            return

        if self.curretfloor < targetfloor:
            while self.curretfloor < targetfloor:
                self.up_floor()

        elif self.curretfloor > targetfloor:
            while self.curretfloor > targetfloor:
                self.down_floor()

    def down_floor(self):
        if self.curretfloor > self.lowestfloor:
            self.curretfloor -= 1
            print(f"The elevator is now at: {self.curretfloor} floor")

    def up_floor(self):
        if self.curretfloor < self.highestfloor:
            self.curretfloor += 1
            print(f"The elevator is now at: {self.curretfloor} floor")


class House:

    def __init__(self, lowestfloor, highestfloor, number_of_elevators):
        self.lowest_floor = lowestfloor
        self.highest_floor = highestfloor
        self.elevators = []

        for i in range(number_of_elevators):
            elevator = Elevator(lowestfloor, highestfloor)
            self.elevators.append(elevator)

    def ride_elevator(self, elevator_number, targetfloor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print("Invalid elevator number.")
            return

        elevator = self.elevators[elevator_number - 1]
        elevator.moveto_targetfloor(targetfloor)

    def firealarm(self):
        print("\nFire alarm !!! All the elevators down to lowest level.\n")
        for elevator in self.elevators:
            elevator.moveto_targetfloor(self.lowest_floor)
            print("")
house = House(1, 20, 3)

print("\nElevator 1:")
house.ride_elevator(1, 11)

print("\nElevator 2:")
house.ride_elevator(2, 8)

print("\nElevator 3:")
house.ride_elevator(3, 14)

house.firealarm()
    