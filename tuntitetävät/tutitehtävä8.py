class Airplane:
    def __init__(self, nimi,id,maxfuel):
        self.nimi = nimi
        self.id = id
        self.maxfuel = maxfuel
        self.currentfuel = 0
    

    def tank(self,fuel):
        self.space_tank = self.maxfuel - self.currentfuel
        
        if fuel > self.space_tank:
           self.currentfuel = self.maxfuel
           print("The plane ",self.nimi, "is now added this much fuel: " ,self.space_tank)
        else:
            print("The plane ",self.nimi, "is now added this much fuel: " ,fuel)
               

    def print_data(self):
        for nimi in self.plane:
             print("The entered plane's name: ",self.nimi, "and the ID is :", self.plane[self.id])
             print("The curret fuel now is : ", self.plane[self.currentfuel])

class Airport:
    def __init__(self,nimi,id):
        self.nimi = nimi 
        self.id = id
        self.plane = []

    def add_plane(self,plane):
        self.plane.append(plane)

    def print_plane(self):
        print("The plane is now at ",self.nimi)
        for i in self.plane:
            self.print_data()


plane1 = Airplane("ABC",789,5000)
plane2 = Airplane("DEF",000,6000)
plane3 = Airplane("PPP",676,7000)
airport1 = Airport("Helsinki",123)
airport1.add_plane(plane1)
airport1.add_plane(plane2)
airport1.add_plane(plane3)
plane1.tank(3000)


        