# Örnek 7: f(x) = -2x + 3 (x<5) , pi*x^3 (x>=5)

import math

x = float(input("x değerini girin : "))

if x < 5:
    fx = -2 * x + 3
else:
    fx = math.pi * (x ** 3)

print("Sonuç:", fx)
