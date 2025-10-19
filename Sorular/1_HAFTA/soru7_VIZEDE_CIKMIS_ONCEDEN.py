 #onceden cikmis vize sorusu-1
 #a ile b değerleri dışarıdan kullanıcı tarafından girilecektir.
 # Aşağıdaki işlemi yapan program yazınız.

        # ⎧a < b  ->  a * b - 2
# sonuc1 = ⎨a > b   -> 2 * a + 2
       #  ⎩a = b  ->  5

a = int(input("Birinci sayiyi giriniz : "))
b = int(input("Ikinci sayiyi giriniz :"))
sonuc = 0
if a < b:
  sonuc =  a * b - 2
elif a > b:
    sonuc= 2*a+2
elif a == b:
    sonuc = 5
print(sonuc)

