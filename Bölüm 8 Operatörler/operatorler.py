# == eşit ise , != eşit değil ise , and = ve operatörü , or = veya operatörü , not = değil operatörü --> !=

a = int(input("Bir sayı giriniz = "))

if a < 3 or a > 5:
    print("Sonuç doğru!")

'''
** --> operatörü üs olarak yazar ,
% mod --> operatörü sayıı böler ve kalanı yazar ,
// --> operatörü bölüm yapar ve tam kısmı ifade eder.
sep --> boşlklara istediğini koyabilir 
'''

#tümleyen işlemi ~ işareti ile yapılır
a = 1
b = ~a
print(b) #1 sayısının ikili tabandaki tümleyeni b'dir.

#Aitlik operatörler (in ve not in)
print("a" in "merhaba") # merhaba kelimesinin içerisinde a karakteri var mı
print("abc" not in "merhaba") #merhaba kelimesinin içerisinde abc(bütün olarak) var olmadığı için ve not in olduğu için true döner

#Kimlik operatörü (id)
a = 20
print(id(a)) #a değişkeninin bellek adresidir.

#is ve is not, iki nesnenin bellek adreslerini yani id'lerini karşılaştıran operatörlerdir
a = 20
b = 30
print(a is b) #id(a) ile id(b) aynı sonucu üretiyorsa yani bellek adresleri aynı ise True, farklı ise False sonuç verir
                