sayilar = [20, 12, 42, 647, 13, 1, 8, 9, 100]

#Sayilar listesinin elemanlarını yazdırma while ile
index = 0
while index < len(sayilar):
    print(sayilar[index])
    index += 1

#başlangıç ve bitiş değerlerini kullanıcıdan alıp tüm tek sayıları ekrana yazdırın
baslangic = int(input("Başlangıç değerini giriniz :"))
bitis = int(input("Bitiş değerini giriniz: "))

i = baslangic

while (i < bitis):
    i+=1
    if(i%2==1):
        print(i)

#1-100 arasındaki sayıları azalan şeklinde yazdırma
i = 100
while (i>0):
    print(i)
    i -=1

#kullanıcıdan aldığımız 5 sayıyı sıralı şekilde yazdıralım

sayilar = []
i=0
while(i<5):
    sayi = int(input("Sayı:"))
    sayilar.append(sayi)
    i+=1
sayilar.sort()
print(sayilar)
