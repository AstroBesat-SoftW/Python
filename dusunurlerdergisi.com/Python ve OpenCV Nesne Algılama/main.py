import cv2
import os
import numpy as np

def find_and_print_similarities(camera, image_folder):
    # Resim klasöründeki tüm .jpg uzantılı dosyaların yollarını al
    image_paths = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(".jpg")]

    matched_images = set()  # Eşleşen resim dosyalarının adlarını saklamak için bir küme oluştur

    while True:
        ret, frame = camera.read()  # Kameradan bir kare al
        if not ret:
            break

        frame_height, frame_width, _ = frame.shape  # Kare boyutlarını al

        # Göstermek istediğiniz ekran genişliği ve yüksekliğini tanımlayın
        display_width, display_height = 640, 480

        # Kareyi istenilen boyuta yeniden boyutlandır
        frame_resized = cv2.resize(frame, (display_width, display_height))

        # Daha iyi eşleme için yeniden boyutlandırılan kareyi gri tonlamalı hale getir
        frame_gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

        match_found = False

        for image_path in image_paths:
            # Şablon eşleme için resmi gri tonlamalı olarak oku
            template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Şablonu yeniden boyutlandırılmış kare boyutuna getir
            template_resized = cv2.resize(template, (display_width, display_height))

            # Şablon eşleme işlemini gerçekleştir
            res = cv2.matchTemplate(frame_gray, template_resized, cv2.TM_CCOEFF_NORMED)
            threshold = 0.1  # Eşleşme eşiğini belirleyin
            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                match_found = True
                image_name = os.path.basename(image_path)
                if image_name not in matched_images:
                    # Eğer eşleşen resmin adı daha önce yazdırılmadıysa
                    print("Bulundu:", image_name)
                    matched_images.add(image_name)

        if not match_found:
            print("Bulunamadı")

        # Yeniden boyutlandırılmış kareyi göster
        cv2.imshow("Kamera", frame_resized)

        # Kullanıcı 'q' tuşuna basarsa döngüyü sonlandır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamera serbest bırak
    camera.release()
    # Tüm pencereleri kapat
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Yerel kameradan görüntü almak için 0'ı kullanın
    camera = cv2.VideoCapture(0)
    image_folder = "images/"  # Resim klasörü yolunu güncelleyin
    find_and_print_similarities(camera, image_folder)
