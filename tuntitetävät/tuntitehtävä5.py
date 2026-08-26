pitkä = int(input("Kuninka pitkä olet: "))
ikä = int(input("Kuninka vuotias olet: "))

if 140 >= pitkä > 100 and ikä > 8:
    print("Saat mennä lasten laitteisiin.")

elif 195 > pitkä > 140 and ikä > 8:
    print("Saat mennä kaikkiin laitteisiin.")

elif pitkä  >= 195 and ikä < 8:
    print("Et saa mennä Kirnuun.")

else:
    print("Et saa mennä mitä laitteisiin.")

 
     
    