num = int (input("Anna kokonaisluku: "))

if num < 2:
    print("Ei ole alkuluku.")

for i in range(2,num):
    if num % i == 0:
        print("Ei ole alkuluku.")
        break

else:
    print("Se on alkuluku.")