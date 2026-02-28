import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('gorsel.png', 0)

if img is None:
    print("Hata: 'gorsel.png' bulunamadı! Lütfen dosya yolunu kontrol edin.")
else:
   
    M, N = img.shape
    total_pixels = M * N
    L = 256 # 8-bitlik (0-255)

    # 2. HİSTOGRAM HESAPLAMA
    # Her bir piksel değerinden (0-255 arası) kaç tane olduğunu buluyoruz
    histogram = np.zeros(256, dtype=int)
    for row in img:
        for p in row:
            histogram[p] += 1

 
    cdf = np.zeros(256, dtype=int)
    cdf[0] = histogram[0]
    for i in range(1, 256):
        cdf[i] = cdf[i-1] + histogram[i]

    
    cdf_min = 0
    for i in range(256):
        if cdf[i] > 0:
            cdf_min = cdf[i]
            break


    new_pixels = np.zeros(256, dtype=np.uint8)
    for v in range(256):
        if cdf[v] > 0:
            # Derste işlediğimiz formül: cdf(v) = round( ((cdf(v) - cdf_min) / (M*N - cdf_min)) * (L - 1) )
            numerator = cdf[v] - cdf_min
            denominator = total_pixels - cdf_min
            new_val = round((numerator / denominator) * (L - 1))
            new_pixels[v] = new_val

    equalized_img = new_pixels[img]

    

    plt.figure(figsize=(12, 6))

    
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.hist(img.flatten(), bins=256, range=[0,256], color='black')
    plt.title('Orijinal Histogram')

    plt.subplot(2, 2, 3)
    plt.imshow(equalized_img, cmap='gray', vmin=0, vmax=255)
    plt.title('Eşitlenmiş Görüntü')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.hist(equalized_img.flatten(), bins=256, range=[0,256], color='black')
    plt.title('Eşitlenmiş Histogram')

    plt.tight_layout()
    plt.show()
