# Örnek 1: Girilen değerlerden en küçüğünü bulan program

a = int(input("1. sayıyı girin: "))
b = int(input("2. sayıyı girin: "))
c = int(input("3. sayıyı girin: "))

en_kucuk = min(a, b, c)  # min() en küçük değeri bulur
print("En küçük sayı:", en_kucuk)
