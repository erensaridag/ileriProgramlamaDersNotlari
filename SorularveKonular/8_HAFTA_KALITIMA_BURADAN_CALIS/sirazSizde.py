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