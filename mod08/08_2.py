nimi = set()

while True:
    x = input("Anna nimi: ")
    if x == "":
        break
    if x in nimi:
      print("Tämä nimi on jo syötetty....")
    else:
        nimi.add(x)
        print("Uusi nimi....")


print("\nKaikki syötetyt nimet: ")
for i in nimi:
    print(i)