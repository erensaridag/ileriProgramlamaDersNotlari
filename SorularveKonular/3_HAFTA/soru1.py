# Örnek 1:
# 0-100 arasında rastgele atanmış 20 tam sayı için;
# - Listeyi yazdır
# - Toplamını bul
# - Aritmetik ortalamasını bul
# - En küçük ve en büyük sayıyı bul

import random  # Hazır fonksiyon: Rastgele sayı üretmek için kullanılır

dizi1 = []

for i in range(20):
    dizi1.append(random.randint(0,100))
    # randint(a,b): a-b arası rastgele tam sayı üretir

print("Dizi:", dizi1)

# Toplam bulma
toplam = 0
for k in range(20):
    toplam = toplam + dizi1[k]

print("Toplam:", toplam)

# Ortalama bulma
ort = toplam / len(dizi1)  # len(): dizinin eleman sayısını verir
print("Ortalama:", ort)

# En küçük ve en büyük bulma
dizi1.sort()   # sort(): listeyi küçükten büyüğe sıralar
print("Sıralı Dizi:", dizi1)

print("En Küçük:", dizi1[0])
print("En Büyük:", dizi1[-1])  # -1: son eleman
