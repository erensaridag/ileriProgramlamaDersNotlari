
# 1. Tek sayıların karesi, çift sayıların küpü
print("1. Soru: Teklerin karesi, çiftlerin küpü\n")

n = int(input("Kaç eleman gireceksiniz: "))
liste = []
for i in range(n):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    liste.append(sayi)

yeni_liste = []
for x in liste:
    if x % 2 == 0:
        yeni_liste.append(x ** 3)
    else:
        yeni_liste.append(x ** 2)

print("Orijinal Liste:", liste)
print("Yeni Liste:", yeni_liste)
print("-" * 50)


# 2. Pozitif, negatif ve sıfır sayıları sayma
print("2. Soru: Pozitif / Negatif / Sıfır sayma\n")

liste = []
n = int(input("Kaç sayı gireceksiniz: "))
for i in range(n):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    liste.append(sayi)

pozitif = negatif = sifir = 0

for x in liste:
    if x > 0:
        pozitif += 1
    elif x < 0:
        negatif += 1
    else:
        sifir += 1

print("Pozitif sayı adedi:", pozitif)
print("Negatif sayı adedi:", negatif)
print("Sıfır sayısı:", sifir)
print("-" * 50)


# 3. Aritmetik ortalama ve karşılaştırma
print("3. Soru: Aritmetik ortalama karşılaştırması\n")

liste = []
n = int(input("Kaç sayı gireceksiniz: "))
for i in range(n):
    sayi = float(input(f"{i+1}. sayıyı girin: "))
    liste.append(sayi)

ortalama = sum(liste) / len(liste)
ustunde = [x for x in liste if x > ortalama]
altinda = [x for x in liste if x < ortalama]

print("Liste:", liste)
print("Aritmetik Ortalama:", ortalama)
print("Ortalamanın Üstündekiler:", ustunde)
print("Ortalamanın Altındakiler:", altinda)
print("-" * 50)


# 4. Doğru / Yanlış değerlendirme
print("4. Soru: Doğru / Yanlış Önermeleri\n")

dogru_yanlis = {
    "a": "❌ Python’da doğrudan switch-case yoktur.",
    "b": "✅ match-case ifadesi Python 3.10+ ile eklenmiştir.",
    "c": "✅ list veri tipi sıralı ve değiştirilebilir bir yapıdır.",
    "d": "✅ İlk elemana [0] ile ulaşılır.",
    "e": "❌ append() sonuna ekler, başına değil.",
    "f": "✅ remove() belirtilen değeri siler.",
    "g": "❌ pop() indeks verilirse farklı eleman da siler.",
    "h": "✅ sort() küçükten büyüğe sıralar.",
    "i": "✅ reverse() sırayı tersine çevirir.",
    "j": "✅ Modül .py uzantılı dosyalardan oluşur.",
    "k": "❌ math modülü yalnızca karekök ve log için değildir.",
    "l": "❌ random.choice() sadece 1 eleman seçer.",
    "m": "✅ random.randint(1,10) 1-10 dahil rastgele sayı üretir.",
    "n": "✅ enumerate() eleman ve indeks verir.",
    "o": "✅ extend() başka bir listenin elemanlarını ekler."
}

for harf, ifade in dogru_yanlis.items():
    print(f"{harf}) {ifade}")
