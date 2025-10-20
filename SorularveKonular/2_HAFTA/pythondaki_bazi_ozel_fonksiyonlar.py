# Format(): Metin türü (string) bir verinin istediğimiz formatta olmasını sağlar
# Örnek:
isim = "Ali"
yas = 25
print("Merhaba, benim adım {} ve {} yaşındayım.".format(isim, yas))
# Çıktı: Merhaba, benim adım Ali ve 25 yaşındayım.

print("\n---\n")

# Type(): Bir değişkenin veya ifadenin türünü gösterir
# Örnek:
x = 10
y = "Merhaba"
z = 3.14
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

print("\n---\n")

# Len(): Bir string veya list gibi veri türlerinin uzunluğunu (eleman sayısını/karakter sayısını) verir
# Örnek:
metin = "Python"
liste = [1, 2, 3, 4, 5]
print(len(metin))  # 6 (Python kelimesi 6 karakter)
print(len(liste))  # 5 (listenin 5 elemanı var)


"""
                        !!!  TIP DONUSUM FONKSIYONLARI !!!
                          
   Fonksiyon                                 İşlevi                                                                                     
| ------------- | ------------------------------------------------------------------------------------------ |
| **str()**     | Sayı değerli bir karakter dizisini veya tamsayıyı kayar noktalı sayıya (float) çevirir.    |
| **int()**     | Sayı değerli bir karakter dizisini veya kayan noktalı sayıyı tamsayıya (integer) çevirir.  |
| **bool()**    | Herhangi bir ifadeyi mantıksal veri türüne (bool) çevirir.                                 |
| **float()**   | Bir tamsayı veya kayan noktalı sayıyı karakter dizisine (string) çevirir.                  |
| **complex()** | Herhangi bir sayıyı veya sayı değerli karakter dizisini karmaşık sayıya (complex) çevirir. |
| **ord()**     | Verilen bir karakteri, sayısal olarak ASCII değerine dönüştürür.                           |
| **chr()**     | ASCII değeri sayısal olarak verilen bir değeri karaktere dönüştürür.                       |
  
 """