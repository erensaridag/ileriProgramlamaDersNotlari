"""
Örnek 1: Girilen değerlerden en küçüğünü bulan program

"""
def orn1():
    sayilar = []
    n = int(input("Kaç sayı gireceksiniz: "))

    for i in range(n):
        sayi = int(input("Sayı girin: "))
        sayilar.append(sayi)

    print("En küçük değer:", min(sayilar))

orn1()

