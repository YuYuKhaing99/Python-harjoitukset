class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balance = 20
        self.inventory = []
        self.location = None

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("\nInventory:")
        for item in self.inventory:
            print("-", item.name)

    def show_balance(self):
        print("Balance: €", self.balance)

