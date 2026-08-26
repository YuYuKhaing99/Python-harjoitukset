x = float(input("Anna leiviskät. \n"))
leiviskä = x * 20 * 32 * 13.3
y = float(input("Anna naulat. \n"))
naula = y * 32 * 13.3
z = float(input("Anna luodit. \n"))
luoti = z * 13.3
summa = leiviskä + naula + luoti
kilo = int(summa // 1000)
gramma = summa % 1000
print("Massa nykymittojen mukaan: "  + str(kilo) + " kg" +  " ja "  +  str(round(gramma, 2))+ " g")

