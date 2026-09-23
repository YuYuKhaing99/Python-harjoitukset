class Auto:
  def __init__(self,liscence,topspeed):
    self.liscence = liscence
    self.topspeed = topspeed
    self.speed = 0
    self.distance = 0

auto1 = Auto("ABC123", 142)

print(f"The registered car's liscence is  : {auto1.liscence} and the speed is : {auto1.speed}")


