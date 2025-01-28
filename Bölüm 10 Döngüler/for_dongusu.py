list = [1,2,3,4,5]
#listenin elemanlarını yazdırmak için for kullanılır
for i in list:
    print(i)

_tuple = [(1,2),(4,5),(7,8)]
for a,b in _tuple:
    print(a,b)

_dictionary = {"apple":"elma","computer":"bilgisayar","book":"kitap","pencil":"kalem"}  
for x in _dictionary:
    print(x,_dictionary[x])  #anahtar ile değerini aynı anda yazdırır

#bu işlemi şöyle de yapabiliriz
for key,values in _dictionary.items():
    print(key,values)   

#for uygulamaları
list = [1,2,3,4,5]
for i in list:
    print(i*5)    #liste elemanlarının 5 katını yazdırma

#-----------------------------------------------------------------
toplam = 0
for sayilar in list:
    toplam += sayilar
print(toplam)   #liste elemanlarının toplamını yazdırma

#-----------------------------------------------------------------
kare = []
for sayi in list:
    if sayi % 2 == 0:
        kare.append(sayi**2)
print(kare) #listedeki çift sayıların karelerini yazdırma