class Hahmo:
    def __init__(self, nimi, repliikki):
        self.nimi = nimi
        self.repliikki = repliikki
        self.hp = 100

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")

    def taistelu(self, vastustaja):
        print("Tulee suuri taistelu.")
        input()
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            self.hp = 0
        else:
            print(f"{self.nimi} voitti taistelun!")
            self.tulosta_tiedot()

class Monster(Hahmo):
    def __init__(self, nimi, repliikki):
        super.__init__(self,nimi, repliikki)
        Hahmo.tulosta_tiedot()

class Player(Hahmo):
    def __init__(self, nimi, repliikki,numberofplayer):
        super.__init__(self,nimi, repliikki)
        Hahmo.tulosta_tiedot()
        Hahmo.taistelu()



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