sayi = int(input("Kaça kadar sayıların toplamını girmek istiyosunuz:"))
toplam = 0
for i in range(1, sayi, 1):
#sayıyı da dahil etmek istersek sayı+1 yapıyoruz.
    toplam += i
print("Sayıların toplamı:", str(toplam))
