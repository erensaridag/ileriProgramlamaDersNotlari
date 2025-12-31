metin1 = "Python"
print(metin1[4])
print(metin1[-3])
print("------------------------")
metin = "Programlama"

print(metin[0:3])   # Pro
print(metin[:4])    # Prog
print(metin[-3:])   # ama
print(metin[::2])    # ikiser atlama

print("---------------------------")

ad = "Eren"
soyad = "Sarıdağ"
print(ad + " " + soyad)
print("---------------------------")

print("Python " * 3)

print("---------------")
metin4 = "pYtHon"

print(metin4.upper())
print(metin4.lower())
print(metin4.title())

print("---------------")

metin = "Veri123"       # harf + rakam içeren string
print(metin.isalpha())  # False döner

print("---------------")

metin = "Python Programlama"  # uzun bir string

print("eren" in metin) # "Python" kelimesi string içinde mi kontrol eder
