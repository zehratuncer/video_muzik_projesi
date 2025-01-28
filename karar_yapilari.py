#range fonksiyonu belirli bir aralıkta sıraı sayılar üretmek için kullanılır.
for sayi in range(10):
    print(sayi)     #0123456789 sayilarini üretti

#alt sınır belirtmek istersek
for sayi1 in range(5,15):
    print(sayi1)   #5 6 7 8 9 10 11 12 13 14 üretti
#üstteki örneklerde hep birer birer arttırıldı

#artış miktarını kendimiz belirlemek istersek
for sayi2 in range(5,15,4):
    print(sayi2) #5 9 13 üretti

#azalan şeklinde yazdırmak istersek
for sayi3 in range(10,5,-1):
    print(sayi3)  #10 9 8 7 6 üretti

#pass komudu python dilinde "hiçbir şey yapmadan devam et" anlamına gelmektedir
harfler ="zehra"
while True:
    tahmin = input("Bir harf tahmini giriniz: ")
    if tahmin not in harfler:
        pass
    else:
        print("Bir harfi doğru tahmin ettiniz.")
        break    