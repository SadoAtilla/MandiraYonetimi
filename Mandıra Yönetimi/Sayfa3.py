class dosya:

    def __init__(self):
        pass

    def calisan_ekle(self, ad, soyad, id, alan):
        with open('calisanlar.txt', 'a+') as f:
            f.write(f'Personel ID : {id} ,')
            f.write(f'Ad : {ad} ,')
            f.write(f'Soyad : {soyad} ,')
            f.write(f'Alan : {alan} \n')

    def calisan_ara(self, input_id):
        satir_takip = 0
        with open('calisanlar.txt', 'r') as f:
            a = 0
            for line in f:
                if input_id == int(line[14:17]):
                    a = 1

                    return "{},{}".format(a, satir_takip)
                satir_takip += 1
            if a == 0:
                return "{},{}".format(a, satir_takip)

    def calisan_sil(self, input_id):
        sayi = 0
        eklenen = 0
        if dosya.calisan_ara(dosya, input_id)[0] == "0":
            pass
        else:
            lines = []

            with open('calisanlar.txt', 'r') as f:
                for i, line in enumerate(f):
                    sayi += 1
                    if i != int(dosya.calisan_ara(dosya, input_id)[2:]):
                        lines.append(line)
                        eklenen += 1
            with open('calisanlar.txt', 'w') as f:
                f.writelines(lines)

        if eklenen == sayi:
            return int(0)
        else:
            return int(1)

w=dosya()