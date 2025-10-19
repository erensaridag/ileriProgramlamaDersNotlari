"""
While döngülerinde belirttiğimiz bir koşul doğru olduğu sürece while bloğu içerisinde tanımladığımız kod satırlarını tekrarlatabiliriz.
While döngüsünün söz dizimi şöyledir:
while koşul:
   ifade(ler)

Burada, ifade (ler) tek bir açıklama veya bir ifade bloğu olabilir.
"""
#Örnek 1’den 5’e kadar olan sayıları ekrana yazdırma
i = 1
while i < 5:
    print(i)
    i += 1
print("-----------------------------------------------------")
"""
While döngüsünde Else ifadesini kullanma
  While döngüsü ile else kullanılırsa, koşul yanlış olduğunda, else ifadesi yürütülür.
"""
#Örnek, 5’den küçük olduğu sürece bir sayıyı yazdıran program
count = 0
while count < 5:
   print(count, " sayısı 5'ten küçük")
   count = count + 1
else:
   print(count, " sayısı 5'ten küçük değil.")
