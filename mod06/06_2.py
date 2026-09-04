n = []

while True:
    x = input("Anna luvut: ")
    if x == "":
        break

    n.append(int(x))
    n.sort(reverse = True)
    
print("Viisi suurinta luvut ovat: ")
for i in n[:5]:
    print(i)
 
