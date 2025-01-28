web_site = "https://www.sadikturan.com/"
kurs_adi = "Pyton İle İleri Programlama"

#kurs_adi karakter dizisinde kaç karakter bulunmaktadır ?
sonuc = len(kurs_adi)
print(sonuc)

#web_site içinden www karakterlerini alın.
sonuc = web_site[8:11]
print(sonuc)

#kurs_adi içerisinden ilk 8 ve son 8 karakterleri alın.
sonuc = kurs_adi[0:8] , kurs_adi[-8:]
print(sonuc)

#kurs_adi ifadesindeki karakterleri tersten yaz.
sonuc = kurs_adi[::-1]           
print(sonuc)
''' 
:: --> tüm karakterleri aldığını ifade eder,
-1 --> sondan başa birer birer yazmayı ifade eder,
1  --> baştan sona birer birer yazmayı ifade eder.
'''

