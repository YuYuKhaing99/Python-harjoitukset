
valinta = input ("Valitse +, -, x, stop: ")
num1 = float(input ("Anna numero 1: "))
num2 = float(input ("Anna numero 2: "))

while valinta != "stop":
  
  if valinta == "+":
    tulos = num1 + num2
    
  elif valinta == "-":
    tulos = num1 - num2
    
  elif valinta == "x":
    tulos = num1 * num2
    
  print("Tulos on : ", tulos )  
  valinta = input (" Valitse +, -, x, stop: ")
  if valinta == "stop":
    break
  num1 = float(input ("Anna numero 1: "))
  num2 = float(input ("Anna numero 2: "))







