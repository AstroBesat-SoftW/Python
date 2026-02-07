# faktoriyel hesabı yapımı ders 4

# örnek kullanıcıdan girdi alalım
# kaç fakyoriyel hesaplamak istiyorsa
# hesaplayalım

a = input()
sayi =1
for i in range(a+1):
    sayi = sayi * i
    
print(sayi)

# örnek kullanıcı 3 girer
# range içinde a+1 desim yani 4 olur
# range en son kısmı almaz yani 3 e
# kadar almasını sağladık

# adım 1 
# sayi = 1*1
# adim 2
# sayi = 1*2

# şeklinde ilerler