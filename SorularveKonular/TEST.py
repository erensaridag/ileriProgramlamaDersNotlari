import random as r

dizi = []
sayi =0
for i in range(100):
    x = r.randint(100,200)
    dizi.append(x)
    if x %3 ==0:
        sayi+=1

print(dizi)
print(sayi)