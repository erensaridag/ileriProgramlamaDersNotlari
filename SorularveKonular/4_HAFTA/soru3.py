#3-Aşağıdaki matematiksel işlemi yapınız. xdeğeri 1 ile 10 arasındadır.
 # 𝑥
# 𝑥2
# 𝑥3
# S= + + + ⋯ , 1 ≤ 𝑥 ≤ 10
# 1!
# 2!
# 3!

import math

x = int(input("1 ile 10 arasında bir sayı girin: "))
S = 0

for i in range(1, x+1):
    S += (x ** i) / math.factorial(i)   # x^i / i! hesapla ve S'ye ekle

print("Sonuç:", S)
