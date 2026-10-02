from plant import Plant

from farm import Farm

from player import Player





def menu():

    print("\n--- FARM GAME ---")

    print("1. Buy seeds")

    print("2. Plant seed")

    print("3. Water plants")

    print("4. Grow plants")

    print("5. Check plants")

    print("6. Harvest")

    print("7. Sell crops")

    print("8. Show money")

    print("9. Show inventory")

    print("10. Save game")

    print("11. Load game")

    print("12. Exit")





def buy_seeds(player):

    print("\nSeeds:")

    print("1. Carrot - €5")

    print("2. Tomato - €10")

    print("3. Pumpkin - €15")



    choice = input("Choose seed: ")



    if choice == "1":

        seed = Plant("Carrot", 5, 10)

        player.buy_seed(seed)



    elif choice == "2":

        seed = Plant("Tomato", 10, 20)

        player.buy_seed(seed)



    elif choice == "3":

        seed = Plant("Pumpkin", 15, 35)

        player.buy_seed(seed)



    else:

        print("Wrong choice.")





def harvest(player, farm):

    for plant in farm.plants[:]:



        if plant.growth >= 100:

            player.crops.append(plant)

            farm.plants.remove(plant)



            print("You harvested", plant.name)



        else:

            print(

                plant.name,

                "is not ready yet."

            )





def save_game(player):

    file = open("save.txt", "w")



    file.write(player.name + "\n")

    file.write(str(player.age) + "\n")

    file.write(str(player.money) + "\n")



    file.close()



    print("Game saved.")





def load_game(player):

    try:

        file = open("save.txt", "r")



        player.name = file.readline().strip()

        player.age = int(file.readline())

        player.money = int(file.readline())



        file.close()



        print("Game loaded.")



    except FileNotFoundError:

        print("No save file found.")





def start_game():



    print("================================")

    print("         MY FARM GAME")

    print("================================")



    name = input("Enter your name: ")



    age = int(input("Enter your age: "))



    player = Player(name, age)

    farm = Farm()



    print("\nWelcome", player.name)

    print("You have €50.")



    while True:



        menu()



        choice = input("Choose: ")



        if choice == "1":

            buy_seeds(player)



        elif choice == "2":

            player.plant_seed(farm)



        elif choice == "3":

            farm.water_plants()

            print("You watered your plants.")



        elif choice == "4":

            farm.grow_plants()

            print("Your plants grew.")



        elif choice == "5":

            farm.show_plants()



        elif choice == "6":

            harvest(player, farm)



        elif choice == "7":

            player.sell_crops()



        elif choice == "8":

            print("Money: €", player.money)



        elif choice == "9":



            print("\nSeeds:")



            for seed in player.seeds:

                print("-", seed.name)



            print("Crops:")



            for crop in player.crops:

                print("-", crop.name)



        elif choice == "10":

            save_game(player)



        elif choice == "11":

            load_game(player)



        elif choice == "12":

            print("Thanks for playing!")

            break



        else:

            print("Wrong choice.")

