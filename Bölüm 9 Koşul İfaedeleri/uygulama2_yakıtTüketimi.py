benzinFiyat = 6.69
dizelFiyat = 5.86

ortalamaYakitTuketimi = float(input("100 km'dki ortalama yakıt tüketimini giriniz : "))
gidilecekYol= float(input("Gidilecek yol kaç km: "))
yakitTipi = input("Yakıt tipiniz nedir :")

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if (yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
elif(yakitTipi == "dizel"):
    toplamYakitUcreti = round((dizelFiyat * toplamYakitTuketimi),2)
else:
    print("Yanlış bir değer giriniz!")

print(f"Toplam yakit tüketimi : {toplamYakitUcreti}")