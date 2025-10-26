#Örnek 1: Bir diziye 0-100 arasında rastgele olarak
#atanan 20 tam sayı

import random as r

dizi1=[]
for i in range(0,20):
    dizi1.append(r.randint(1,100))

print(dizi1)
