import math

def unit_hinta(halkaisija,hinta):
    halkaisija_m = halkaisija / 100
    säde = halkaisija_m / 2
    pinta_ala = math.pi * säde **2
    unit_price = hinta / pinta_ala
    return unit_price

halkaisija1 = float(input("Anna pitsan.1 halkaisija in cm : "))
halkaisija2 = float(input("Anna pitsan.2 halkaisija in cm : "))
hinta1 = float(input("Anna pitsan.1 hinta in € : "))
hinta2 = float(input("Anna pitsan.2 hinta in € : "))


p1 = unit_hinta(halkaisija1, hinta1)
p2 = unit_hinta(halkaisija2, hinta2)

print("unit hinta1: ", p1, "€/m square")
print("unit hinta2: ", p2, "€/m square")

if p1 < p2:
    print("Pizza 1 tarjoaa paremman vastineen rahalle.")
elif p2 < p1:
    print("Pizza 2 tarjoaa paremman vastineen rahalle")
else:
    print("Pitsa 1 ja pitsa 2 on sama hinta.")

