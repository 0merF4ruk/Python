sayi = int(input("Faktöriyeli alınacak sayıyı giriniz:"))
faktoriyel = 1
sayici = 1
while sayi + 1 > sayici:
    faktoriyel *= sayici
    sayici += 1
print(faktoriyel)
