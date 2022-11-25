dosya = open("../../../PycharmProjects/Python/sayilar.txt", "r")
# dosyayı okuma modunda açmak için r yazdık.
icerik = dosya.read()
# içerik değişkeni atayıp dostaları okumak için yazdık.
dosya.close()
# kaynak kullanımı için dosyayı kapatıyoruz.
for i in icerik.splitlines():
    # her bir satırı satır satır bölünmesini sağlayıp her satırdaki elemanları teker teker i değişkenine atamasını sağlıyor.
    print(i)
