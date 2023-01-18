class mera:
    def __init__(self):
        pass

    def meraya_Sal(self,mera_boyutu,adet):
        return mera_boyutu*adet

class satış:
    def __init__(self):
        pass

    def satış_yap(self, a=" ", b=""):
        if (self.stok[a] >= int(b)):
            self.stok[a] -= int(b)
            return 1
        else:
            return 0


class Hayvan:

    def __init__(self):
        self.adet = 0
        self.sut_litre = 0
        self.peynir_kilo = 0
        self.yogurt_kilo = 0
        self.kaymak_kilo = 0
        self.dondurma_kilo = 0
        self.tereyagi_kilo = 0
        self.yumurta = 0

    def hayvan_ekle(self, a):
        if (self.adet >= 0):
            self.adet += a
        else:
            return 0

    def hayvan_sil(self, a):
        if (self.adet >= a and self.adet >= 0):
            self.adet -= a
            return 1
        else:
            return 0

    def stok_bilgisi(self):
        print(self.stok)