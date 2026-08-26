import random
nimi = input("Pelaajan nimi: ")
ikä = input("Pelaajan ikä: ")

print("Hei", nimi, "!", ikä, "vuotias.")
print("Tervetuloa Kivi_Paperi_Sakset_Peliin")

while True:
 x = ("kivi", "paperi", "sakset")
 pelaja = input ("Valitse kivi, paperi tai sakset: "). lower()
 tietokone = random.choice(x)

 print("sinä valitset: ", pelaja)
 print("tietokoneen valinta: ", tietokone)

 if pelaja == tietokone:
   print("Se on tasapeli!")

 elif pelaja == "kivi" and  tietokone == "sakset":
    print("Sinä voitat !")
 elif pelaja == "sakset" and  tietokone == "paperi":
    print("Sinä voitat !")
 elif pelaja == "paperi" and  tietokone == "kivi":
    print("Sinä voitat !")
 else:
    print("Hävisit pelin !")
 taas = input ("Haluatko pelata uudelleen? (kyllä/ei): ").lower()

 if taas !="kyllä":
   print("Kiitos pelaamisesta! ") 
   break





