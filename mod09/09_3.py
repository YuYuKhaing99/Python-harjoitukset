class Auto:
    def __init__(self,speed,distance):
        self.speed = speed
        self.distance = distance

    def drive(self,hour):
        self.distance += hour * self.speed
        return self.distance
auto1 = Auto(60,2000)
auto1.drive(float(1.5))
print(f"The Car's present distance is  : {auto1.distance} ")
