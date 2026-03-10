import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import minimum_filter, maximum_filter

# 1. Görüntüyü Siyah-Beyaz (Grayscale) Olarak Oku
# 'cameraman.tif' veya 'eight.tif' gibi derste geçen resimleri kullanabilirsin.
# Kendi bilgisayarındaki bir resmin yolunu buraya yazmalısın.
image_path = 'ornek_resim.jpg' 
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Lütfen geçerli bir resim yolu giriniz!")
else:
    # --- YARDIMCI FONKSİYON: Çizim için ---
    def plot_result(original, filtered, title):
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(original, cmap='gray')
        plt.title("Orijinal Görüntü")
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(filtered, cmap='gray')
        plt.title(title)
        plt.axis('off')
        plt.show()

    # ==========================================
    # LİNEER UZAYSAL FİLTRELER
    # ==========================================

    # 1. Ortalama (Average/Mean - Kutu) Filtresi (3x3)
    # Maske içindeki piksellerin ortalamasını alır.
    kernel_avg = np.ones((3, 3), np.float32) / 9
    avg_filtered = cv2.filter2D(img, -1, kernel_avg)
    plot_result(img, avg_filtered, "Ortalama (Average) Filtre (3x3)")

    # 2. Gaussian Filtresi (Ağırlıklı Ortalama)
    # Merkeze daha fazla ağırlık vererek bulanıklaştırma yapar.
    gaussian_filtered = cv2.GaussianBlur(img, (5, 5), 0)
    plot_result(img, gaussian_filtered, "Gaussian Filtre (5x5)")

    # 3. Sobel Filtresi (Kenar Bulma / Yüksek Geçiren)
    # Yatay ve dikey kenarları vurgular.
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)
    plot_result(img, sobel_combined, "Sobel Kenar Bulma Filtresi")


    # ==========================================
    # NON-LİNEER UZAYSAL FİLTRELER
    # ==========================================

    # 4. Minimum Filtresi (Min Operatörü)
    # Maske içindeki en küçük gri tonu merkeze atar.
    min_filtered = minimum_filter(img, size=3)
    plot_result(img, min_filtered, "Minimum (Min) Filtresi (3x3)")

    # 5. Maksimum Filtresi (Max Operatörü)
    # Maske içindeki en büyük gri tonu merkeze atar.
    max_filtered = maximum_filter(img, size=3)
    plot_result(img, max_filtered, "Maksimum (Max) Filtresi (3x3)")

    # 6. Median (Orta-Değer) Filtresi ve Gürültü Ekleme
    # Tuz-biber gürültüsünü temizlemede çok etkilidir.
    
    # Dersteki gibi önce resme "Salt & Pepper" (Tuz-Biber) gürültüsü ekleyelim
    noise_img = img.copy()
    row, col = noise_img.shape
    number_of_pixels = np.random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord=np.random.randint(0, row - 1)
        x_coord=np.random.randint(0, col - 1)
        noise_img[y_coord][x_coord] = 255 # Tuz (Beyaz)
    for i in range(number_of_pixels):
        y_coord=np.random.randint(0, row - 1)
        x_coord=np.random.randint(0, col - 1)
        noise_img[y_coord][x_coord] = 0   # Biber (Siyah)
        
    # Median filtresini gürültülü resme uygulayalım
    median_filtered = cv2.medianBlur(noise_img, 3)
    plot_result(noise_img, median_filtered, "Median (Orta-Değer) Filtresi (3x3)")
