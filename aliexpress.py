ürün = int(input("Ürünün Fiyatı: "))
vergi1 = ürün * 2//10
vergi = ürün * 2//10
vergi2 = vergi * 2//10
toplam = float(8.70 + vergi + vergi2 + ürün + vergi1 )
print(toplam)