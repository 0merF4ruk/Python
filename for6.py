sayi = int(input("Kaça kadar asal sayıları yazdıracağını belirtiniz:"))
print(2)
for i in range(3, sayi, 1):
    kontrol = False
    for j in range(2, i):
        if i % j == 0:
            kontrol = True
    if kontrol == False:
        print(i)
