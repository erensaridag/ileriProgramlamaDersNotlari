 #geçme notlu olan sekli

vize = int(input("vize notunu gir : "))
final = int(input("final notunu gir : "))
ortalama = vize*0.4 + final*0.6
print(ortalama)
if ortalama>88:
    print("AA")
elif ortalama>60 and ortalama<88:
    print("+B")
else:
    print("kaldin")