# Örnek 5: 10-1000 arasındaki elemanlarının 5’e bölümünden kalan
# 2 olanlarının eleman sayısını yazdıran program.
sayac = 0
for i in range(10, 1001):
    if i % 5 == 2:
        sayac += 1
print("5'e bölümünden kalan 2 olan sayıların sayısı:", sayac)