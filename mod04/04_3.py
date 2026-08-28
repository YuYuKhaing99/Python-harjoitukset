suku = input("Anna sukupuolesi (nainen / mies): ")
hemo = int(input("Anna hemoglobiiniarvon (g/l): "))

if 117 <= hemo <= 175 and suku == "nainen":
    print("Hemoglobiiniarvo on normaali. ")
elif hemo < 117 and suku == "nainen":
    print("Hemoglobiiniarvo on alhainen. ")
elif hemo >175 and suku == "nainen":
    print("Hemoglobiiniarvo on korkea. ")
elif 134 <= hemo <= 195:
    print("Hemoglobiiniarvo on normaali. ")
elif hemo < 134:
    print("Hemoglobiiniarvo on alhainen. ")
else:
    print("Hemoglobiiniarvo on korkea. ")
    


