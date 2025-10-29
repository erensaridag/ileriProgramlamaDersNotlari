# Örnek 4: 100 - 200 arası rastgele 100 sayıdan
# 3'e tam bölünen kaç eleman vardır?

import random

dizi = []
sayi = 0

for i in range(100):
    dizi.append(random.randint(100,200))
    if dizi[i] % 3 == 0:
        sayi = sayi + 1

print("3’e bölünen sayı adedi:", sayi)
