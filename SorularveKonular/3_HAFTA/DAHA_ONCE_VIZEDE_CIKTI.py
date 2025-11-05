# Soru:
# Rastgele olarak 100-200 tam sayı değerleri arasında oluşturulan
# 100 elemanlı bir dizinin elemanlarının 3’e bölünen eleman sayısının
# kaç tane olduğunu bulan programı yazınız.

import random  # random modülü rastgele sayı üretmek için kullanılır

dizi = []
sayi = 0  # 3'e bölünen sayıların adedi

for i in range(100):
    # random.randint(100, 200) → 100 ile 200 arasında rastgele tam sayı üretir
    x = random.randint(100, 200)
    dizi.append(x)   # list.append() → listeye eleman ekler
    # % (mod) operatörü → bölümden kalan bulur , kalan 0 ise 3’e tam bölünüyor demektir
    if x % 3 == 0:
        sayi += 1  # sayıyı 1 arttır
print("Dizi:", dizi)
print("3'e bölünen sayı adedi:", sayi)
