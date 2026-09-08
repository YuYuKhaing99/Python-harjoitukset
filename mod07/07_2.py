import random

def dice(max_luku):
 return random.randint(1,max_luku)

max_luku = int (input("Anna maksimisilmäluku: "))

while True:
  roll = dice(max_luku)
  print(roll)

  if roll == max_luku:
   break