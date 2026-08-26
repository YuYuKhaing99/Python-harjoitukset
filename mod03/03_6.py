import random
kolmekoodi = ( str(random.randint(0, 9)) +
               str(random.randint(0, 9)) +
               str(random.randint(0, 9)))
neljäkoodi = ( str(random.randint(1, 6)) +
               str(random.randint(1, 6)) +
               str(random.randint(1, 6)) +
               str(random.randint(1, 6)))
print("Kolmenumeroinen koodi: " + str(kolmekoodi))
print("Neljänumeroinen koodi: " + str(neljäkoodi))

