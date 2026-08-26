vuosi = int(input("Anna vuosi: "))
check = vuosi % 4
if vuosi == 2020:
    print("2020 ei ollut olympialaisia, mutta 2021 poikkeukselliseti oli. (Syynä oli korona).")

elif check == 0:
    print("Se ollut olympiavuosi ! ")

elif check != 0:
    print ("Ei ollut olympiavuosi ! ")
