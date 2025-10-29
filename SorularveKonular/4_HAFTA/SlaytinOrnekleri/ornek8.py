# Örnek 8: (sin(a) - 5*b) / (cos(a) + sin(b))

import math

a = float(input("a değerini derece cinsinden girin: "))
b = float(input("b değerini derece cinsinden girin: "))


sonuc = (math.sin(a) - 5 * b) / (math.cos(a) + math.sin(b))

print("Sonuç:", sonuc)
