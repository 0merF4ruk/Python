us = int(input("Üssü girin:"))
taban = int(input("Tabanı girin:"))
sonuc = 1
for i in range(1, us + 1, 1):
    sonuc *= taban
print(sonuc)
