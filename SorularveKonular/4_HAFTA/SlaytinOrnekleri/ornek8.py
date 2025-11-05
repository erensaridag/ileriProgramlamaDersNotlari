# Örnek 8: (sin(a) - 5*b) / (cos(a) + sin(b))

import math as m

a = float(input("a değerini derece cinsinden girin: "))
b = float(input("b değerini derece cinsinden girin: "))


sonuc = (m.sin(a) - 5 * b) / (m.cos(a) + m.sin(b))

print("Sonuç:", sonuc)
