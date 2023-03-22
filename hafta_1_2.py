#basit işlem

print('yaş karşılaştırma')
print('sen kaç yaşındasın?')
benimyas = input()

print('diğerinin yaş kaç')
digeri = input()
sonuc = int(benimyas) - int(digeri)
sonuc2 = int(digeri) - int(benimyas)
#artık sonucu yazdırmak gerek

if (benimyas < digeri):
    print('o senden büyük' + ' '+ str(sonuc2))

else:
    print('sen ondan büyüksün' + ' ' + str(sonuc))
