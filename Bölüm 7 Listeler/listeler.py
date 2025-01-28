#Python listelerinde eleman sayısını len() metodu ile öğrenebiliriz

list1 = ['one','two','there']
list2 = [[1,2,3],[4,5,6],[7,8,9],10]

print(len(list1)) # 3
print(len(list2)) # 4

list3 = ["Python", "C#", "JavaScript","Java"]

if "C#" in list3:       #Eğer list3'ün içinde c# var ise
    print("True")
else:
    print("False")

del list3[3]    #Listenin 4. elemanını sildi
print(list3)

#listeleri ekrana yazdırma
liste = [50,60,70]
print(liste)
#her bir elemanı bağımsız yazdırma
for a in liste:
    print(a)
#elemanların iki katını yazdırma
for i in range(0,len(liste)):
    liste[i] *= 2
print(liste)     

#Bir listeyi kendi elemanlarını tekrar ederek çoğaltmak için * operatörü kullanılır
x = [10,20,30]
y = x*2
print(y)

#listeye eleman ekleme append() komudu ile yapılır
liste = [10,20,30]
liste.append(40)
print(liste)

#listenin belirtilen indisine bir eleman eklemek için insert() komudu kullanılır
liste.insert(1,15)  #burada 1 hangi indexe koyacağımızı söyler, 15 kısmı ise koyduğumuz elemanı temsil eder
print(liste)

#listeye birden fazla eleman eklemek için extend() kullanılır
liste.extend([3,5,10,15,20,25])
print(liste)

#remove() komudu bir liste içerisinde belirtilen değeri çıkarmak için kullanılır
liste.remove(20)
print(liste)
#liste içerisinde aynı değer birden çok kez bulunuyorsa yalnız ilki silinir.

#pop() sondaki elemanı silmeye yarar
liste.pop()
print(liste)

#Herhangi bir elemanın liste içerisinde var olup olmadığı "in" ve "not in" operatörleri ile kontrol edilebilir
liste = [10,20,30]
sonuc = 10 in liste
print(sonuc) 

sonuc = 70 not in liste
print(sonuc)

#index() bu komut herhangi bir elemanın liste içerisinde hangi indexte yer aldığını bulmamızı sağlar
indeks = liste.index(10)
print(indeks)
#liste içerisinde aynı değer birden çok kez bulunuyorsa yalnızca ilk değerin bulunduğu indexi verir.

#liste kopyalama
list = [50,60,70]
copy = list[:]
print(copy) #tümünü kopyalar

copy = list[1:3]
print(copy) #1. ve 2. indexi kopyalar

#listeyi küçükten büyüğe sıralama sort()
liste = [2,5,7,1,3,9]
liste.sort()
print(liste)
#bir listenin mevcut eleman sırasını tersin çevirmek için reverse() kullanılır
liste = [2,5,7,1,3,9]
liste.reverse()
print(liste)
#sıralı hali tersine çevirmekte bir seçenektir
liste = [2,5,7,1,3,9]
liste.sort()
liste.reverse()
print(liste)

#liste içinde bir elemanın kaç kez tekrar ettiğini bulma count()
liste = [2,3,6,1,7,8,1,2]
k = liste.count(1)
print(k)

#liste elemanlarının toplamını bulma sum()
liste = [1,2,3,4,5]
toplam = sum(liste)
print(toplam)

#Liste üreteçleri
liste = [a for a in range(5)]
print(liste)