luku = int(input("Anna luku: "))
summa = 0

while True:
    if luku == 0:
        break
    else:
        summa += luku
        luku = int(input("Anna luku: "))

print("Sum: ", summa)