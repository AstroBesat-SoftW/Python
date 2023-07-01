#doğum günü kaydetme

dogumgunu = {'Besat': '20 Nisan', 'Eray': '11 Mart', 'Elif':'23 Ocak'}

#okuma işlemi
with open('1.ders.txt', 'r') as dosyaac:
    baglan = dosyaac.read()
    dogumgunu = eval(baglan)
  #  print(dogumgunu)

while True:
    print('isim gir: (çıkmak için -t- harfine bas)')
    isim = input()
    if isim == 't':
        break


    if isim in dogumgunu:
        with open('1.ders.txt', 'r') as dosyaac:
            baglan = dosyaac.read()
            dogumgunu = eval(baglan)
        
        print(dogumgunu[isim]+' doğum günü'+ isim)

    else:
        print('böyle isimde doğum günü kayıtlı değil'+isim)
        print('kayıt için doğum tarihini  gir')
        dogum = input()
        dogumgunu[isim] = dogum
        print('eklendi')
        dosyaac = open('1.ders.txt', 'w')
        dosyaac.write(str(dogumgunu))
        dosyaac.close
