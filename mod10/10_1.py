class Elevator:
    def __init__(self,lowestfloor,highestfloor):
      self.lowestfloor = lowestfloor
      self.highestfloor = highestfloor
      self.curretfloor = lowestfloor

    def moveto_targetfloor(self,targetfloor):
       if self.curretfloor < self.lowestfloor or self.curretfloor > self.highestfloor:
          print("Invalid floor")
       elif self.curretfloor < targetfloor:
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

elevator = Elevator(1,20)
print()
print("Move the elevator to floor 15 :\n")
elevator.moveto_targetfloor(15)
print()
print("Move the elevator to floor 1 :\n")
elevator.moveto_targetfloor(1)