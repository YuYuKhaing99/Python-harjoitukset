class Room:
    def __init__(self, name):
        self.name = name
        self.vegetable = None

    def show(self):
        if self.vegetable:
            print(self.vegetable.name,
                  "-", self.vegetable.growth, "%")
        else:
            print("Nothing is growing here.")