from .classes import Player, Room, Item


def create_game():
    # Create rooms
    home = Room("Home", "You are at home with your plant.")

    garden = Room(
        "Garden",
        "There are many beautiful plants here."
    )

    shop = Room(
        "Garden Shop",
        "You can find useful gardening items here."
    )

    greenhouse = Room(
        "Greenhouse",
        "A warm place where plants grow well."
    )

    # Connect rooms
    home.connections["north"] = garden

    garden.connections["south"] = home
    garden.connections["east"] = shop
    garden.connections["north"] = greenhouse

    shop.connections["west"] = garden

    greenhouse.connections["south"] = garden

    # Create items
    watering_can = Item("watering can", 1)
    fertilizer = Item("fertilizer", 1)

    # Put items in rooms
    garden.items.append(watering_can)
    shop.items.append(fertilizer)

    # Ask player information
    name = input("What is your name? ")

    age = int(input("How old are you? "))

    # Create player
    player = Player(name, age, home)

    # Create plant
    plant = {
        "growth": 0,
        "water": 50,
        "health": 100,
        "day": 1
    }

    return player, plant


def show_plant(plant):
    print("\n--- MY PLANT ---")
    print("Growth:", plant["growth"], "/ 100")
    print("Water:", plant["water"], "/ 100")
    print("Health:", plant["health"], "/ 100")
    print("Day:", plant["day"])


def show_room(player):
    print("\n--- ROOM ---")
    print("You are in:", player.room.name)
    print(player.room.description)

    if len(player.room.items) > 0:
        print("Items here:")

        for item in player.room.items:
            print("-", item.name)

    print("Directions:")

    for direction in player.room.connections:
        print("-", direction)


def show_bag(player):
    print("\n--- BAG ---")

    if len(player.items) == 0:
        print("Your bag is empty.")
    else:
        for item in player.items:
            print("-", item.name)


def move(player):
    print("\nWhere do you want to go?")

    for direction in player.room.connections:
        print("-", direction)

    direction = input("Direction: ")

    if direction in player.room.connections:
        player.room = player.room.connections[direction]
        print("You moved to", player.room.name)
    else:
        print("You cannot go there.")


def take_item(player):
    if len(player.room.items) == 0:
        print("There are no items here.")
        return

    print("Items here:")

    for item in player.room.items:
        print("-", item.name)

    name = input("What do you want to take? ")

    for item in player.room.items:
        if item.name == name:
            player.items.append(item)
            player.room.items.remove(item)

            print("You took the", item.name)
            return

    print("That item is not here.")


def water_plant(player, plant):
    has_watering_can = False

    for item in player.items:
        if item.name == "watering can":
            has_watering_can = True

    if has_watering_can == False:
        print("You need a watering can.")
        return

    plant["water"] = plant["water"] + 30

    if plant["water"] > 100:
        plant["water"] = 100

    plant["growth"] = plant["growth"] + 10

    if plant["growth"] > 100:
        plant["growth"] = 100

    print("You watered the plant!")
    print("The plant grew!")


def use_fertilizer(player, plant):
    has_fertilizer = False

    for item in player.items:
        if item.name == "fertilizer":
            has_fertilizer = True

    if has_fertilizer == False:
        print("You need fertilizer.")
        return

    plant["growth"] = plant["growth"] + 20

    if plant["growth"] > 100:
        plant["growth"] = 100

    print("You used fertilizer!")
    print("The plant grew a lot!")


def wait(player, plant):
    plant["day"] = plant["day"] + 1

    plant["water"] = plant["water"] - 20

    if plant["water"] < 0:
        plant["water"] = 0

    print("One day passed.")

    if plant["water"] == 0:
        plant["health"] = plant["health"] - 20
        print("Your plant needs water!")

    else:
        plant["growth"] = plant["growth"] + 5
        print("Your plant grew a little.")


def save_game(player, plant):
    file = open("save.txt", "w")

    file.write("Player: " + player.name + "\n")
    file.write("Age: " + str(player.age) + "\n")
    file.write("Room: " + player.room.name + "\n")
    file.write("Growth: " + str(plant["growth"]) + "\n")
    file.write("Water: " + str(plant["water"]) + "\n")
    file.write("Health: " + str(plant["health"]) + "\n")
    file.write("Day: " + str(plant["day"]) + "\n")

    file.close()

    print("Game saved!")


def load_game():
    try:
        file = open("save.txt", "r")

        print("\n--- SAVE FILE ---")

        for line in file:
            print(line, end="")

        file.close()

    except FileNotFoundError:
        print("There is no save file.")


def check_game(player, plant):

    # Ending 1
    if plant["growth"] >= 100:
        print("\n🌸 Your plant is fully grown!")
        print("You win!")
        return True

    # Ending 2
    if plant["health"] <= 0:
        print("\n🥀 Your plant died.")
        print("Game over.")
        return True

    # Ending 3
    if player.room.name == "Greenhouse":
        if plant["growth"] >= 50:
            print("\n🌿 You are a great gardener!")
            print("Your plant loves the greenhouse.")
            return True

    return False


def menu():
    print("\n========== PLANT GAME ==========")
    print("1. Show plant")
    print("2. Show room")
    print("3. Move")
    print("4. Take item")
    print("5. Water plant")
    print("6. Use fertilizer")
    print("7. Wait one day")
    print("8. Show bag")
    print("9. Save game")
    print("10. Load game")
    print("11. Quit")
    print("================================")


def start_game():

    player, plant = create_game()

    print("\nWelcome to Plant Game!")
    print("Hello", player.name)
    print("Your age is", player.age)

    playing = True

    while playing:

        menu()

        choice = input("Choose an option: ")

        if choice == "1":
            show_plant(plant)

        elif choice == "2":
            show_room(player)

        elif choice == "3":
            move(player)

        elif choice == "4":
            take_item(player)

        elif choice == "5":
            water_plant(player, plant)

        elif choice == "6":
            use_fertilizer(player, plant)

        elif choice == "7":
            wait(player, plant)

        elif choice == "8":
            show_bag(player)

        elif choice == "9":
            save_game(player, plant)

        elif choice == "10":
            load_game()

        elif choice == "11":
            print("Thanks for playing!")
            playing = False

        else:
            print("Please choose 1-11.")

        # Check if game should end
        if check_game(player, plant):
            playing = False
