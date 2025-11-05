
def soru1 (a,b) :
    sonuc = 0
    if a<b:
        sonuc = a*b-2
    elif a>b:
        sonuc = 2*a+2
    else:
        sonuc = 5

    return sonuc

x = soru1(3,5)
print(x)