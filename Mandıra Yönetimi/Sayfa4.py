from abc import abstractmethod
from Sayfa1 import mera
from Sayfa2 import inek,koyun,keci,tavuk
from Sayfa3 import dosya

class calisanlar():
    def __init__(self):
        self.__ad = ""
        self.__soyad = ""
        self.__id = 0
        self.__alan = ""


    def set_Calisan_ad(self,ad):
        self.__ad = ad

    def set_Calisan_soyad(self,soyad):
        self.__soyad = soyad

    def set_Calisan_id(self,id):
        self.__id = int(id)

    def set_Calisan_alan(self,alan):
        self.__alan = alan

    def set_Calisan(self):
        w.calisan_ekle(self.__ad,self.__soyad,self.__id,self.__alan)

    @abstractmethod
    def yem_ver(self):
        pass

    def su_ver(self):
        print("Su veriliyor..")


class calisan_inek(calisanlar):

    def __init__(self):
        pass

    def inek_sag(self):
        inek.sut_litre += inek.adet * 15
        inek.stok["inek sütü"] = inek.sut_litre
        return int(inek.adet * 15)

    def yem_ver(self):
        return int(inek.adet * 10)

    def meraya_sal(self, mera_boyutu, adet):
         return mera.meraya_Sal(self, mera_boyutu, adet)


class calisan_koyun(calisanlar):

    def __init__(self):
        pass

    def koyun_sag(self):
        koyun.sut_litre += koyun.adet * 7
        koyun.stok["koyun sütü"] = koyun.sut_litre
        return int(koyun.adet * 7)

    def yem_ver(self):
        return int(koyun.adet * 5)

    def meraya_sal(self,mera_boyutu,adet):
        return mera.meraya_Sal(self,mera_boyutu,adet)


class calisan_keci(calisanlar):

    def __init__(self):
        pass

    def keci_sag(self):
        keci.sut_litre += keci.adet * 7
        keci.stok["keci sütü"] = keci.sut_litre
        return int(keci.adet * 7)


    def yem_ver(self):
        return int(keci.adet * 5)

    def meraya_sal(self, mera_boyutu, adet):
        return mera.meraya_Sal(self, mera_boyutu, adet)


class calisan_tavuk(calisanlar):

    def __init__(self):
        pass

    def yumurta_topla(self):
        tavuk.stok["yumurta"] += tavuk.adet
        return tavuk.adet

    def yem_ver(self):
        return int(tavuk.adet / 8)



w = dosya()