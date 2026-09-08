import random
collect = []
rahaa = 0

def etsi_jalokiviä():
    x = random.choice(["rubiini", "safiiri", "timantti", "", "", ""])
    if x in ["rubiini", "safiiri", "timantti"]:
        collect.append(x)
        print("\nlöysit jalokiven. lisätty kohde.")
    else:
        print("\nEt löytänyt yhtään jalokiveä.")
    
def näytä_jalokiveä():
    if len(collect) == 0:
        print("\nsinulla ei ole helmiä.")
        return
    print("\nKeräämäsi jalokivet: ")
    for i in collect:
        print(i)

def myydä_jalokiveä():
    global rahaa
    if len(collect) == 0:
        print("\nSinulla ei ole jalokivet myydään.")

    else:
        hinta = {"rubiini": 100, 
         "safiiri": 200, 
         "timantti": 300 }
        summa = 0

        for gem in collect:
         summa += hinta[gem]

        rahaa += summa
        collect.clear()

        print("\nMyit kaikki jalokivet: ", summa,"€")
        print("Sinulla on nyt : ", rahaa, "€")

while True:
    print("\n_______päävalikko_______")
    print("1. Etsi ja kerää jalokivet ")
    print("2. Näytä kerätyt jalokivet ")
    print("3. Myy jalokivet ")
    print("4. Poistu\n")

    valinta = int(input("Valitse yksi vaihtoehto: \n"))

    if valinta == 4:
        print("Kiitos pelaamisesta !")
        break
    elif valinta == 1:
        etsi_jalokiviä()
    elif valinta == 2:
        näytä_jalokiveä()
    elif valinta == 3:
        myydä_jalokiveä()
    else:
        print("virheellinen. Yritä uudelleen.")

        
        

