import json
from player import Player
from room import Room
from item import Item


def menu():
    print()
    print("=== VEGETABLE FARM ===")
    print("1. Buy seed")
    print("2. Plant")
    print("3. Water")
    print("4. Check growth")
    print("5. Harvest")
    print("6. Sell")
    print("7. Inventory")
    print("8. Balance")
    print("9. Save")
    print("10. Exit")


def buy(player):
    print()
    print("1. Carrot - €3")
    print("2. Tomato - €5")
    print("3. Potato - €4")

    choice = input("Choose seed: ")

    if choice == "1":
        seed = Item("Carrot seed", 3)
    elif choice == "2":
        seed = Item("Tomato seed", 5)
    elif choice == "3":
        seed = Item("Potato seed", 4)
    else:
        print("Invalid choice.")
        return

    if player.balance >= seed.price:
        player.balance -= seed.price
        player.add_item(seed)
        print("Bought", seed.name)
    else:
        print("Not enough money.")


def plant(player, garden):
    if garden.vegetable is not None:
        print("Something is already growing.")
        return

    seeds = []

    for item in player.inventory:
        if "seed" in item.name.lower():
            seeds.append(item)

    if len(seeds) == 0:
        print("You have no seeds.")
        return

    print()
    print("Your seeds:")

    for i in range(len(seeds)):
        print(i + 1, seeds[i].name)

    choice = input("Choose seed: ")

    try:
        number = int(choice)
    except ValueError:
        choice = input("Choose: ").strip()

        return

    if number < 1 or number > len(seeds):
        print("Invalid choice.")
        return

    seed = seeds[number - 1]

    name = seed.name.replace(" seed", "")

    vegetable = Item(name, seed.price * 2)
    vegetable.growth = 0

    player.inventory.remove(seed)
    garden.vegetable = vegetable

    print("You planted", vegetable.name)


def water(garden):
     if garden.vegetable is None:
        print("Nothing to water.")
        return

     garden.vegetable.growth += 25

     if garden.vegetable.growth > 100:
        garden.vegetable.growth = 100

     print("You watered the", garden.vegetable.name)
     print("Growth:", garden.vegetable.growth, "%")



def check_growth(garden):
    if garden.vegetable is None:
        print("Nothing is growing.")
        return

    print(
        garden.vegetable.name,
        "growth:",
        garden.vegetable.growth,
        "%"
    )


def harvest(player, garden):
    if garden.vegetable is None:
        print("Nothing to harvest.")
        return

    if garden.vegetable.growth < 100:
        print("It is not ready.")
        return

    player.add_item(garden.vegetable)

    print("You harvested", garden.vegetable.name)

    garden.vegetable = None


def sell(player):
    vegetables = []

    for item in player.inventory:
        if item.name == "Carrot":
            vegetables.append(item)
        elif item.name == "Tomato":
            vegetables.append(item)
        elif item.name == "Potato":
            vegetables.append(item)

    if len(vegetables) == 0:
        print("No vegetables to sell.")
        return

    total = 0

    for vegetable in vegetables:
        total += vegetable.price

    for vegetable in vegetables:
        player.inventory.remove(vegetable)

    player.balance += total

    print("You earned €", total)




def save(player, garden):


    saved_game = {
        "name1": player.name,
        "age1": player.age,
        "balance1": player.balance,  
        "vegetable1": garden.vegetable.name if garden.vegetable is not None else None,
        "growth1": garden.vegetable.growth if garden.vegetable is not None else 0,
        "inventory1": [item.name for item in player.inventory]   
        
    }

    with open("save1.json", "w") as file:
        json.dump(saved_game, file)


def read_file(filename):

    with open(filename, "r") as file:
        print(file.read())



def load_game():
 try:
     with open("save1.json", "r") as file:
         saved_game = json.load(file)
         return saved_game["name1"], saved_game["age1"], saved_game["balance1"], saved_game["vegetable1"] if saved_game["vegetable1"] else "none", saved_game["growth1"] if saved_game["vegetable1"] else 0, [Item(item_name, 0) for item_name in saved_game["inventory1"]]
 except FileNotFoundError:
         print("No saved game found.")
         return None

def main():

    read_file("./peliprojekti 13/intro.txt")
    print()
    print(".....Instructions.....")
    print()
    read_file("./peliprojekti 13/instructions.txt")
    print()
    save_game = load_game()

    name = input("Name: ").lower()
    if save_game and name == save_game[0]:
        
        choice = input("Do you want to continue the previous game? (yes/no): ").strip().lower()

        if choice == "yes":
            player_name, age, balance, vegetable_name, growth, inventory = save_game
            player = Player(player_name, age)
            player.balance = balance
            garden = Room("Garden")
            shop = Room("Shop")
            market = Room("Market")
            player.location = garden
            player.inventory = inventory
            
            print("Game loaded. Welcome back,", player.name)
            print("Age: ", player.age)
            print("Your balance is €", player.balance)
            for item in player.inventory:
                print("Inventory item:", item.name)
            #print("Your inventory:", player.inventory)
           
            vegetable = Item(vegetable_name, 0)  # Price is not needed for loaded vegetable
            vegetable.growth = growth
            #garden.vegetable = vegetable
            #print("Your vegetable is:", vegetable_name)
            print("Growth:", vegetable.growth, "%")

            if vegetable.name != "none":
                garden.vegetable = vegetable

    else:
        name = input("Name: ")

        try:
            age = int(input("Age: "))
        except ValueError:
            age = 18

        player = Player(name, age)

        # Start with €20
        player.balance = 20

        garden = Room("Garden")
        shop = Room("Shop")
        market = Room("Market")

        player.location = garden

        print()
        print("You start with €20.")
        print("Goal: reach €50.")

    while True:

        menu()

        choice = input("Choose: ").strip()

        if choice == "1":
          print("BUY SELECTED")
          player.location = shop
          buy(player)

        elif choice == "2":
         print("PLANT SELECTED")
         player.location = garden
         plant(player, garden)

        elif choice == "3":
         print("WATER SELECTED")
         player.location = garden
         water(garden)

        elif choice == "4":
          print("GROWTH SELECTED")
          player.location = garden
          check_growth(garden)

        elif choice == "5":
         print("HARVEST SELECTED")
         player.location = garden
         harvest(player, garden)

        elif choice == "6":
            print("SELL SELECTED")
            player.location = market
            sell(player)

        elif choice == "7":
            print("INVENTORY SELECTED")
            player.show_inventory()

        elif choice == "8":
            print("BALANCE SELECTED")
            player.show_balance()

        elif choice == "9":
            print("SAVE SELECTED")
            save(player, garden)

        elif choice == "10":
            print("Thanks for playing!")
            break

        else:
            print("INVALID CHOICE!")

        if player.balance >= 50:
                    print()
                    print("YOU WON!")
                    print("You reached €50!")
                    break


if __name__ == "__main__":
    main()
