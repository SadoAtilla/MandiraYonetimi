from abc import abstractmethod


class hayvan():

    def __init__(self,adet):
        self.adet = adet
        self.sut_litre = 0
        self.peynir_kilo = 0
        self.yogurt_kilo = 0
        self.kaymak_kilo = 0
        self.dondurma_kilo = 0
        self.tereyagi_kilo = 0

    @abstractmethod
    def yem_ver(self):
        pass

    def meraya_sal(self):
        print("Meraya salındı..")

    def su_ver(self):
        print("Su verildi..")

    def peynir_uret(self,kilo):
        print(kilo , " kilo peynir üretildi")
        self.sut_litre -= kilo*10
        print(self.sut_litre)
        self.peynir_kilo += kilo


    def kaymak_uret(self,kilo):
        print(kilo, " kaymak üretildi")
        self.kaymak_kilo += kilo

    def yogurt_uret(self, kilo):
        print(kilo, " yogurt üretildi")
        self.sut_litre -= kilo
        print(self.sut_litre)
        self.yogurt_kilo += kilo

    def dondurma_uret(self,kilo):
        print(kilo, " dondurma üretildi")
        self.sut_litre -= kilo
        print(self.sut_litre)
        self.dondurma_kilo += kilo

    def tereyagi_uret(self,kilo):
        print(kilo, " tereyagi üretildi")
        self.sut_litre -= kilo * 5
        print(self.sut_litre)
        self.tereyagi_kilo += kilo



class inek(hayvan):

    def __init__(self,adet):
        super().__init__(adet)

    def sut_sag(self):
        self.sut_litre += self.adet * 15
        print(self.adet * 15 , " litre süt sağıldı..")
        print("Toplam süt litresi : ", self.sut_litre)

    def yem_ver(self):
        print(self.adet*10," kilo yem verildi..")


class keci(hayvan):
    def __init__(self,adet):
        super().__init__(adet)

    def sut_sag(self):
        self.sut_litre += self.adet * 7
        print(self.adet * 7," litre süt sağıldı..")
        print("Toplam süt litresi : ",self.sut_litre)

    def yem_ver(self):
        print(self.adet*5," kilo yem verildi")


class koyun(hayvan):
    def __init__(self, adet):
        super().__init__(adet)

    def sut_sag(self):
        self.sut_litre += self.adet * 7
        print(self.adet * 7, " litre süt sağıldı..")
        print("Toplam süt litresi : ", self.sut_litre)

    def yem_ver(self):
        print(self.adet * 5, " kilo yem verildi")


class tavuk(hayvan):
    def __init__(self, adet):
        super().__init__(adet)
        self.yumurta = 0

    def yumurta_topla(self):
        self.yumurta = self.adet
        print(self.yumurta, " adet yumurta toplandı..")

    def yem_ver(self):
        print(self.adet /8 , " kilo yem verildi..")





inekk = inek(300)
koyun = koyun(150)
keci = keci(50)
tavuk = tavuk(189)

inekk.sut_sag()
inekk.sut_sag()
inekk.yem_ver()
inekk.su_ver()
inekk.meraya_sal()
inekk.peynir_uret(30)
print(inekk.peynir_kilo)