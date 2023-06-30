#kod ile txt dosyası oluşturp içine bir şeyler yazıcaz..

dosyaac = open('yazicine.txt', 'w') #dosya ismi
neyazsin = input('içinde ne yazsın \n ')
dosyaac.write(neyazsin) #içinde ne yazsın

dosyaac.close()

