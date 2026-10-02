class Farm:

    def __init__(self):

        self.plants = []



    def add_plant(self, plant):

        self.plants.append(plant)



    def show_plants(self):

        if len(self.plants) == 0:

            print("You don’t have plants yet!")

        else:

            for plant in self.plants:

                print(

                    f”{plant.name} is now growing:                                               

                        {plant.growth}%

                )



    def water_plants(self):

        for plant in self.plants:

            plant.water()



def grow_plants(self):

        for plant in self.plants:

            plant.grow()

