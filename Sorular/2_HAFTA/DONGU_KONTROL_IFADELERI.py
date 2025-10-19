# Break ve Continue:
# - break komutu döngüyü tamamen sonlandırır (for ve while kullanılır)
# - continue komutu döngünün o turunu atlar ve bir sonraki turdan devam eder (for ve while kullanılır)

# Örnek 1: continue kullanımı
x = 0
while x < 5:
    x += 1
    if x == 2:
        continue  # x 2 olduğunda o turu atla
    print(x)
# Açıklama: x 5'ten küçük olduğu sürece ekrana yazdırılır,
# ancak x 2 olduğunda continue çalışır ve 2 ekrana yazılmaz.
# Döngü 3'ten devam eder.

print("\n---\n")

# Örnek 2: break kullanımı
x = 0
while x < 5:
    x += 1
    if x == 2:
        break  # x 2 olduğunda döngüyü sonlandır
    print(x)
# Açıklama: x 5'ten küçük olduğu sürece ekrana yazdırılır,
# ancak x 2 olduğunda break çalışır ve döngü biter.
# Ekrana sadece 1 yazdırılır.

print("\n---\n")

# Pass: Hiçbir işlem yapmadan blok çalışmaya devam eder
x = 0
while x < 5:
    x += 1
    if x == 2:
        pass  # x 2 olduğunda hiçbir işlem yapma
    print(x)
# Açıklama: x 5'ten küçük olduğu sürece ekrana yazdırılır,
# x 2 olduğunda pass çalışır ama kod akışı devam eder.
# Ekrana 1,2,3,4,5 yazdırılır.
