import random

def dice():
    return random.randint(1,6)

while True:
     ram = dice()
     print(ram)

     if ram == 6:
      break
    