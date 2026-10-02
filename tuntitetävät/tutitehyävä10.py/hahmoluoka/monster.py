from .hahmo import Hahmo

class Monster(Hahmo):
    def __init__(self, nimi, repliikki):
        super().__init__(nimi, repliikki)
        super().tulosta_tiedot()