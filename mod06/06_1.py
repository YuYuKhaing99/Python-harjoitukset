import random
n = int(input("Anna arpakuutioiden lukumäärän: "))
summa = 0

for i in range(n):
    ran = random.randint(1,6)
    summa += ran

print("Silmälukujen summa on: ", summa)



