sayi = int(input("Faktöriyel işlem için sayı giriniz:"))
faktoriyel = 1
for i in range(1, sayi + 1, 1):
    faktoriyel *= i
print(faktoriyel)
