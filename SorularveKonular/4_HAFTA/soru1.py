#1-Aşağıdaki matematiksel işlemin programını yazınız?
# a ve b kullanıcı tarafından girilecektir.
 #   𝑠 = 𝑝𝑖 ∗ 𝑎2 + 𝑏 2

import math as m

a  = int(input("a sayisni girniz : "))
b = int(input("b sayisni girniz : "))

s = m.pi*(a**2)+(b**2)
print(s)
