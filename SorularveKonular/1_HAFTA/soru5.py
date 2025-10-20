#Örnek 4: Ortalamaya göre öğrencinin sınıf geçme durumunu (geçti – kaldı) gösteren

quiz1 = int(input("Enter the first quiz grade : "))
quiz2 = int(input("Enter the second quiz grade : "))
averages = (quiz1+quiz2)/2
if averages>60:
    print("Passed")
else :
    print("Failed")
