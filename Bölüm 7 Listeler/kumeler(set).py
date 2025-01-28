"""
Kümeler ile tuples(demetler) arasındaki farklar:
1)
set: Değiştirilebilir, eleman eklenebilir veya çıkarılabilir
tuple: Ddeğiştirilemez, bir kez oluşturulduktan sonra üzerinde işlem yapılamaz
2)
set: Aynı elemandan sadece bir tane bulunabilir birden fazla varsa bile çıktıda bir tane gösterir
tuple: Elemanlar birden fazla olabilir
3)
set: Sırasızdır.Elemanların belli bir sırası yoktur.
tuple: Sıralıdır.Elemanlar eklenme sırasına göre saklanır.
4)
set: Genellikle benzersiz elemanlar kümesi gerektiğinde kullanılır. Küme işlemler(birleşim,fark vb)
tuple: Genellikle sabit veri koleksiyonları gerektiğinde kullanılır 
"""
kume = set() #boş bir küme tanımlar
kume2 = {1,2,3} #2.tanımlanma biçimi

#daha önce tanımlı olan listeler veya demetler de kümeye dönüştürülebilir
liste = ["yeşil","beyaz","kırmızı"]
renkler = set(liste)
print (renkler)

#değiştirilemez bir küme oluşturmak için frozenset() kullanılır
fs = frozenset(["deneme","bir","iki","üç"]) #ekleme veya çıkarma yapılamaz

#kümeye eleman ekleme
kume2.add(4)
print(kume2)
#birden fazla eleman ekleme
kume2.update([5,6,7,8,9])
print(kume2)

#kümeden eleman çıkartmak
kume2.remove(9)
print(kume2)

#iki küme farkı: bir kümede olup diğer kümede olmayan elemanlaraı bulma işlemine fark alma denir difference() kullanılır
kume1 = {1,2,3,4,5}
kume2
fark = kume2.difference(kume1)
print(f'İki küme farkı: {fark}')
#başka bir fark alma biçimi
fark = kume2 - kume1
print(f'İki küme farkı: {fark}')

#kesişim kümesi: her iki kümede de var olan elemanı bulma
kume1 = {1,2,3,4,5}
kume2 = {1,2,3,4,5,6,7,8}
kesisim = kume1.intersection(kume2)
print(kesisim)
#başka bir kesişim alma biçimi
kesisim = kume1 & kume2
print(kesisim)

#birleşim kümesi 
kume1 = {1,2,3,4,5}
kume2 = {1,2,3,4,5,6,7,8}
birlesim = kume1.union(kume2)
print(birlesim)
#başka bir birleşim tanımlanma biçimi
birlesim = kume1 | kume2
print(birlesim)

#ayrık küme tespiti: iki kümenin ortak elemanı var olup olmadığını kontrol etme
kume1 = {1,2,3}
kume2 = {3,4,5}
ayrikKumeMi = kume1.isdisjoint(kume2) #3 ortak olduğu için false döner
print(ayrikKumeMi)

#alt küme 
kume1 = {1,2,3}
kume2 = {1,2,3,4,5}
altKume = kume1.issubset(kume2)
print(altKume)

#kapsayan küme
kume1 = {1,2,3}
kume2 = {1,2,3,4,5}
kapsar = kume2.issuperset(kume1)
print(kapsar)