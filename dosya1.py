for i in range(1, 10, 1):
    dosya = open("../../../PycharmProjects/Python/sayilar.txt", "a")
    #Bir dosyaya ifadenin teker teker eklenmesiini istiyosak append mod : a
    #Sadece o dosyaya ver yazdırmak için ise write mode : w kullanılması gerekir.
    veri = str(i) + "\n"
    dosya.write(veri)
    dosya.close()
