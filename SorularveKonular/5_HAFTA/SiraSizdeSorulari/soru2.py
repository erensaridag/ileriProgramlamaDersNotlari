import random


def dizi_islemleri(min_deger, max_deger, eleman_sayisi):
    sayilar = [random.randint(min_deger, max_deger) for _ in range(eleman_sayisi)]

    # 3'e bölünenlerin sayısı
    uce_bolunen = [x for x in sayilar if x % 3 == 0]
    uce_bolunen_sayisi = len(uce_bolunen)

    # Çift sayıların ortalaması
    ciftler = [x for x in sayilar if x % 2 == 0]
    if len(ciftler) > 0:
        cift_ortalama = sum(ciftler) / len(ciftler)
    else:
        cift_ortalama = 0

    return uce_bolunen_sayisi, cift_ortalama


# Ana program
adet, ort = dizi_islemleri(100, 200, 100)
print("3'e bölünen sayı adedi:", adet)
print("Çift sayıların ortalaması:", ort)
