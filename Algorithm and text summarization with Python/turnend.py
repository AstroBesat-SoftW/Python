import os
import shutil

# Kaynak klasör ve hedef klasör yollarını belirleyin
kaynak_klasor_yolu = 'asama3/'
hedef_klasor_yolu = 'çıktı/'

# Hedef klasörü oluşturun (eğer yoksa)
if not os.path.exists(hedef_klasor_yolu):
    os.makedirs(hedef_klasor_yolu)

# Kaynak klasördeki tüm txt dosyalarını alın
txt_dosyalari = [dosya for dosya in os.listdir(kaynak_klasor_yolu) if dosya.endswith('.txt')]

# Tüm txt dosyalarını birleştirip özet.txt dosyasına kaydedin
with open(os.path.join(hedef_klasor_yolu, 'özet.txt'), 'w', encoding='utf-8') as hedef_dosya:
    for txt_dosya in txt_dosyalari:
        dosya_yolu = os.path.join(kaynak_klasor_yolu, txt_dosya)
        with open(dosya_yolu, 'r', encoding='utf-8') as kaynak_dosya:
            icerik = kaynak_dosya.read()
            hedef_dosya.write(icerik)
            hedef_dosya.write('\n')  # Dosyalar arasında bir satır boşluk bırakın

print("Tüm txt dosyaları başarıyla birleştirilip özet.txt dosyasına kaydedildi.")
