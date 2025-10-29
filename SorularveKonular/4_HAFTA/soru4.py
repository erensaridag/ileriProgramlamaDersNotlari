import math

S = 0
for i in range(1, 11):  # 1'den 10'a kadar
    S += i * math.sqrt(i)  # i * √i

print("Sonuç:", S)
