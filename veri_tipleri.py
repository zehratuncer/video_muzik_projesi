#string = yazı
#integer = normal sayı - 2484384, 2, 34,
#float = virgüllü sayılar - 23.56
#round = sayıyı yuvarlar
#bool = true v false
#bir şeyi yazdırmak için = print()
#kullandığım ifadenin tipini öğrenmek için = print(type(ifade))

'''
pi = "3.14"
pi_sayisi = 3.14
print(type(pi_sayisi))

#sayıyı yazıya çevirmek isterken başına "str" sayıa çevirmek isterken başına "int"
print(str(pi_sayisi))
print(float(pi))
'''

# dairenin alanını ve çevresini hesaplama

pi = 3.14
r = float(input("Yarı Çapı Giriniz = "))
alan = pi * (r**2)
cevre = 2 * pi * r

print("Alan  : ",alan)
print("Çevre : ",cevre)

#km mil çevirimi
mesafeKm = int(input("Kaç km yol gittiniz : "))
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2) #noktadan sonra 2 basamak alır

print(str(mesafeKm) + "km = " + str(mesafeMil) + " mil.")