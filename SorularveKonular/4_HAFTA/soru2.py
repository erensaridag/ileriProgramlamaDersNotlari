#2-Aşağıdaki işlemi yapınız.
      #1 ∗ 1 + 2 ∗ 2 + 3 ∗ 3 + ⋯ + 10 ∗ 10

import math

dizi = []
sayi_toplam = 0

for i in range(1,11):
    sayi_toplam += i*i

print("Sonuc : ",sayi_toplam)