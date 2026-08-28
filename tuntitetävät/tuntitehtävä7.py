
valinta = input ("Valitse +, -, x, stop: ")
num1 = float(input ("Anna numero 1: "))
num2 = float(input ("Anna numero 2: "))

while valinta != "stop":
  
  if valinta == "+":
    summa = num1 + num2
    print("Tulos on : ", summa )
  elif valinta == "-":
    minus = num1 - num2
    print("Tulos on : ", minus )
  elif valinta == "x":
    kertaa = num1 * num2
    print("Tulos on : ", kertaa )
    
  valinta = input (" Valitse +, -, x, stop: ")
  if valinta == "stop":
    break
  num1 = float(input ("Anna numero 1: "))
  num2 = float(input ("Anna numero 2: "))







