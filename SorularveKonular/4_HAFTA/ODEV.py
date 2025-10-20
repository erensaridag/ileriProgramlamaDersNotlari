import math

# SORU 1: S = √(a³ + b³) + π × (a+b)
a = int(input("a değerini girin: "))
b = int(input("b değerini girin: "))
s = math.sqrt(a**3 + b**3) + math.pi * (a + b)
print(f"Sonuç: {s}")


# SORU 2: S = √1 + √2 + √3 + … + √15
s = 0
for i in range(1, 16):
    s += math.sqrt(i)
print(f"Sonuç: {s}")


# SORU 3: S = (x/2!) + (x²/4!) + (x³/6!) + … + (x⁵/10!)
x = float(input("x değerini girin: "))
s = 0
for n in range(1, 6):
    s += x**n / math.factorial(2*n)
print(f"Sonuç: {s}")


# SORU 4: S = 1/(1+1) + 2/(2+1) + 3/(3+1) + … + n/(n+1)
n = int(input("n değerini girin: "))
s = 0
for i in range(1, n + 1):
    s += i / (i + 1)
print(f"Sonuç: {s}")


# SORU 5: A = (cos(a) + sin(b)) / √(a²+b²)
a = float(input("a değerini girin: "))
b = float(input("b değerini girin: "))
a_sonuc = (math.cos(a) + math.sin(b)) / math.sqrt(a**2 + b**2)
print(f"Sonuç: {a_sonuc}")



# SORU 6: S = Σ (xᵢ² + 1) / √xᵢ
liste = [float(x) for x in input("Sayıları virgülle girin: ").split(',')]
s = 0
for x in liste:
    s += (x**2 + 1) / math.sqrt(x)
print(f"Sonuç: {s}")