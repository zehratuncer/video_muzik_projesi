#1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise veya üniversite olmalıdır.

isim = input("İsminizi giriniz :")
yas = int(input("Yaşınızı giriniz :"))
egitim = input("Eğitim bilginizi giriniz : ")

if(yas >= 18):
    if(egitim == "lise" or egitim == "üniversite"):
        print("Ehliyet Alabilirsiniz!")
    else:
        print("Ehliyet alma hakkınız yoktur!")
else:
    print("Yaşınız ehliyet almak için küçüktür!")

#2-Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1. Bakım -> 1.yıl
# 2. Bakım -> 2.yıl
# 3. Bakım -> 3.yıl   
# simdi = (2025/01/28)
import datetime

tarih = input("Aracınız hangi tarihte trafiğe çıktı : ")
tarih = tarih.split("/")

simdi=datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days
print(gun)
if(gun<=365):
    print("1.Servis bakımı gelmiştir!")
elif(gun>365) and (gun<=365*2):
    print("2.Servis bakımı gelmiştir!")
elif(gun>=365*2) and (gun<=365*3):
    print("3.Servis bakımı gelmiştir!")
else:
    print("Hatalı bilgi girdiniz!")
