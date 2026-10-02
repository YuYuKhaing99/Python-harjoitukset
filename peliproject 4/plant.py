class Plant:

    def __init__(self, name, price, sell_price):

        self.name = name

        self.price = price

        self.sell_price = sell_price

        self.growth = 0

        self.watering= False



  def grow(self):

        if self.water:

            self.growth += 25

            self.watering= False



            if self.growth > 100:

                self.growth = 100



def water(self):

        self.watering= True

