from Sayfa1 import Hayvan,satış


class inek(Hayvan, satış):

    def __init__(self):
        super().__init__()
        self.stok = {"inek sütü": 0, "inek kaymağı": 0, "inek peyniri": 0, "inek tereyağı": 0, "inek dondurması": 0,
                     "inek yoğurdu": 0, }

    def kaymak_uret(self, kilo):
        if (self.stok["inek sütü"] >= kilo):
            self.kaymak_kilo += kilo
            self.stok["inek kaymağı"] += self.kaymak_kilo
            return 1

        else:
            return 0

    def peynir_uret(self, kilo):
        if (self.stok["inek sütü"] >= kilo * 10):
            self.stok["inek sütü"] -= kilo * 10
            self.stok["inek peyniri"] += kilo
            return 1
        else:
            return 0

    def yogurt_uret(self, kilo):
        if (self.stok["inek sütü"] >= kilo):
            self.stok["inek sütü"] -= kilo
            self.yogurt_kilo += kilo
            self.stok["inek yoğurdu"] += self.yogurt_kilo
            return 1

        else:
            return 0

    def dondurma_uret(self, kilo):
        if (self.stok["inek sütü"] >= kilo):
            self.stok["inek sütü"] -= kilo
            self.dondurma_kilo += kilo
            self.stok["inek dondurması"] += self.dondurma_kilo
            return 1

        else:
            return 0

    def tereyagi_uret(self, kilo):
        if (self.stok["inek sütü"] >= kilo * 5):
            self.stok["inek sütü"] -= kilo * 5
            self.tereyagi_kilo += kilo
            self.stok["inek tereyağı"] += self.tereyagi_kilo
            return 1

        else:
            return 0


class keci(Hayvan, satış):
    def __init__(self):
        super().__init__()
        self.stok = {"keci sütü": 0, "keci yoğurdu": 0, "keci peyniri": 0, "keci dondurması": 0}

    def peynir_uret(self, kilo):
        if (self.stok["keci sütü"] >= kilo * 10):

            self.stok["keci sütü"] -= kilo * 10

            self.peynir_kilo += kilo
            self.stok["keci peyniri"] = self.peynir_kilo
            return 1

        else:
            return 0

    def yogurt_uret(self, kilo):
        if (self.stok["keci sütü"] >= kilo):

            self.stok["keci sütü"] -= kilo

            self.yogurt_kilo += kilo
            self.stok["keci yoğurdu"] = self.yogurt_kilo
            return 1

        else:
            return 0

    def dondurma_uret(self, kilo):
        if (self.stok["keci sütü"] >= kilo):
            self.stok["keci sütü"] -= kilo

            self.dondurma_kilo += kilo
            self.stok["keci dondurması"] = self.dondurma_kilo
            return 1

        else:
            return 0


class koyun(Hayvan, satış):
    def __init__(self):
        super().__init__()
        self.stok = {"koyun sütü": 0, "koyun peyniri": 0, "koyun yoğurdu": 0}

    def peynir_uret(self, kilo):
        if (self.stok["koyun sütü"] >= kilo * 10):

            self.stok["koyun sütü"] -= kilo * 10

            self.peynir_kilo += kilo
            self.stok["koyun peyniri"] = self.peynir_kilo
            return 1

        else:
            return 0

    def yogurt_uret(self, kilo):
        if (self.stok["koyun sütü"] >= kilo):

            self.stok["koyun sütü"] -= kilo

            self.yogurt_kilo += kilo
            self.stok["koyun yoğurdu"] = self.yogurt_kilo
            return 1

        else:
            return 0


class tavuk(Hayvan, satış):
    def __init__(self):
        super().__init__()
        self.stok = {"yumurta": 0}



inek = inek()
koyun = koyun()
keci = keci()
tavuk = tavuk()

