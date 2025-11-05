import math
def soru4(r):
 alan=math.pi*math.pow(r,2)
 cevre=2*math.pi*r
 hacim=1   # gereksiz aslinda ama hoca boyle yazmis kendi kodunda 
 return alan,cevre,hacim

a,c,h=soru4(5)
print(a)
print(c)