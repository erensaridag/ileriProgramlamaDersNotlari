# Örnek 2:
# Soru: 100-200 arasında rastgele atanan 100 tam sayıdan
# tek sayıların toplamını bulan program.

import random

dizi2 = []
toplam_tek = 0

for i in range(100):
    x = random.randint(100, 200)  # 100-200 arası rastgele sayı
    dizi2.append(x)
    if x % 2 == 1:  # % -> modül operatörü, tek sayı kontrolü
        toplam_tek += x

print("Dizi2:", dizi2)
print("Tek sayıların toplamı:", toplam_tek)
