# Örnek 2: En büyük sayının kuvvetini ve karekökünü alma

import math

a = int(input("1. sayıyı girin: "))
b = int(input("2. sayıyı girin: "))

en_buyuk = max(a, b)  # max() en büyük sayıyı bulur

print("Kuvvet (2. dereceden):", math.pow(en_buyuk, 2))   # Üs alma
print("Karekök:", math.sqrt(en_buyuk))                   # Karekök