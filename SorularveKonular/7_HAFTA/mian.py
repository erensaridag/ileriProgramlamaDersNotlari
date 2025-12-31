#Soru 1: Kullanıcıdan bir yaş değeri alınsın.
#Eğer yaş 0 veya negatifse, raise ifadesi kullanarak
#"Geçersiz yaş girdiniz!" şeklinde özel bir hata mesajı
#üretilsin.
try:
 yas=int(input("yaşınız giriniz:"))
 if yas<=0:
  raise ValueError("Geçersiz yaş girdiniz!")
except ValueError as hata:
 print("hatasız kod olmaz hatamla sev beni :P",hata)
finally:
  print("hala gençsiniz")