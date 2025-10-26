import random as r

def soru2 ():
    dizi = []
    sayi = 0

    for i in range(50):
        dizi.append(r.randint(10,1000))
        if dizi[i]%5==2:
            sayi=sayi+1

    return sayi

print(soru2())