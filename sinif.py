sinif_a=("0,1,2,3,4,5,6,7,8,9")
sinif_b=("10,11,12,13,14,15,16,17,18,19,20")
isim=input("0<=sayi=>20 kuralinda sayi girin:")
if isim in sinif_a:
      print("sayi a sinifindadir.")
elif isim in sinif_b:
      print("sayi b sinifindadir.")
else:
      print("sayi belirtilen siniflarda bulunmamaktadir.")