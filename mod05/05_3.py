num = float(input("Anna luvut: "))

if num != "":
 suurin = float(num)
 pienin = float(num)

while True:

  num = input("Anna luvut: ")

  if num == "":
    break
  
  luku = float(num)

  if luku > suurin: 
   suurin = luku
  elif luku < pienin:
   pienin = luku

print("Pienin luku on: ", pienin)
print("Suurin luku on: ", suurin)


