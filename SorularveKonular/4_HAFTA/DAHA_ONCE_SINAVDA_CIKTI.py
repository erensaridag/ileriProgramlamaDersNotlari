import math
x = int(input(" X degerini giriniz : "))
y = int(input(" Y degerini giriniz : "))
toplam = 0
if  x>y:
    toplam = x+y
    print(toplam)
elif x==y:
    toplam = math.fabs(x-y)
    print(toplam)
else:
    toplam = math.factorial(x+y)
    print(toplam)