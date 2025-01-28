"""Tuples listelere benzer ancak tek farkı oluşturulduktan sonra üzerinde ekleme, silme, değiştirme sıralama gibi işlemler yapılamaz"""
demet = tuple() #boş bir demet tanımlar
demet = tuple([1,2,3]) #içerisinde 1,2,3 değerleri olan bir demet tanımlar
demet = (1,2,3) #içerisinde 1,2,3 değerleri olan farklı bir tanımlama biçimi 
demet = ("elma","kiraz","armut") #string demeti
demet = (1,2,"elma",2.5,True) #farklı türde elemanlardan oluşan bir demet

#demet elemanlarına erişim 
demet = (1,2,3)
a = demet[1]
print(a)

#demet eleman sayısı bulma
demet = (1,2,3)
uzunluk = len(demet)
print(uzunluk)

#demeti ekrana yazdırma
demet=(1,2,3)
print(demet)
#veya
for i in demet:
    print(i)
#ve daha niceleri listede yapılanlar burada da yapılıyor..    