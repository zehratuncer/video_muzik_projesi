#Daha bir çok metdou öğrenmek için --> https://www.w3schools.com/python/default.asp

#Upper metodu, karakterlerin hepsini büyük harfe çevirir.
message = "hello there"
sonuc = message.upper()
print(sonuc)

#Lower metodu, karakterlerin hepsini küçük harfe çevirir.
message2 = "SELAMLAR"
sonuc = message2.lower()
print(sonuc)

#title() metodu, karakter dizisindeki her kelimenin baş harfini büyük harfe çevirir.
message3 = "merhaba arkadaşlar"
sonuc = message.title()
print(sonuc)

#capitalize(), karakter dizisindeki sadece ilk kelimenin baş harfini büyük harfe çevirir.
message4 = "selamlar, bugün nasılsınız?"
sonuc = message3.capitalize()
print(sonuc)

#Strip metodu, karakter dizisinin baş ve sondaki boşluk karakterlerini siler.
message5 = "      Zehra       "
sonuc = message4.strip()
print(sonuc)

#is ile başlayan metodlar soru soruyor
#islower metodu, tüm harfler küçük mü sorusunu sorar.
message6 = "GALATASARAY ÜNİVERSİTESİ"
sonuc = message6.islower()
print(sonuc)

#Eğer strip() metodunun belirttiğimiz karakterleri silmesini istersek;
username = ",,,,...!!zehratuncer***"
x = username.strip(',.!*')
print("my username is " + x)

#Split metodu, boşluklarla ayrılan kelimeleri bir parantez içerisinde kelime olarak ayırır. 
#split() parantez içerisine koyduğun şeyden ayırabilirsin.
message7 = "Önemli. Değil?"
sonuc = message7.split(".")
print(sonuc)
message8 = "Bugün Hava Çok Güzel"
sonuc = message8.split()
print(sonuc)
ornek = "Sıfırıncı, Birinci, İkinci index"
sonuc = ornek.split()
print(sonuc[0])  #sıfırıncı indexi yazdırır

#Join metodu ile ifadeler arasına koyduğun şey ile birleşebilir
message9 = "Güzel Günler Göreceğiz"
sonuc = "-".join(sonuc)
print(sonuc)

#endswith ve startswith , Cümlenin ne ile başlayıp bittiğini sorar.
message10 = "Nice the meet you"
sonuc = message10.endswith("o")  #cümle o ile mi bitti
print(sonuc)
sonuc = message10.startswith("N")#cümle N ile mi başladı
print(sonuc)

#Replace metodu karakter güncellemesi için kullanılır. 
isim = "Zehra Tuncer"
isim = isim.replace('Zehra','Selin')
print(isim)

#bir stringin değerini değiştirmek için replace() kullanılır
s1 = "güneşli"
s2 = "bulutlu"
s3 = s1.replace("güneşli",s2)
print(s3)

