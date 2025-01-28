#Sözlükler üzerinde ekleme, silme, güncelleme yapılabilir.
#sozluk = {anahtar1:deger1, anahtar2:deger2...} olarak tanımlanır

#ing-türkçe sözlük
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pencil":"kalem"}

#sözlük elemanlarına erişim
kelime = sozluk["book"]
print(kelime)

#get() komudu parantez içerisine yazılan anahtara ait değeri bulmamızı sağlar
kelime = sozluk.get("orange")   #bulunmadığı için none değer üretir
kelime2 = sozluk.get("book")    #kitap olarak bulur ancak parantez içine kitap yazsaydık none dönerdi
print(kelime)
print(kelime2)

#sözlüğe eleman ekleme
sozluk ["rose"] = "gül"
print(sozluk)

#sözlük elemanlarını değiştirme
sozluk["pencil"] = "dolma kalem"
print(sozluk)

#sözlükten eleman silme
del sozluk["pencil"]    #pencili sildi
print(sozluk)

#sözlüğü temizleme
sozluk.clear()
print(sozluk)

#sözlük elemanlarını listeleme
sozluk = {"apple":"elma","computer":"bilgisayar","book":"kitap","pencil":"kalem"}
for k in sozluk:
    print("İngilizcesi:",k,"-> Türkçesi:",sozluk[k])

#items() komudu bir sözlüğün içerisinde hem anahtar hem de değerlere aynı anda erişmemizi sağlar
print(sozluk.items())    #dict_items([('apple', 'elma'), ('computer', 'bilgisayar'), ('book', 'kitap'), ('pencil', 'kalem')])

#keys() komudu ile sözlüğün anahtar kelimelerine ulaşılır
for k in sozluk.keys():
    print(k)

#values() komudu ile sözlüğün anahatar kelimelerinin değerlerine erişilir
for k in sozluk.values():
    print(k)

#sözlükte anahtar varlığını kontrol etme (in veya not in)
print("apple" in sozluk) #sözlükte apple var mı ? = True
print("orange" not in sozluk) #sözlükte orange yok mu ? = True

#sözlük güncelleme update()
urun = {"kalem":2,"defter":5,"makas":4}
guncel = {"kalem":7,"defter":3,"makas":2,"boya":8}
urun.update(guncel)
print(guncel)
print(urun)

#sözlük kopyalama copy()
havadurumu = {"ankara":"bulutlu","izmir":"güneşli","bursa":"karlı"}
tahmin = havadurumu.copy()
print(tahmin)

#bir örnek
ogrenciler = {
    100:
    {
        "ad":"zehra",
        "soyad":"tuncer",
        "yas":20
    },
    101:
    {
        "ad":"sahin",
        "soyad":"tuncer",
        "yas":35
    }
}
print(ogrenciler[100])
print(ogrenciler[100]["ad"])