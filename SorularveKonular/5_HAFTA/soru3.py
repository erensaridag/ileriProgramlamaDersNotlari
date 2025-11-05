import math

"""
Fonksiyona parametre olarak gelen x değerine göre aşağıdaki
işlemi gerçekleştiren programı yazınız? Fonksiyon değer
döndürmeyecek ve sonuc2 değeri ekrana yazdırılacaktır. 
Not: ilk değer 1’den başlayacaktır. Fonksiyonun çalışabilmesi
için gerekli ana fonksiyonu yazmayı ve varsa programın
çalışabilmesi için gerekli olan paket ve değişkenleri yazmayı
unutmayınız.
"""
def soru3(x):
 sayi=0
 for i in range(1,x+1):
  sayi=sayi+(i/math.sqrt(i*(i+1 )))
 print(sayi)
#ana fonksiyon
deger=int(input("değeri gir = "))
soru3(deger)
soru3(9)

