# OOP - NESNE YONELIMLI PROGRAMLAMA

#  KAVRAMLAR : pass komutu onemli bu dilde   , __init__  buda onemli , ***self komutu da onemli
# kurucu fonnkison yazilmasi onemli
#sira sizde yerindeki sorular onceden sinavda cikmis tekrar etmek onemli
# kalitim konusunda ornekler yazan kisimdaki resim cikabilir oncdeden cikmis
# veri onu isleme haftaya
class Araba:
    def __init__(self):
        self.adi="Araba"
        self.turu = "Araba"
        self.km = "Araba"

    def arabaGidiyor(self):
        print(self.adi,"Araba gidio....")
    def arabaDurdur(self):
        print(self.adi,"Araba durdu....")
    def arabaKM(self):
            print(self.adi, "Araba km cok yuksek....",araba1.km)

araba1 = Araba()
araba1.adi="Fiat Linea"
araba1.km=500000
araba1.arabaGidiyor()
araba1.arabaDurdur()
araba1.arabaKM()
print("---------------------------------------------------")


class MeyveSepeti():
    def __init__(self):
        self.icindekiler = []

    def meyve_ekle(self, adi):
        self.icindekiler.append(adi)

    def meyveleri_goruntule(self):
        for x in self.icindekiler:
            print(x)

sariSepet = MeyveSepeti()
sariSepet.meyve_ekle("elma")
sariSepet.meyve_ekle("armut")
sariSepet.meyveleri_goruntule()

print("---------------------------------------------------")

class Diyet():
 def __init__(self,diyetAdi,diyetTuru,diyetTarifi):
     self.diyetAdi = diyetAdi
     self.diyetTuru = diyetTuru
     self.diyetTarifi = diyetTarifi

diyet = Diyet("Kilo verme","saglikli beslenme","salata")
print(diyet.diyetAdi)
print(diyet.diyetTuru)
print(diyet.diyetTarifi)

print("---------------------------------------------------")
