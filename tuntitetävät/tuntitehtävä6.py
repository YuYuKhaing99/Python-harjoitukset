nimi = input("Anna nimesi: ")
ruoka = input("Valitse kasvi tai normmali ruokaa ")
print(nimi + " halua kokeilla kouluun ruokasta. " + " Ottaako " + nimi + " kasvi tai normaali ruokaa ?")
if ruoka == "kasvi":
    print("Tänään kasvisruoka on kasvispulla ja kastike. " +nimi+ " ei tykää.")
else:
    print("Tänään nurmaaliruoka on lihaapulla ja juusto kastike. " +nimi+ " tykää.")
    
