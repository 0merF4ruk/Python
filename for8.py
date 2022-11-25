veri = "BTK Eğitim 181"
egitim = list(veri)
print(egitim)
harf_sayici = 0
rakam_sayici = 0
for i in egitim:
    if str(i).isdecimal():
        rakam_sayici += 1
    else:
        harf_sayici += 1
print("Rakam sayıcı", rakam_sayici)
print("Harf sayıcı", harf_sayici)
