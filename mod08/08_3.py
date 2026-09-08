lentokenttä = {}
while True:
  print("_____LENTOASEMAVALIKKO_____")
  print("1. Syötä uusi lentokenttä") 
  print("2. Etsi lentokenttä") 
  print("3. Lopeta")

  valinta = int(input("Valitse yksi vaihtoehto: "))

  if valinta == 1:
     x = input("Anna uusi ICAO koodi: ")
     y = input("Anna uusi lentokentän nimi: ")
     lentokenttä[x] = y
     print("Uusi lentokenttä lisätty.")

  elif valinta == 2:
     z = input("Anna ICAO koodi: ")
     if z in lentokenttä:
      print("Sen lentokentän nimi on: ", lentokenttä[z]) 
     else:
        print("Ei löydy.")

  elif valinta == 3:
     break
  
  else:
     print("virheellinen syöte!")
