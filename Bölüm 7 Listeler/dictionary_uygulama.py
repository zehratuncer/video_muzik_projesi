#3 ürün bilgisini kullanıcıdan al ve bir sözlükte sakla
urunler = {}

id = input('id : ')
ad = input('ad : ')
fiyat = input('fiyat : ')
urunler [id] = {
    "ad":ad,
    "fiyat":fiyat
}
id = input('id : ')
ad = input('ad : ')
fiyat = input('fiyat : ')
urunler [id] = {
    "ad":ad,
    "fiyat":fiyat
}
id = input('id : ')
ad = input('ad : ')
fiyat = input('fiyat : ')
urunler [id] = {
    "ad":ad,
    "fiyat":fiyat
}

print(urunler)

aranacak = input("Aramak istediğiniz ürünün id'sini giriniz :")
urun = urunler[id]
print(f'id: {id}, ürün adı: {urun["ad"]}, ürün fiyatı: {urun["fiyat"]}')
