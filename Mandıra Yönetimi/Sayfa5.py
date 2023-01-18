from tkinter import *

from Sayfa2 import inek,koyun,keci,tavuk
from Sayfa4 import calisan_tavuk,calisan_inek,calisan_keci,calisan_koyun
from Sayfa3 import dosya



inek_gorevlisi = calisan_inek()
inek_gorevlisi.set_Calisan_ad("Barış")
inek_gorevlisi.set_Calisan_soyad("Çaylı")
inek_gorevlisi.set_Calisan_id(123)
inek_gorevlisi.set_Calisan_alan("inek")
inek_gorevlisi.set_Calisan()

koyun_gorevlisi = calisan_koyun()
koyun_gorevlisi.set_Calisan_ad("Sadık")
koyun_gorevlisi.set_Calisan_soyad("Atilla")
koyun_gorevlisi.set_Calisan_id(321)
koyun_gorevlisi.set_Calisan_alan("koyun")
koyun_gorevlisi.set_Calisan()

keci_gorevlisi = calisan_keci()
keci_gorevlisi.set_Calisan_ad("Ali")
keci_gorevlisi.set_Calisan_soyad("Biçim")
keci_gorevlisi.set_Calisan_id(789)
keci_gorevlisi.set_Calisan_alan("keci")
keci_gorevlisi.set_Calisan()

tavuk_gorevlisi = calisan_tavuk()
tavuk_gorevlisi.set_Calisan_ad("Mesutcan")
tavuk_gorevlisi.set_Calisan_soyad("Tomay")
tavuk_gorevlisi.set_Calisan_id(987)
tavuk_gorevlisi.set_Calisan_alan("tavuk")
tavuk_gorevlisi.set_Calisan()


w = dosya()








master = Tk()

# İŞLEMLERİN FONKSİYONLARI
def hayvan_ekle():
    frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

    sayi_yazisi = Label(frame_sag, bg="#add8e6", text="kaç hayvan ekleyeceksiniz: ")
    sayi_yazisi.pack(padx=2, pady=2)

    def sonuclandirma():

        if x.get() == 1:
            inek.hayvan_ekle(int(eklenecek_sayi.get()))
            frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
            frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)
            sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="HAYVAN EKLEMESİ TAMAMLANDI")
            sonuclandirma_ekrani.pack(pady=50)

            yeniden_eklemek = Button(frame_sag, text="YENİDEN EKLEMEK İÇİN BASINIZ", command=hayvan_ekle)
            yeniden_eklemek.pack()

        elif x.get() == 2:
            koyun.hayvan_ekle(int(eklenecek_sayi.get()))
            frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
            frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)
            sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="HAYVAN EKLEMESİ TAMAMLANDI")
            sonuclandirma_ekrani.pack(pady=50)

            yeniden_eklemek = Button(frame_sag, text="YENİDEN EKLEMEK İÇİN BASINIZ", command=hayvan_ekle)
            yeniden_eklemek.pack()

        elif x.get() == 3:
            keci.hayvan_ekle(int(eklenecek_sayi.get()))
            frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
            frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)
            sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="HAYVAN EKLEMESİ TAMAMLANDI")
            sonuclandirma_ekrani.pack(pady=50)

            yeniden_eklemek = Button(frame_sag, text="YENİDEN EKLEMEK İÇİN BASINIZ", command=hayvan_ekle)
            yeniden_eklemek.pack()
        elif x.get() == 4:
            tavuk.hayvan_ekle(int(eklenecek_sayi.get()))
            frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
            frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)
            sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="HAYVAN EKLEMESİ TAMAMLANDI")
            sonuclandirma_ekrani.pack(pady=50)

            yeniden_eklemek = Button(frame_sag, text="YENİDEN EKLEMEK İÇİN BASINIZ", command=hayvan_ekle)
            yeniden_eklemek.pack()

    x = IntVar()
    eklenecek_sayi = Spinbox(frame_sag, from_=1, to=999999999999999)
    eklenecek_sayi.pack()

    ekleme_butonu_yazi = Label(frame_sag, bg="#add8e6", text="EKLEMEK İSTEDİĞİNİZ HAYVANI SEÇİNİZ ")
    ekleme_butonu_yazi.pack(padx=2, pady=2)

    inek_ekleme_butonu = Radiobutton(frame_sag, text="inek", variable=x, value=1)
    inek_ekleme_butonu.pack(pady=5)

    koyun_ekleme_butonu = Radiobutton(frame_sag, text="koyun", variable=x, value=2)
    koyun_ekleme_butonu.pack(pady=5)

    keçi_ekleme_butonu = Radiobutton(frame_sag, text="keçi", variable=x, value=3)
    keçi_ekleme_butonu.pack(pady=5)

    tavuk_ekleme_butonu = Radiobutton(frame_sag, text="tavuk", variable=x, value=4)

    tavuk_ekleme_butonu.pack(pady=5)

    tamamlama_button = Button(frame_sag, text="tamam", command=sonuclandirma)
    tamamlama_button.pack()


def hayvan_sil():
    def silme_tamamlandı():

        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="HAYVAN SİLMESİ TAMAMLANDI")
        sonuclandirma_ekrani.pack(pady=50)

        yeniden_eklemek = Button(frame_sag, text="YENİDEN SİLMEK İÇİN BASINIZ", command=hayvan_sil)
        yeniden_eklemek.pack()

    def silme_tamamlanamadı():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="HAYVAN SİLMESİ TAMAMLANAMADI")
        sonuclandirma_ekrani.pack(pady=5)

        sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="BU KADAR HAYVANIMIZ YOK MALESEF")
        sonuclandirma_ekrani.pack(pady=50)

        yeniden_eklemek = Button(frame_sag, text="YENİDEN SİLMEK İÇİN BASINIZ", command=hayvan_sil)
        yeniden_eklemek.pack()

    def sonuclandirma():
        if x.get() == 1:
            if inek.hayvan_sil(int(silinecek_sayi.get())) == 1:

                silme_tamamlandı()
            else:
                silme_tamamlanamadı()
        elif x.get() == 2:
            if koyun.hayvan_sil(int(silinecek_sayi.get())) == 1:

                silme_tamamlandı()
            else:
                silme_tamamlanamadı()
        elif x.get() == 3:
            if keci.hayvan_sil(int(silinecek_sayi.get())) == 1:

                silme_tamamlandı()
            else:
                silme_tamamlanamadı()
        elif x.get() == 4:
            if tavuk.hayvan_sil(int(silinecek_sayi.get())) == 1:
                silme_tamamlandı()
            else:
                silme_tamamlanamadı()

    x = IntVar()
    frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)
    hayvan_silme_yazi = Label(frame_sag, bg="#add8e6", text="SİLMEK SİTEDİĞİNİZ HAYVANI SEÇİNİZ")
    hayvan_silme_yazi.pack(pady=5)

    silinecek_sayi = Spinbox(frame_sag, from_=1, to=999999999999999)
    silinecek_sayi.pack()

    silme_butonu_yazi = Label(frame_sag, bg="#add8e6", text="EKLEMEK İSTEDİĞİNİZ HAYVANI SEÇİNİZ ")
    silme_butonu_yazi.pack(padx=2, pady=2)

    inek_silme_butonu = Radiobutton(frame_sag, text="inek", variable=x, value=1)
    inek_silme_butonu.pack(pady=5)

    koyun_silme_butonu = Radiobutton(frame_sag, text="koyun", variable=x, value=2)
    koyun_silme_butonu.pack(pady=5)

    keçi_silme_butonu = Radiobutton(frame_sag, text="keçi", variable=x, value=3)
    keçi_silme_butonu.pack(pady=5)

    tavuk_silme_butonu = Radiobutton(frame_sag, text="tavuk", variable=x, value=4)

    tavuk_silme_butonu.pack(pady=5)

    tamamlama_button = Button(frame_sag, text="tamam", command=sonuclandirma)
    tamamlama_button.pack()


def urun_ekle():
    def urun_ekleme_kismi():
        def sonuc_ekrani_urun_ekle():
            frame_sag = Frame(master, bg="#add8e6")
            frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)
            sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="ÜRETİM TAMAMLANDI")
            sonuclandirma_ekrani.pack(pady=50)

            yeniden_eklemek = Button(frame_sag, text="YENİDEN ÜRETMEK İÇİN BASINIZ", command=urun_ekle)
            yeniden_eklemek.pack()

        def sonuc_ekrani_eklenemedi():
            frame_sag = Frame(master, bg="#add8e6")
            frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)
            sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="ÜRETİM TAMAMLANAMADI")
            sonuclandirma_ekrani.pack(pady=5)

            sonuclandirma_ekrani = Label(frame_sag, bg="#add8e6", text="YETERLİ SÜTÜMÜZ YOK MALESEF")
            sonuclandirma_ekrani.pack(pady=5)

            yeniden_eklemek = Button(frame_sag, text="YENİDEN ÜRETMEK İÇİN BASINIZ", command=urun_ekle)
            yeniden_eklemek.pack(pady=50)

        if x.get() == 1:
            if y.get() == 1:
                if inek.tereyagi_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()
                else:
                    sonuc_ekrani_eklenemedi()
            elif y.get() == 2:
                if inek.peynir_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()
                else:
                    sonuc_ekrani_eklenemedi()
            elif y.get() == 3:
                if inek.yogurt_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()
                else:
                    sonuc_ekrani_eklenemedi()

            elif y.get() == 4:
                if inek.kaymak_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()

                else:
                    sonuc_ekrani_eklenemedi()
            elif y.get() == 5:
                if inek.dondurma_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()
                else:
                    sonuc_ekrani_eklenemedi()

        elif x.get() == 2:

            if y.get() == 2:
                if koyun.peynir_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()
                else:
                    sonuc_ekrani_eklenemedi()
            elif y.get() == 3:
                if koyun.yogurt_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()
                else:
                    sonuc_ekrani_eklenemedi()


        elif x.get() == 3:
            if y.get() == 2:
                if keci.peynir_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()
                else:
                    sonuc_ekrani_eklenemedi()
            elif y.get() == 3:
                if keci.yogurt_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()
                else:
                    sonuc_ekrani_eklenemedi()

            elif y.get() == 5:
                if keci.dondurma_uret(int(uretim_miktari.get())) == 1:

                    sonuc_ekrani_urun_ekle()
                else:
                    sonuc_ekrani_eklenemedi()

    ()

    frame_soll = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_soll.place(relx=0.37, rely=0.23, relwidth=0.26, relheight=0.4)

    frame_bosluk = Frame(master, bg="#000000")
    frame_bosluk.place(relx=0.63, rely=0.23, relwidth=0.01, relheight=0.4)

    frame_sagg = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_sagg.place(relx=0.64, rely=0.23, relwidth=0.26, relheight=0.4)

    frame_alt = Frame(master, bg="#add8e6")
    frame_alt.place(relx=0.37, rely=0.64, relwidth=0.53, relheight=0.19)

    frame_cizgi = Frame(master, bg="#000000")
    frame_cizgi.place(relx=0.37, rely=0.63, relwidth=0.53, relheight=0.02)

    x = IntVar()
    y = IntVar()

    hayvan_sec = Label(frame_soll, text="HAYVAN SEÇİNİZ", bg="#add8e6")
    hayvan_sec.pack()

    inek_secme = Radiobutton(frame_soll, text="inek   ", variable=x, value=1, bg="#add8e6")
    inek_secme.pack(pady=13)
    koyun_secme = Radiobutton(frame_soll, text="Koyun", variable=x, value=2, bg="#add8e6")
    koyun_secme.pack(pady=13)
    keci_secme = Radiobutton(frame_soll, text="keci   ", variable=x, value=3, bg="#add8e6")
    keci_secme.pack(pady=13)

    urun_sec = Label(frame_sagg, text="ÜRÜN SEÇİNİZ ", bg="#add8e6")
    urun_sec.pack()

    sut_secenegi = Radiobutton(frame_sagg, text="tereyagi", bg="#add8e6", variable=y, value=1)
    sut_secenegi.pack(pady=4)

    peynir_secenegi = Radiobutton(frame_sagg, text="peynir        ", bg="#add8e6", variable=y, value=2)
    peynir_secenegi.pack(pady=4)

    yogurt_secenegi = Radiobutton(frame_sagg, text="yoğurt       ", bg="#add8e6", variable=y, value=3)
    yogurt_secenegi.pack(pady=4)

    kaymak_secenegi = Radiobutton(frame_sagg, text="kaymak     ", bg="#add8e6", variable=y, value=4)
    kaymak_secenegi.pack(pady=4)

    dondurma_secenegi = Radiobutton(frame_sagg, text="dondurma", bg="#add8e6", variable=y, value=5)
    dondurma_secenegi.pack(pady=4)

    tereyagi_secenegi = Radiobutton(frame_sagg, text="tereyağı", bg="#add8e6", variable=y, value=6)
    tereyagi_secenegi.pack(pady=4)

    miktar_yazi = Label(frame_alt, text="ÜRETİM MİKTARI GİRİNİZ ", bg="#add8e6")
    miktar_yazi.pack(pady=5)

    uretim_miktari = Spinbox(frame_alt, from_=1, to=999999999999999)
    uretim_miktari.pack()

    uret_butonu = Button(frame_alt, text="ÜRET", command=urun_ekleme_kismi)
    uret_butonu.pack(pady=5)


def urun_sat():
    def satim_alani():

        def satim_sonu_ekrani():
            frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
            frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

            satim_sonu_yazi = Label(frame_sag, text="SATIM TAMAMLANDI")
            satim_sonu_yazi.pack(pady=50)

            tekrar_satim_butonu = Button(frame_sag, text="TEKRAR SATIŞ YAPMAK İÇİN TIKLAYINIZ", command=urun_sat)
            tekrar_satim_butonu.pack(pady=5)

        def basarisiz_satis():
            frame_sag = Frame(master, bg="#add8e6")
            frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

            satim_sonu_yazi = Label(frame_sag, text="SATIM TAMAMLANAMADI")
            satim_sonu_yazi.pack(pady=5)

            satim_sonu_yazi = Label(frame_sag, text="YETERİ ÜRÜNÜNÜZ YOK")
            satim_sonu_yazi.pack()

            tekrar_satim_butonu = Button(frame_sag, text="TEKRAR SATIŞ YAPMAK İÇİN TIKLAYINIZ", command=urun_sat)
            tekrar_satim_butonu.pack(pady=50)

        if t.get() == 4:
            if r.get == 1:

                if tavuk.satış_yap("yumurta", str(satilan_miktar.get())) == 1:

                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()


        elif t.get() == 1:
            if r.get() == 2:
                if inek.satış_yap("inek sütü", str(satilan_miktar.get())) == 1:

                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()
            elif r.get() == 3:
                if inek.satış_yap("inek peyniri", str(satilan_miktar.get())) == 1:


                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()

            elif r.get() == 4:
                if inek.satış_yap("inek yoğurdu", str(satilan_miktar.get())) == 1:
                   satim_sonu_ekrani()
                else:
                    basarisiz_satis()
            elif r.get() == 5:
                if inek.satış_yap("inek kaymağı", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()
            elif r.get() == 6:
                if inek.satış_yap("inek dondurması", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()
            elif r.get() == 7:
                if inek.satış_yap("inek tereyağı", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()

        elif t.get() == 3:
            if r.get() == 2:
                if keci.satış_yap("keci sütü", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()
            elif r.get() == 3:
                if keci.satış_yap("keci peyniri", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()

            elif r.get() == 4:
                if keci.satış_yap("keci yoğurdu", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()
            elif r.get() == 6:
                if keci.satış_yap("keci dondurması", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()
        elif t.get() == 2:
            if r.get() == 2:
                if koyun.satış_yap("koyun sütü", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()

            elif r.get() == 3:
                if koyun.satış_yap("koyun peyniri", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()
            elif r.get() == 4:
                if koyun.satış_yap("koyun yoğurdu", str(satilan_miktar.get())) == 1:
                    satim_sonu_ekrani()
                else:
                    basarisiz_satis()

    frame_soll = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_soll.place(relx=0.37, rely=0.23, relwidth=0.26, relheight=0.43)

    frame_sagg = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_sagg.place(relx=0.64, rely=0.23, relwidth=0.26, relheight=0.43)

    frame_alt = Frame(master, bg="#add8e6")
    frame_alt.place(relx=0.37, rely=0.67, relwidth=0.53, relheight=0.16)

    frame_cizgi = Frame(master, bg="#000000")
    frame_cizgi.place(relx=0.37, rely=0.66, relwidth=0.53, relheight=0.02)

    frame_bosluk = Frame(master, bg="#000000")
    frame_bosluk.place(relx=0.63, rely=0.23, relwidth=0.01, relheight=0.45)

    satilacak_urun_yazi = Label(frame_soll, text="HAYVAN SEÇİNİZ", bg="#add8e6")
    satilacak_urun_yazi.pack()

    t = IntVar()
    r = IntVar()

    inek_satilacak_urun = Radiobutton(frame_soll, text="inek    ", bg="#add8e6", variable=t, value=1)
    inek_satilacak_urun.pack(pady=6)

    koyun_satilacak_urun = Radiobutton(frame_soll, text="koyun", bg="#add8e6", variable=t, value=2)
    koyun_satilacak_urun.pack(pady=6)

    keci_satilacak_urun = Radiobutton(frame_soll, text="keci   ", bg="#add8e6", variable=t, value=3)
    keci_satilacak_urun.pack(pady=6)

    tavuk_satilacak_urun = Radiobutton(frame_soll, text="tavuk", bg="#add8e6", variable=t, value=4)
    tavuk_satilacak_urun.pack(pady=6)

    urun_secimi_yazisi = Label(frame_sagg, bg="#add8e6", text="ÜRÜN SEÇİNİZ")
    urun_secimi_yazisi.pack()

    yumurta_satimi = Radiobutton(frame_sagg, bg="#add8e6", text="yumurta", variable=r, value=1)
    yumurta_satimi.pack()

    sut_satimi = Radiobutton(frame_sagg, bg="#add8e6", text="süt         ", variable=r, value=2)
    sut_satimi.pack()

    peynir_satimi = Radiobutton(frame_sagg, bg="#add8e6", text="peynir", variable=r, value=3)
    peynir_satimi.pack()

    yogurt_satimi = Radiobutton(frame_sagg, bg="#add8e6", text="yoğurt", variable=r, value=4)
    yogurt_satimi.pack()

    kaymak_satimi = Radiobutton(frame_sagg, bg="#add8e6", text="kaymak", variable=r, value=5)
    kaymak_satimi.pack()

    dondurma_satimi = Radiobutton(frame_sagg, bg="#add8e6", text="dondurma", variable=r, value=6)
    dondurma_satimi.pack()

    tereyagi_satimi = Radiobutton(frame_sagg, bg="#add8e6", text="tereyağı", variable=r, value=7)
    tereyagi_satimi.pack()

    satilan_miktar = Spinbox(frame_alt, from_=1, to=99999999)
    satilan_miktar.pack(pady=10)

    sat_butonu = Button(frame_alt, text="SAT", command=satim_alani)
    sat_butonu.pack(pady=5)


def calisan_isleri():
    frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

    def calisanlari_goruntuleme():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        lines = []
        with open('calisanlar.txt', 'r') as f:
            for i, line in enumerate(f):
                lines.append(line)
        with open('calisanlar.txt', 'w') as f:
            f.writelines(lines)

        for i in lines:
            yazdir = Label(frame_sag, text=i)
            yazdir.pack(pady=0)

    def calisan_ekle():

        def ekleme_alani():
            if x.get() == 1:
                inek_gorevlisi.set_Calisan_ad(isim.get())
                inek_gorevlisi.set_Calisan_soyad(soyisim.get())
                inek_gorevlisi.set_Calisan_id(id_giris.get())
                inek_gorevlisi.set_Calisan_alan("inek")
                inek_gorevlisi.set_Calisan()
            elif x.get() == 2:
                koyun_gorevlisi.set_Calisan_ad(isim.get())
                koyun_gorevlisi.set_Calisan_soyad(soyisim.get())
                koyun_gorevlisi.set_Calisan_id(id_giris.get())
                koyun_gorevlisi.set_Calisan_alan("koyun")
                koyun_gorevlisi.set_Calisan()
            elif x.get() == 3:
                keci_gorevlisi.set_Calisan_ad(isim.get())
                keci_gorevlisi.set_Calisan_soyad(soyisim.get())
                keci_gorevlisi.set_Calisan_id(id_giris.get())
                keci_gorevlisi.set_Calisan_alan("keci")
                keci_gorevlisi.set_Calisan()
            elif x.get() == 4:
                tavuk_gorevlisi.set_Calisan_ad(isim.get())
                tavuk_gorevlisi.set_Calisan_soyad(soyisim.get())
                tavuk_gorevlisi.set_Calisan_id(id_giris.get())
                tavuk_gorevlisi.set_Calisan_alan("tavuk")
                tavuk_gorevlisi.set_Calisan()

            frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
            frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

            sonuc = Label(frame_sag, bg="#add8e6", text="EKLEME TAMAMLANDI")
            sonuc.pack()

            geri_don = Button(frame_sag, text="çalışan işleri", command=calisan_isleri)
            geri_don.pack()

        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        id_yazisi = Label(frame_sag, text="3 haneli id giriniz", bg="#add8e6")
        id_yazisi.pack()

        id_giris = Entry(frame_sag)
        id_giris.pack()

        ad_yazisi = Label(frame_sag, text="ad giriniz", bg="#add8e6")
        ad_yazisi.pack()

        isim = Entry(frame_sag)
        isim.pack(pady=0)

        soyad_yazisi = Label(frame_sag, text="soyad giriniz", bg="#add8e6")
        soyad_yazisi.pack()

        soyisim = Entry(frame_sag)
        soyisim.pack(pady=0)

        alan_yazisi = Label(frame_sag, text="alan seçiniz", bg="#add8e6")
        alan_yazisi.pack()

        x = IntVar()
        inek_alani = Radiobutton(frame_sag, text="inek", variable=x, value=1)
        inek_alani.pack(pady=1)

        koyun_alani = Radiobutton(frame_sag, text="koyun", variable=x, value=2)
        koyun_alani.pack(pady=1)

        keci_alani = Radiobutton(frame_sag, text="keçi", variable=x, value=3)
        keci_alani.pack(pady=1)

        tavuk_alani = Radiobutton(frame_sag, text="tavuk", variable=x, value=4)
        tavuk_alani.pack(pady=1)

        ekleme_butonu = Button(frame_sag, text="ekle", command=ekleme_alani)
        ekleme_butonu.pack()

    def calisan_silme():

        def calisan_silme_islemi():
            if w.calisan_sil(int(silinecek_id.get())) == 1:
                frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
                frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

                silme_tamamlandi=Label(frame_sag,text="SİLME TAMAMLANDI")
                silme_tamamlandi.pack(pady=10)

                yeni_islem=Button(frame_sag,text="çalışan işleri",command=calisan_isleri())
                yeni_islem.pack(pady=10)
            elif w.calisan_sil(int(silinecek_id.get()))==0:
                frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
                frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

                silme_tamamlandi = Label(frame_sag, text="SİLME TAMAMLANAMADI")
                silme_tamamlandi.pack(pady=10)

                yeni_islem = Button(frame_sag, text="çalışan işleri", command=calisan_isleri())
                yeni_islem.pack(pady=10)



        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        id_yazisi = Label(frame_sag, text="silinecek id yi yazınız")
        id_yazisi.pack()

        silinecek_id = Entry(frame_sag)
        silinecek_id.pack()

        sil_butonu = Button(frame_sag, text="sil", command=calisan_silme_islemi)
        sil_butonu.pack()

    calisanlari_goruntule = Button(frame_sag, text="çalışanları görüntüle", command=calisanlari_goruntuleme)
    calisanlari_goruntule.pack(pady=3)

    calisan_ekleme = Button(frame_sag, text="çalışan ekle", command=calisan_ekle)
    calisan_ekleme.pack(pady=3)

    calisan_silmes = Button(frame_sag, text="çalışan silme", command=calisan_silme)
    calisan_silmes.pack(pady=3)


def hayvan_sayisi():
    frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

    inek_yazi = Label(frame_sag, bg="#add8e6", text="inek sayisi")
    inek_yazi.pack()

    inek_sayisi_yazdir = Label(frame_sag, bg="#add8e6", text=inek.adet)
    inek_sayisi_yazdir.pack()

    koyun_yazi = Label(frame_sag, bg="#add8e6", text="koyun sayisi")
    koyun_yazi.pack()

    koyun_sayisi_yazdir = Label(frame_sag, bg="#add8e6", text=koyun.adet)
    koyun_sayisi_yazdir.pack()

    keci_yazi = Label(frame_sag, bg="#add8e6", text="keçi sayisi")
    keci_yazi.pack()

    keci_sayisi_yazdir = Label(frame_sag, bg="#add8e6", text=keci.adet)
    keci_sayisi_yazdir.pack()

    tavuk_yazi = Label(frame_sag, bg="#add8e6", text="tavuk sayisi")
    tavuk_yazi.pack()

    tavuk_sayisi_yazdir = Label(frame_sag, bg="#add8e6", text=tavuk.adet)
    tavuk_sayisi_yazdir.pack()


def stok_durumu():
    frame_orta2 = Frame(master, bg="#a8eced")  # SAĞ ALAN
    frame_orta2.place(relx=0.37, rely=0.23, relwidth=0.18, relheight=0.6)

    frame_orta1 = Frame(master, bg="#a9e4e6")  # SAĞ ALAN
    frame_orta1.place(relx=0.55, rely=0.23, relwidth=0.18, relheight=0.6)

    frame_orta3 = Frame(master, bg="#64d9dc")  # SAĞ ALAN
    frame_orta3.place(relx=0.72, rely=0.23, relwidth=0.18, relheight=0.6)

    frame_orta4 = Frame(master, bg="#8deeee")  # SAĞ ALAN
    frame_orta4.place(relx=0.72, rely=0.60, relwidth=0.18, relheight=0.23)

    tavuk_yazdir = Label(frame_orta4, bg="#8deeee", text="tavuk ürünleri")
    tavuk_yazdir.pack()

    yumurta_yazisi = Label(frame_orta4, bg="#8deeee", text="yumurta")
    yumurta_yazisi.pack()

    yumurta_sayisi = Label(frame_orta4, bg="#8deeee", text=tavuk.stok["yumurta"])
    yumurta_sayisi.pack()

    keci_yazdir = Label(frame_orta1, bg="#a9e4e6", text="keçi ürünleri")
    keci_yazdir.pack()

    keci_sütü = Label(frame_orta1, bg="#a9e4e6", text="süt miktarı")
    keci_sütü.pack()

    keci_sütü_miktari = Label(frame_orta1, bg="#a9e4e6", text=keci.stok["keci sütü"])
    keci_sütü_miktari.pack()

    keci_peynir = Label(frame_orta1, bg="#a9e4e6", text="peynir miktarı")
    keci_peynir.pack()

    keci_peynir_miktari = Label(frame_orta1, bg="#a9e4e6", text=keci.stok["keci peyniri"])
    keci_peynir_miktari.pack()

    keci_yogurt = Label(frame_orta1, bg="#a9e4e6", text="yogurt miktarı")
    keci_yogurt.pack()

    keci_yogurt_miktari = Label(frame_orta1, bg="#a9e4e6", text=keci.stok["keci yoğurdu"])
    keci_yogurt_miktari.pack()

    keci_dondurma = Label(frame_orta1, bg="#a9e4e6", text="dondurma miktarı")
    keci_dondurma.pack()

    keci_dondurma_miktari = Label(frame_orta1, bg="#a9e4e6", text=keci.stok["keci dondurması"])
    keci_dondurma_miktari.pack()

    # İNEK STOKLARI==========================================================================================================
    inek_yazdir = Label(frame_orta2, bg="#a8eced", text="inek ürünleri")
    inek_yazdir.pack()

    inek_sütü = Label(frame_orta2, bg="#a8eced", text="süt miktarı")
    inek_sütü.pack()

    inek_sütü_miktari = Label(frame_orta2, bg="#a8eced", text=inek.stok["inek sütü"])
    inek_sütü_miktari.pack()

    inek_peynir = Label(frame_orta2, bg="#a8eced", text="peynir miktarı")
    inek_peynir.pack()

    inek_peynir_miktari = Label(frame_orta2, bg="#a8eced", text=inek.stok["inek peyniri"])
    inek_peynir_miktari.pack()

    inek_yogurt = Label(frame_orta2, bg="#a8eced", text="yogurt miktarı")
    inek_yogurt.pack()

    inek_yogurt_miktarı = Label(frame_orta2, bg="#a8eced", text=inek.stok["inek yoğurdu"])
    inek_yogurt_miktarı.pack()

    inek_kaymak = Label(frame_orta2, bg="#a8eced", text="kaymak miktarı")
    inek_kaymak.pack()

    inek_kaymak_miktarı = Label(frame_orta2, bg="#a8eced", text=inek.stok["inek kaymağı"])
    inek_kaymak_miktarı.pack()

    inek_dondurma = Label(frame_orta2, bg="#a8eced", text="dondurma miktarı")
    inek_dondurma.pack()

    inek_dondurma_miktarı = Label(frame_orta2, bg="#a8eced", text=inek.stok["inek dondurması"])
    inek_dondurma_miktarı.pack()

    inek_tereyagi = Label(frame_orta2, bg="#a8eced", text="tereyağı miktarı")
    inek_tereyagi.pack()

    inek_tereyagı_miktarı = Label(frame_orta2, bg="#a8eced", text=inek.stok["inek tereyağı"])
    inek_tereyagı_miktarı.pack()

    # KOYUN STOKLARI==========================================================================================================
    koyun_yazdir = Label(frame_orta3, bg="#64d9dc", text="koyun ürünleri")
    koyun_yazdir.pack()

    koyun_sütü = Label(frame_orta3, bg="#64d9dc", text="süt miktarı")
    koyun_sütü.pack()

    koyun_sütü_miktari = Label(frame_orta3, bg="#64d9dc", text=koyun.stok["koyun sütü"])
    koyun_sütü_miktari.pack()

    koyun_peynir = Label(frame_orta3, bg="#64d9dc", text="peynir miktarı")
    koyun_peynir.pack()

    koyun_peynir_miktari = Label(frame_orta3, bg="#64d9dc", text=koyun.stok["koyun peyniri"])
    koyun_peynir_miktari.pack()

    koyun_yogurt = Label(frame_orta3, bg="#64d9dc", text="yogurt miktarı")
    koyun_yogurt.pack()

    koyun_yogurt_miktarı = Label(frame_orta3, bg="#64d9dc", text=koyun.stok["koyun yoğurdu"])
    koyun_yogurt_miktarı.pack()

    pass


def mandira_isleri():
    def ineklere_yem_ver():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        yem_miktari = Label(frame_sag, bg="#add8e6",
                            text="İNEKLERE {} KİLO YEM VERİLDİ".format(inek_gorevlisi.yem_ver()))
        yem_miktari.pack(pady=100)

    def koyunlara_yem_ver():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        yem_miktari = Label(frame_sag, bg="#add8e6",
                            text="KOYUNLARA {} KİLO YEM VERİLDİ".format(koyun_gorevlisi.yem_ver()))
        yem_miktari.pack(pady=100)

    def keci_yem_ver():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        yem_miktari = Label(frame_sag, bg="#add8e6",
                            text="KEÇİLERE {} KİLO YEM VERİLDİ".format(keci_gorevlisi.yem_ver()))
        yem_miktari.pack(pady=100)

    def tavuklara_yem_ver():
        frame_sag = Frame(master, bg="#add8e6")
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        yem_miktari = Label(frame_sag, bg="#add8e6",
                            text="TAVUKLARA {} KİLO YEM VERİLDİ".format(tavuk_gorevlisi.yem_ver()))
        yem_miktari.pack(pady=100)

    def inek_meraya_salınsın():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)


        salındı = Label(frame_sag, bg="#add8e6", text="HAYVANLAR {} METREKARE MERAYA SALINDI".format(inek_gorevlisi.meraya_sal(5,inek.adet)))
        salındı.pack(pady=100)

    def koyun_meraya_salınsın():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)


        salındı = Label(frame_sag, bg="#add8e6", text="KOYUNLAR {} METREKARE MERAYA SALINDI".format(koyun_gorevlisi.meraya_sal(3,koyun.adet)))
        salındı.pack(pady=100)

    def keci_meraya_salınsın():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)


        salındı = Label(frame_sag, bg="#add8e6", text="KEÇİLER {} METREKARE MERAYA SALINDI".format(keci_gorevlisi.meraya_sal(2,keci.adet)))
        salındı.pack(pady=100)



    def inek_sut():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        sonuc = Label(frame_sag, bg="#add8e6", text="{} LİTRE İNEK SÜTÜ SAĞILDI".format(inek_gorevlisi.inek_sag()))
        sonuc.pack(pady=100)

    def koyun_sut():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        sonuc = Label(frame_sag, bg="#add8e6", text="{} LİTRE KOYUN SÜTÜ SAĞILDI".format(koyun_gorevlisi.koyun_sag()))
        sonuc.pack(pady=100)

    def keci_sut():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        sonuc = Label(frame_sag, bg="#add8e6", text="{} LİTRE KEÇİ SÜTÜ SAĞILDI".format(keci_gorevlisi.keci_sag()))
        sonuc.pack(pady=100)

    def yumurta_topla():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        sonuc = Label(frame_sag, bg="#add8e6", text="{} TANE YUMURTA TOPLANDI".format(tavuk_gorevlisi.yumurta_topla()))
        sonuc.pack(pady=100)

    def su_ver():
        frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
        frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

        verildi = Label(frame_sag, text="HAYVANLARA SU VERİLDİ", bg="#add8e6")
        verildi.pack(pady=100)

    frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_sag.place(relx=0.37, rely=0.23, relwidth=0.27, relheight=0.6)

    frame_sag_sol = Frame(master, bg="#add8e6")  #
    frame_sag_sol.place(relx=0.64, rely=0.23, relwidth=0.26, relheight=0.6)

    inek_yem_verme_butonu = Button(frame_sag, text="ineklere yem ver", command=ineklere_yem_ver)
    inek_yem_verme_butonu.pack(pady=5)

    koyun_yem_verme_butonu = Button(frame_sag, text="koyunlara yem ver", command=koyunlara_yem_ver)
    koyun_yem_verme_butonu.pack(pady=5)

    keci_yem_verme_butonu = Button(frame_sag, text="keçilere yem ver", command=keci_yem_ver)
    keci_yem_verme_butonu.pack(pady=5)

    tavuk_yem_verme_butonu = Button(frame_sag, text="tavuklara yem ver", command=tavuklara_yem_ver)
    tavuk_yem_verme_butonu.pack(pady=5)

    meraya_salma_butonu = Button(frame_sag, text="inekleri meraya sal", command=inek_meraya_salınsın)
    meraya_salma_butonu.pack(pady=5)

    meraya_salma_butonu = Button(frame_sag, text="koyunları meraya sal", command=koyun_meraya_salınsın)
    meraya_salma_butonu.pack(pady=5)

    inek_sut_sag = Button(frame_sag_sol, text="ineklerin sütünü sağ", command=inek_sut)
    inek_sut_sag.pack(pady=5)


    koyun_sut_sag = Button(frame_sag_sol, text="koyunların sütünü sağ", command=koyun_sut)
    koyun_sut_sag.pack(pady=5)

    koyun_sut_sag = Button(frame_sag_sol, text="keçilerin sütünü sağ", command=keci_sut)
    koyun_sut_sag.pack(pady=5)

    yumurta_topla_butonu = Button(frame_sag_sol, text="tavukların yumurtalarını topla", command=yumurta_topla)
    yumurta_topla_butonu.pack(pady=5)

    su_verme_butonu = Button(frame_sag_sol, text="su ver", command=su_ver)
    su_verme_butonu.pack(pady=5)


    meraya_salma_butonu = Button(frame_sag_sol, text="keçileri meraya sal", command=keci_meraya_salınsın)
    meraya_salma_butonu.pack(pady=5)



# GENEL ARAYÜZ AYARLARI
def arayuz():
    canvas = Canvas(master, height=450, width=750)  # PENCERE BOYUTLAR
    canvas.pack()

    frame_ust = Frame(master, bg="#add8e6")  # ÜST ALAN
    frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.12)

    frame_sol = Frame(master, bg="#add8e6")  # SOL ALAN
    frame_sol.place(relx=0.1, rely=0.23, relwidth=0.263, relheight=0.6)

    frame_sag = Frame(master, bg="#add8e6")  # SAĞ ALAN
    frame_sag.place(relx=0.37, rely=0.23, relwidth=0.53, relheight=0.6)

    # ÜST TARAFIN YAZILARI
    ust_yazi = Label(frame_ust, bg="#add8e6", text="İNÖNÜ MANDIRA", font="Verdana  12 bold")
    ust_yazi.pack()

    sado_isim = Label(frame_ust, bg="#add8e6", text="SADO ATİLLA \n 02210201035 ")
    sado_isim.pack(side=RIGHT)

    baris_isim = Label(frame_ust, bg="#add8e6", text="BARIŞ ÇAYLI \n 02210201038  ")
    baris_isim.pack(side=LEFT)

    # İŞLEMLER
    islem_seciniz = Label(frame_sol, bg="#add8e6", text="LÜTFEN İŞLEM SEÇİNİZ")
    islem_seciniz.pack(pady=2.5)

    hayvan_ekleme_butonu = Button(frame_sol, text="hayvan ekleme", command=hayvan_ekle)
    hayvan_ekleme_butonu.pack(pady=2)

    hayvan_silme_butonu = Button(frame_sol, text="hayvan silme", command=hayvan_sil)
    hayvan_silme_butonu.pack(pady=2)

    urun_ekleme_butonu = Button(frame_sol, text="urun uret", command=urun_ekle)
    urun_ekleme_butonu.pack(pady=2)

    urun_silme_butonu = Button(frame_sol, text="urun satıldı", command=urun_sat)
    urun_silme_butonu.pack(pady=2)

    urun_fiyat_listesi_butonu = Button(frame_sol, text="çalışan işleri", command=calisan_isleri)
    urun_fiyat_listesi_butonu.pack(pady=2)

    hayvan_sayisi_butonu = Button(frame_sol, text="hayvan sayısını gör", command=hayvan_sayisi)
    hayvan_sayisi_butonu.pack(pady=2)

    stok_sayisi_butonu = Button(frame_sol, text="stok durumuna bak", command=stok_durumu)
    stok_sayisi_butonu.pack(pady=2)

    mandira_isleri_butonu = Button(frame_sol, text="mandıra işleri", command=mandira_isleri)
    mandira_isleri_butonu.pack()

    master.mainloop()



arayuz()