class Kullanici:
    def __init__(self,adi,soyadi,numarasi):
        self.adi = adi
        self.soyadi = soyadi
        self.numarasi = numarasi
    def giris(self):
        print("giris yapildi")
    def cikis(self):
        print("cikis yapildi")

class Akademisyen(Kullanici):
    def __init__(self,adi,soyadi,numarasi,dogum_tarihi):
        print("Akademisyen sınıfı fonksiyonu")
        self.adi= adi
        self.soyadi=soyadi
        self.numarasi= numarasi
        self.dogum_tarihi = dogum_tarihi
class Personel(Kullanici):
    pass
class Ogrenci(Kullanici):
    pass

akademisyen = Akademisyen("Mehmet","Demir",123,1987)
personel= Personel("Nazif","Bayrak",999)
ogrenci = Ogrenci("Kamil","Kaya",852)

print(akademisyen.adi)
print(akademisyen.soyadi)
print(akademisyen.numarasi)
print(akademisyen.dogum_tarihi)
