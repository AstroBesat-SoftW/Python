import os

def split_text_into_parts(input_file, output_directory):
    # Metni oku
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Metni cümlelerine bölelim
    sentences = text.split('. ')  # Cümleler nokta ve boşlukla ayrılır varsayıldı.

    # Cümle sayısını ve 10 eşit parçaya bölecek adım miktarını hesapla
    total_sentences = len(sentences)
    step = total_sentences // 10

    for i in range(10):
        start = i * step
        end = (i + 1) * step if i < 9 else total_sentences
        part_sentences = sentences[start:end]

        # Parçayı oluştur ve son noktayı ekleyin
        part_text = '. '.join(part_sentences)
        if i < 9 and end < total_sentences:
            part_text += '.'
        
        # Parçayı ilgili klasöre kaydet
        output_file = os.path.join(output_directory, f"{i + 1}.txt")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(part_text)

if __name__ == "__main__":
    input_file = "add.txt"
    output_directory = "asama/"

    # Klasörü oluştur (eğer yoksa)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    split_text_into_parts(input_file, output_directory)
