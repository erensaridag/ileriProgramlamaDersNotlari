class Kitap():
    def __init__(self,kitapAdi,kitapYazari,sayfSayisi):
        self.kitapAdi = kitapAdi
        self.kitapYazari = kitapYazari
        self.sayfSayisi = sayfSayisi

    def ozet(self):
        print("kitap adı:",self.kitapAdi)
        print("kitap yazari:",self.kitapYazari)
      #  print("kitap sayfa sayisi:",self.sayfSayisi)

kitap1 = Kitap("Yaban","Yakub Kadri",231)
kitap1.ozet()

print("**********************************************")

class Kargo ():
    def __init__(self,gonderen,alici,takip_no):
        self.gonderen = gonderen
        self.alici = alici
        self.takip_no = takip_no

class HizliKargo(Kargo):
    def __init__(self,gonderen,alici,takip_no,sure):
        self.gonderen = gonderen
        self.alici = alici
        self.takip_no = takip_no
        self.sure = sure

        print("gonderen=", self.gonderen)
        print("alıcı=", self.alici)
        print("takip no=", self.takip_no)
        print("sure=", self.sure)

deger3 = HizliKargo("Eren","Kian","TR448102",6)

print("**********************************************")
"""
class Okul():
def __init__(self,okulno,okuladi):
self.okulno=okulno
self.okuladi=okuladi
deger2=Okul(123,"Gümüşpala İÖO")
"""
#yazdirma islemi yapan hali Okul2() olan asagidaki yani
class Okul2():
    def __init__(self,okulno,okuladi):
        self.okulno = okulno
        self.okuladi = okuladi
    def ozet2(self):
        print(self.okulno)
        print(self.okuladi)

deger2 = Okul2(448,"Bugdayli IOO")
deger2.ozet2()