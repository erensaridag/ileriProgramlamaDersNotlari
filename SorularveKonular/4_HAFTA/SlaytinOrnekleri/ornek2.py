#Örnek 2: En büyük sayının kuvvetini ve karekökünü alma
import math

def orn2():
    sayilar = []
    n = int(input("Kaç sayı gireceksiniz: "))

    for i in range(n):
        sayi = float(input("Sayı girin: "))
        sayilar.append(sayi)

    en_buyuk = max(sayilar)
    print("En büyük sayı:", en_buyuk)
    print("Karesi:", math.pow(en_buyuk, 2))
    print("Karekökü:", math.sqrt(en_buyuk))

orn2()