import math

s = 0
k = 0
A = int(input(" A degerini giriniz : "))
B = int(input(" B degerini giriniz : "))

s = math.sin(B)+3*math.pow(A,4)
k = math.sqrt(A+B)
sonuc = s/k
print("Sonuc : ",sonuc)
