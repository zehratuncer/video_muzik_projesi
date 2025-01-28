# if = eğer , else = değilse , 2 tane == eşit ise demek , elif = seçenek çoğaltıcı

kagan_not = input("Kağan'ın Notu = ")
erdem_not = input("Erdem'in Notu = ")
zeliha_not = input("Zeliha'nın Notu = ")

if kagan_not == zeliha_not == erdem_not:
    print("Üçünün notu birbirine eşittir.")
elif kagan_not == zeliha_not:
    print("Kağan'ın notu Zeliha'nın notuna eşittir.")
elif erdem_not == zeliha_not:
    print("Erdem'in notu Zeliha'nın notuna eşittir")    
elif kagan_not == erdem_not:
    print("Kağan'ın notu Erdem'in notuna eşittir.")        
else:
    print("Kimsenin notu birbirine eşit değildir.")