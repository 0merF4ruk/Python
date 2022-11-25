islem = input("islem sembolü girin:")
sayi1 = int(input("sayi1:"))
sayi2 = int(input("sayi2:"))
if islem == "+":
    sonuc = int(sayi1) + int(sayi2)
    print("islemin sonucu: ", str(sonuc))
elif islem == "-":
    sonuc = int(sayi1) - int(sayi2)
    print("islemin sonucu: ", str(sonuc))
elif islem == "*":
    sonuc = int(sayi1) * int(sayi2)
    print("islemin sonucu: ", str(sonuc))
elif islem == "/1":
    sonuc = int(sayi1) / int(sayi2)
    print("islemin sonucu:", str(sonuc))
