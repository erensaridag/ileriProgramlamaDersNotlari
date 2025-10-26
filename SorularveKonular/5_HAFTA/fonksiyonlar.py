print("---------------------------")

def myFun  ():
    print("Hello World ! ")

myFun()
print("---------------------------")
def nameFun(fname):
    print("Hello"+ fname +"!")

nameFun("Eren")
print("---------------------------")

def selamla(isim="isimsiz"):
    print("Merhaba",isim)
selamla()  # fun a deger gondermessek varsayilan degeri kullanir.
selamla("Mestan")

print("---- 2.ornek ----")
def myCountry(myCountry = "Norway"):
    print("My country : "+myCountry)

myCountry("Finland")
myCountry()
print("---------------------------")

def returnFun(x):
    return x*5

print(returnFun(3))
print(returnFun(5))
print(returnFun(9))

print("---------------------------")

def myFoods(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]

myFoods(fruits)

print("---------------------------")










