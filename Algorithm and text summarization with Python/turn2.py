import os

# İlk klasör ve hedef klasörü belirtin
input_folder = 'asama/'
output_folder = 'asama2/'

# Hedef klasörü oluşturun (eğer yoksa)
os.makedirs(output_folder, exist_ok=True)

# Dosya sayısını belirtin (örneğin, 10 dosya)
file_count = 10

# Her dosya için işlem yapın
for i in range(1, file_count + 1):
    input_file_path = os.path.join(input_folder, f'{i}.txt')
    output_file_path = os.path.join(output_folder, f'{i}.txt')

    # Dosyayı okuyun
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    # Cümle sayısını hesaplayın
    sentence_count = len(lines)

    # İşlenecek cümle sayısını hesaplayın (%30'u)
    processed_sentence_count = max(1, int(sentence_count * 0.3))

    # İşlenmiş veriyi oluşturun
    processed_data = ''.join(lines[:processed_sentence_count])

    # İşlenmiş veriyi yeni dosyaya kaydedin
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(processed_data)

    print(f"{i}.txt dosyası işlendi ve kaydedildi.")
