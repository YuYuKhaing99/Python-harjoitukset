class Auto:
  def __init__(self,liscence,topspeed):
    self.liscence = liscence
    self.topspeed = topspeed
    self.speed = 0
    self.distance = 0

  def acceleration(self,change):
      if self.speed + change <= 0:
        self.speed = 0
      elif self.speed + change > self.topspeed:
        self.speed = self.topspeed
      else:
        self.speed += change
      return self.speed

auto1 = Auto("ABC123", 142)
auto1.acceleration(30)
auto1.acceleration(70)
auto1.acceleration(50)
print(f"The Car's present speed is  : {auto1.speed} ")
auto1.acceleration(-200)
print(f"The Car's present speed is  : {auto1.speed} ")

