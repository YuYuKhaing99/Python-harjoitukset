from .hahmo import Hahmo

class Player(Hahmo):
    def __init__(self, nimi, repliikki,numberofplayer):
        super().__init__(self,nimi, repliikki)
        player = []
        super().tulosta_tiedot()
        super().taistelu()

        for p in range(numberofplayer):
           self.player.append(player)
