import random

x = (2,3,4,5,6,7,8,9)
tietokone = random.choice(x)


while True:

    num = int(input("Arvaa kokonaisluvun väliltä 1..10: "))
    if num == tietokone:
     print("Oikein! ")
     break

    if num > tietokone:
        print("Liian suuri arvaus !")
    elif num < tietokone:
        print("Liian pieni arvaus !")

