import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def apply_linear_filter(image, kernel):
    k_h, k_w = kernel.shape
    pad_h, pad_w = k_h // 2, k_w // 2
    
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    output_image = np.zeros_like(image, dtype=np.float64)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+k_h, j:j+k_w]
            output_image[i, j] = np.sum(region * kernel)
            
    return np.clip(output_image, 0, 255).astype(np.uint8)

def apply_nonlinear_filter(image, kernel_size, operator):
    pad = kernel_size // 2
    padded_image = np.pad(image, ((pad, pad), (pad, pad)), mode='constant', constant_values=0)
    output_image = np.zeros_like(image)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+kernel_size, j:j+kernel_size]
            
            if operator == 'min':
                output_image[i, j] = np.min(region)
            elif operator == 'max':
                output_image[i, j] = np.max(region)
            elif operator == 'median':
                output_image[i, j] = np.median(region)
                
    return output_image

image_list = [
    'kaynak_resmi.png', 
    'ortalama_filtre.png', 
    'gurultulu_resim_gaussian.png', 
    'median.png', 
    'median_2.png'
]

for filename in image_list:
    if not os.path.exists(filename):
        continue

    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    kernel_avg = np.ones((3, 3), np.float32) / 9.0
    avg_filtered = apply_linear_filter(img, kernel_avg)

    kernel_gaussian = np.array([[1, 2, 1],
                                [2, 4, 2],
                                [1, 2, 1]], dtype=np.float32) / 16.0
    gaussian_filtered = apply_linear_filter(img, kernel_gaussian)

    median_filtered_3x3 = apply_nonlinear_filter(img, 3, 'median')
    median_filtered_9x9 = apply_nonlinear_filter(img, 9, 'median')

    name, ext = os.path.splitext(filename)
    cv2.imwrite(f"{name}_sonuc_ortalama{ext}", avg_filtered)
    cv2.imwrite(f"{name}_sonuc_gaussian{ext}", gaussian_filtered)
    cv2.imwrite(f"{name}_sonuc_median3x3{ext}", median_filtered_3x3)
    cv2.imwrite(f"{name}_sonuc_median9x9{ext}", median_filtered_9x9)

    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 16))
    fig.suptitle(f"Goruntu: {filename}", fontsize=16, fontweight='bold')

    axes[0, 0].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[0, 0].set_title("Orijinal Goruntu")
    axes[0, 0].axis('off')
    axes[0, 1].imshow(avg_filtered, cmap='gray', vmin=0, vmax=255)
    axes[0, 1].set_title("Ortalama Filtre (3x3)")
    axes[0, 1].axis('off')

    axes[1, 0].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[1, 0].set_title("Orijinal Goruntu")
    axes[1, 0].axis('off')
    axes[1, 1].imshow(gaussian_filtered, cmap='gray', vmin=0, vmax=255)
    axes[1, 1].set_title("Gaussian Filtre (3x3)")
    axes[1, 1].axis('off')

    axes[2, 0].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[2, 0].set_title("Orijinal Goruntu")
    axes[2, 0].axis('off')
    axes[2, 1].imshow(median_filtered_3x3, cmap='gray', vmin=0, vmax=255)
    axes[2, 1].set_title("Median Filtre (3x3)")
    axes[2, 1].axis('off')

    axes[3, 0].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[3, 0].set_title("Orijinal Goruntu")
    axes[3, 0].axis('off')
    axes[3, 1].imshow(median_filtered_9x9, cmap='gray', vmin=0, vmax=255)
    axes[3, 1].set_title("Median Filtre (9x9)")
    axes[3, 1].axis('off')

    plt.tight_layout()
    plt.subplots_adjust(top=0.95) 
    plt.show()
