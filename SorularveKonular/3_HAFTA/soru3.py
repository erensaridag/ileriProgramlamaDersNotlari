# Örnek 3:
# Soru: 1-600 arasında rastgele atanan 100 tam sayıdan
# çift sayıların sayısını bulan program.

import random

dizi3 = []
cift_sayi = 0

for i in range(100):
    x = random.randint(1, 600)  # 1-600 arası rastgele sayı
    dizi3.append(x)
    if x % 2 == 0:  # % -> modül operatörü, çift sayı kontrolü
        cift_sayi += 1

print("Dizi3:", dizi3)
print("Çift sayı adedi:", cift_sayi)
