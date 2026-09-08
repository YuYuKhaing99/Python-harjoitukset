def convert_litre(gallona):
    return gallona * 3.785

gallona = float(input("Anna gallona: "))

while True:
    if gallona < 0:
        break

    else: 
      litre = convert_litre(gallona)
      print("Annettu gallona litroiksi: ", litre)
      gallona = float(input("Anna gallona: "))
