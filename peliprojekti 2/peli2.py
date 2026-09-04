import random
valinta = ["€", "#", "%", "?"]
rahaa = 150

ikä = int(input("Kuinka vuotta olet?"))

if ikä < 12:
    print("Olet alaikäinen. Et voi pelata.")
    exit()

print("\nTervetuloa! Kolme rullan kolikkopeliin.")

def print_menu():
    print(" \n_________Päävalikko__________")
    print("1- pyörähdys")
    print("2- saldo")
    print("3- päivittäiset palkinnot")
    print("4- miten pelata")
    print("5- uloskäynti \n")
print_menu()

while True:
    komento = input ("Anna komento: ")

    if komento == "5":
        break
    elif komento == "1":
        if rahaa < 20:
            print("Sinulla ei ole tarpeeksi rahaa pyörittämiseen.")
        else:
         rahaa -= 20

         kelat = [random.choice(valinta), 
                  random.choice(valinta), 
                  random.choice(valinta)]

         print("\nSpinning.....")
         print("___".join(kelat))

         if kelat[0] == kelat[1] == kelat[2]:
             if kelat[0] == "€" and kelat[1] == "€" and kelat[2] == "€" :
              win = 100
              print("Suuria voittoja! Saat 100 € ")
             else:
              win = 50
              print("Kolme ottelua! Saat 50€ ")
             rahaa += win

         elif (kelat[0] == kelat[1] or kelat[0]== kelat[2] or kelat[1]== kelat[2]):
             rahaa += 20
             print("Kaksi paria! Saat 20 €")
         else:
            print("Ei osumaa, yritä uudelleen!")

    elif komento == "2":
       print( "Nykyinen saldosi on:", rahaa)
    elif komento == "4":
       print("Valitse valikkoriviltä. Valita 1- pyöräytys aloittaaksesi pelin."
             "Jos saat kolme €, saat 100 € suurvoiton. Jos saat kolme samaa, saat 50 €."
             "Jos saat kaksi samaa, saat 20 €. Yksi pyöräytys maksaa 20 €."
             "Voit lunastaa päivittäisen palkinnon ja saada 10 € päivässä.")
    elif komento == "3":
        rahaa += 10
        print("Saat päivittäisen palkinnon 10 €. Saldosi on nyt:", rahaa)
    else:
       print("Virheellinen komento, valitse uudelleen!")

    print_menu()
print("Kiitos pelamisesta!")
print("Kokonaissaldo: ", rahaa)

