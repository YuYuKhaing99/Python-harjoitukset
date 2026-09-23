num = int (input("Anna luku: "))
list = []
count = 0
sum = 0
even = 0
odd = 0

while num != 0:
    list.append(num)

    for i in list:
     count += 1
     sum += i
     if i % 2 == 0:
        even += 1
     else:
        odd += 1

    num = int (input("Anna luku: "))

keskiarvo = sum / count
print("Lukujen määrä:" ,count)
print("Lukujen summa:" ,sum)
print("Lukujen keskiarvo:" ,keskiarvo)
print("Lukujen even:" ,even)
print("Lukujen odd:" ,odd)
