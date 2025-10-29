# Örnek 5: S = 1/1! + 2/2! + ... + x/x! , 1 ≤ x ≤ 10

import math

x = int(input("1 ile 10 arasında bir sayı girin: "))
s = 0

for i in range(1, x + 1):
    s += i / math.factorial(i)

print("Sonuç:", s)
