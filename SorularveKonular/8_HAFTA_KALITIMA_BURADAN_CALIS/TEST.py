class BosSinif():


 class Ogrencii():
    pass

class Araba():
   pass
a = Araba()

class Kisi():
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    def bilgi_yazdir(self):
        print(self.ad,self.soyad)


class Kitap():
    def __init__(self,kitapAdi,kitapYazari,sayfaSayisi):
        self.kitapAdi = kitapAdi
        self.kitapYazari = kitapYazari
        self.sayfaSayisi = sayfaSayisi
    def ozet(self):
        print(self.kitapAdi,self.kitapYazari)

class Personel():
    def __init__(self,ad,soyad,sicilNo):
        self.ad = ad
        self.soyad = soyad
        self.sicilNo = sicilNo

personel = Personel("Ali","METIN",123)


class Kullanici():
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
    def giris(self):
        print("Giris yapildi...")

class Ogrenci(Kullanici):
    pass

o = Ogrenci("Can", "Demir")

class Kullanici:
    def __init__(self, ad):
        self.ad = ad

    def bilgi(self):
        print("Kullanıcı")

class Ogrenci(Kullanici):
    def __init__(self, ad, no):
        super().__init__(ad)
        self.no = no

    def bilgi(self):
        print("Öğrenci")
class Kargo:
    def __init__(self, gonderen, alici):
        self.gonderen = gonderen
        self.alici = alici

class HizliKargo(Kargo):
    def __init__(self, gonderen, alici, sure):
        super().__init__(gonderen, alici)
        self.sure = sure
