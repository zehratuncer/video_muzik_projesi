list = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]

#Liste kaç elemanlıdır?
result = len(list)
print(result)

#Listenin ilk ve son elemanı nedir?
print(list[0]+" , "+list[-1])

#Samsung S5 Değerini Samsung S4 İle Değiştirin.
list [0] = "Samsung S4"
print(list)

#Samsung S6 değeri listenin bir elemanı mıdır?

if "Samsung S6" in list:
    print("Samsung S6 liste içerisinde bulunuyor.")
else:
    print("Listede bulunmuyor.")

#Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" yazdırın
list[-2:] = ["Samsung S9", "Samsung S10"]
print(list)


