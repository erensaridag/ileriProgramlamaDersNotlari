def toplam_islemi(n):
    sonuc = 0
    for i in range(2, n+1):
        sonuc += i / (i + 2)
    return sonuc

# Ana program
n = int(input("n değerini giriniz: "))
print("Sonuç =", toplam_islemi(n))
