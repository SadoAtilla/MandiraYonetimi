from abc import abstractmethod


class satış:
    def satış_yap(self, a=" ", b = ""):
        if(self.stok[a]>= int(b)):
            self.stok[a] -= int(b)

class Hayvan():

    def __init__(self):
        self.adet = 0
        self.sut_litre = 0
        self.peynir_kilo = 0
        self.yogurt_kilo = 0
        self.kaymak_kilo = 0
        self.dondurma_kilo = 0
        self.tereyagi_kilo = 0
        self.yumurta = 0

    def hayvan_ekle(self,a):
        if(self.adet>= 0):
            self.adet += a
        else:
            print("Mümkün olan bi değer giriniz.")

    def hayvan_sil(self,a):
        if (self.adet >= a and self.adet >=0):
            self.adet -= a
        else:
            print("Mümkün olan bi değer giriniz.")

    @abstractmethod
    def yem_ver(self):
        pass

    def meraya_sal(self):
        print("Meraya salındı..")

    def su_ver(self):
        print("Su verildi..")

    def stok_bilgisi(self):
        print(self.stok)



class inek(Hayvan,satış):

    def __init__(self):
        super().__init__()
        self.stok = {"inek sütü": 0, "inek kaymağı": 0, "inek peyniri": 0, "inek tereyağı": 0, "inek dondurması": 0,"inek yoğurdu": 0,}

    def sut_sag(self):
        self.sut_litre += self.adet * 15
        print(self.adet * 15 , " litre süt sağıldı..")
        print("Toplam süt litresi : ", self.sut_litre)
        self.stok["inek sütü"] += self.sut_litre



    def yem_ver(self):
        print(self.adet*10," kilo yem verildi..")

    def kaymak_uret(self, kilo):
        if (self.sut_litre >= kilo):
            print(kilo, " kaymak üretildi")
            self.kaymak_kilo += kilo
            self.stok["inek kaymağı"] += self.kaymak_kilo

        else:
            print("Stoğunuzda yeteri kadar süt bulunmuyor.")

    def peynir_uret(self,kilo):
        if (self.sut_litre >= kilo * 10):
            print(kilo, " kilo peyniri üretildi")
            self.sut_litre -= kilo * 10
            print(self.sut_litre)
            self.stok["inek peyniri"] += self.peynir_kilo

        else:
            print("Stoğunuzda yeteri kadar sütü bulunmuyor.")

    def yogurt_uret(self, kilo):
        if (self.sut_litre >= kilo):
            print(kilo, "yogurtu üretildi")
            self.sut_litre -= kilo
            print(self.sut_litre)
            self.yogurt_kilo += kilo
            self.stok["inek yoğurdu"] += self.yogurt_kilo

        else:
            print("Stoğunuzda yeteri kadar sütü bulunmuyor.")

    def dondurma_uret(self,kilo):
        if(self.sut_litre >= kilo):
            print(kilo, " dondurma üretildi")
            self.sut_litre -= kilo
            print(self.sut_litre)
            self.dondurma_kilo += kilo
            self.stok["inek dondurması"] += self.dondurma_kilo

        else:
            print("Stoğunuzda yeteri kadar süt bulunmuyor.")

    def tereyagi_uret(self,kilo):
        if(self.sut_litre >= kilo*5):
            print(kilo, " tereyagi üretildi")
            self.sut_litre -= kilo * 5
            print(self.sut_litre)
            self.tereyagi_kilo += kilo
            self.stok["inek tereyağı"] += self.tereyagi_kilo

        else:
            print("Stoğunuzda yeteri kadar süt bulunmuyor.")


class keci(Hayvan,satış):
    def __init__(self):
        super().__init__()
        self.stok = {"keci sütü": 0, "keci yoğurdu": 0,"keci peyniri": 0, "keci dondurması": 0}

    def sut_sag(self):
        self.sut_litre += self.adet * 7
        print(self.adet * 7," litre süt sağıldı..")
        print("Toplam süt litresi : ",self.sut_litre)
        self.stok["keci sütü"] += self.sut_litre


    def yem_ver(self):
        print(self.adet*5," kilo yem verildi")



    def peynir_uret(self, kilo):
        if (self.sut_litre >= kilo * 10):
            print(kilo, " kilo peyniri üretildi")
            self.sut_litre -= kilo * 10
            print(self.sut_litre)
            self.peynir_kilo += kilo
            self.stok["keci peyniri"] += self.peynir_kilo

        else:
            print("Stoğunuzda yeteri kadar sütü bulunmuyor.")

    def yogurt_uret(self, kilo):
        if (self.sut_litre >= kilo):
            print(kilo, "yogurtu üretildi")
            self.sut_litre -= kilo
            print(self.sut_litre)
            self.yogurt_kilo += kilo
            self.stok["keci yoğurdu"] += self.yogurt_kilo

        else:
            print("Stoğunuzda yeteri kadar sütü bulunmuyor.")

    def dondurma_uret(self, kilo):
        if (self.sut_litre >= kilo):
            print(kilo, " dondurma üretildi")
            self.sut_litre -= kilo
            print(self.keci_sutu)
            self.dondurma_kilo += kilo
            self.stok["keci dondurması"] += self.dondurma_kilo

        else:
            print("Stoğunuzda yeteri kadar süt bulunmuyor.")




class koyun(Hayvan,satış):
    def __init__(self):
        super().__init__()
        self.stok = {"koyun sütü": 0, "koyun peyniri": 0, "koyun yoğurdu": 0}

    def sut_sag(self):
        self.sut_litre += self.adet * 7
        print(self.adet * 7, " litre süt sağıldı..")
        print("Toplam süt litresi : ", self.sut_litre)
        self.stok["koyun sütü"] += self.sut_litre


    def yem_ver(self):
        print(self.adet * 5, " kilo yem verildi")


    def peynir_uret(self, kilo):
        if (self.sut_litre >= kilo * 10):
            print(kilo, " kilo peyniri üretildi")
            self.sut_litre -= kilo * 10
            print(self.sut_litre)
            self.peynir_kilo += kilo
            self.stok["koyun peyniri"] += self.peynir_kilo

        else:
            print("Stoğunuzda yeteri kadar sütü bulunmuyor.")

    def yogurt_uret(self, kilo):
        if (self.sut_litre >= kilo):
            print(kilo, "yogurtu üretildi")
            self.sut_litre -= kilo
            print(self.sut_litre)
            self.yogurt_kilo += kilo
            self.stok["koyun yoğurdu"] += self.yogurt_kilo

        else:
            print("Stoğunuzda yeteri kadar sütü bulunmuyor.")


class tavuk(Hayvan,satış):
    def __init__(self):
        super().__init__()
        self.stok = {"yumurta": 0}


    def yumurta_topla(self):
        self.yumurta += self.adet
        print(self.yumurta, " adet yumurta toplandı..")
        self.stok["yumurta"] += self.yumurta



    def yem_ver(self):
        print(self.adet /8 , " kilo yem verildi..")









inekk = inek()
koyun = koyun()
keci = keci()
tavuk = tavuk()

inekk.hayvan_ekle(100)
koyun.hayvan_ekle(101)
keci.hayvan_ekle(102)
tavuk.hayvan_ekle(103)

print(inekk.adet)
print(koyun.adet)
print(keci.adet)
print(tavuk.adet)

keci.sut_sag()
keci.yogurt_uret(50)
keci.peynir_uret(10)


tavuk.yumurta_topla()

inekk.hayvan_ekle(100)
inekk.sut_sag()
inekk.kaymak_uret(10)
inekk.stok_bilgisi()
tavuk.stok_bilgisi()
keci.stok_bilgisi()
koyun.stok_bilgisi()
print("----------------------------------------------------------")
tavuk.satış_yap("yumurta","5")
tavuk.stok_bilgisi()
inekk.satış_yap("inek sütü", "100")
inekk.stok_bilgisi()


