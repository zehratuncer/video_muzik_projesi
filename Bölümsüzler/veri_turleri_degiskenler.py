print("İstanbul","İzmir", sep="-") #2 kelimenin arasına tire koyar.
print("1","2","3","4","5", sep="-") #çıktısı : 1-2-3-4-5 bunu yapmanın daha basit bir yolu aşağıda
print(*"12345", sep = "-")
print(*"12345") #herhangi bir sep verilmediyse, aralara boşluk gelir
print(1,2,3,4, sep="x") #istenilen işaret aralara konulabilir
print("python öğreniyoruz", end ="!") #ekrana yazdırılan ifadenin sonuna ! işareti konur
print("merhaba \n python") #\n newline alt satıra geçer
print("A \t B \t C") #ifadeler arasında bir tab boşluk gelir
print("\a") #bip veya alarm sesi çaldırır
print("python \r programlama") # karakter dizisi içerisinde bulunduğu noktadan itibaren satır başına kadar olan kısmı siler

