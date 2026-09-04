count = 1

while count < 6:
    x = input("Käyttäjätunnus : ")
    y = input("Salasana : ")

    if x == "python" and y == "rules":
        print("Tervetuloa !")
        break
    elif count == 5:
        print("Pääsy evätty.")

    count += 1


    
    