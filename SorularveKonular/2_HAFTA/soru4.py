# Örnek 4: 1 den kullanıcının girmiş olduğu sayıya kadar olan
# tek ve çift sayıların toplamını ayrı ayrı bulan ve sonucu ekranda gösteren program.
n = int(input("Bir sayı girin: "))
cift_toplam = 0
tek_toplam = 0
for i in range(1, n+1):
    if i % 2 == 0:
        cift_toplam += i
    else:
        tek_toplam += i
print("Çift sayıların toplamı:", cift_toplam)
print("Tek sayıların toplamı:", tek_toplam)