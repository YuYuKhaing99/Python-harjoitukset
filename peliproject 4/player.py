class Player:

    def __init__(self, name, age):

        self.name = name

        self.age = age

        self.money = 50

        self.seeds = []

        self.crops = []



    def buy_seed(self, seed):

        if self.money >= seed.price:

            self.money -= seed.price

            self.seeds.append(seed)

            print("You bought: ", seed.name, "seeds.")

        else:

            print("You do not have enough money to buy seeds! ")



    def plant_seed(self, farm):

        if len(self.seeds) > 0:

            seed = self.seeds.pop(0)

            farm.add_plant(seed)

            print("You planted: ", seed.name)

        else:

            print("You have no seeds to plant! ")



    def sell_crops(self):

        if len(self.crops) == 0:

            print("You have no crops to sell !")

            return



        total = 0



        for crop in self.crops:

            total += crop.sell_price



        self.money += total

        self.crops.clear()

        print("You earned: ", total, ”€”)

