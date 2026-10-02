from hahmoluoka import Monster, Player

monster = Monster("Zoro", "Run quick, I will catch u!")
player = Player ("Kiro", "I am faster than u, u can't catch me....",2)

print("Game start!!")
player.tulosta_tiedot()
input()

print(f"{Player.nimi} kohtaa ensimmäiseksi kauhean hirviön. Hirviö huutaa:")
print(monster.repliikki)
monster.tulosta_tiedot()

input()
player.taistelu(monster)
input()
print(f"Peli ohi.")