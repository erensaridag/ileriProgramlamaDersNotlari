 #geçme notlu olan sekli

vize = input("vize notunu gir : ")
final = input("final notunu gir : ")
vize = int(vize)
final = int(final)
ortalama = vize*0.4 + final*0.6
print(ortalama)
if ortalama>88:
    print("AA")
elif ortalama>60 and ortalama<88:
    print("+B")
else:
    print("kaldin")