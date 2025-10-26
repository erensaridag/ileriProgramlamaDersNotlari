
def soru1 (a,b) :
    sonuc1 = 0
    if a<b:
        sonuc1 = a*b-2
    elif a>b:
        sonuc1 = 2*a+2
    else:
        sonuc1 = 5

    return sonuc1

x = soru1(3,5)
print(x)