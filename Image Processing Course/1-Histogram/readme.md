# [cite_start]Görüntü İşleme Dersi [cite: 3]

[cite_start]**Yazar:** Besat ÇINGAR [cite: 4]  
[cite_start]**Ödev No:** Hafta 3 - Ödev 1 [cite: 4]

| Ödevler | Ödev Verilme Tarihi | Teslim Edilme Durumu |
| :--- | :--- | :--- |
| Histogram Eşitleme | Hafta 3 | [cite_start]Teslim Edildi | [cite: 128]

---

## [cite_start]Histogram Eşitleme Nedir? [cite: 5]

[cite_start]Histogram eşitleme (Histogram Equalization), sayısal görüntü işlemede sıkça kullanılan ve doğrudan piksellerin kendi değerleri üzerinde çalışan "noktasal" bir operasyondur[cite: 6]. 

[cite_start]Temel amacı, bir görüntüdeki piksellerin renk (gri seviye) dağılımını hesaplamak ve bu dağılımı matematiksel bir dönüşümle tüm alana daha homojen bir şekilde yaymaktır[cite: 7]. [cite_start]Bu işlem, görüntünün kümülatif dağılım fonksiyonu (CDF) üzerinden doğrusal olmayan bir dönüşüm gerçekleştirerek çalışır[cite: 8]. [cite_start]Bu sayede, görüntüde çok fazla bulunan (histogramda tepe yapan) piksel değerlerinin arası açılırken, daha az bulunan düşük olasılıklı piksel seviyeleri birbirine yaklaştırılır[cite: 9].

[cite_start]**Formül (Görsel 1):** [cite: 11]
[cite_start]$$cdf(v)=round(\frac{cdf(v)-cdf_{min}}{(M\times N)-cdf_{min}}\times(L-1))$$ [cite: 10]

**Yazılım (Python) Karşılığı:**
```python
cdf(v) = round(((cdf(v) - cdf_min) / (M*N - cdf_min)) * (L-1))
[cite_start]``` [cite: 12]

---

## [cite_start]Histogram Eşitlemeye Neden İhtiyaç Duyulur? [cite: 13]

* [cite_start]**Düşük Kontrastlı Görüntüleri İyileştirmek:** Sisli bir havada çekilmiş fotoğraflar veya aydınlatmanın yetersiz olduğu ortamlar, görüntünün piksel değerlerinin dar bir aralığa (örneğin sadece orta grilere) sıkışmasına neden olur[cite: 14]. [cite_start]Histogram eşitleme, bu dar alana sıkışmış pikselleri 0 (tam siyah) ile 255 (tam beyaz) aralığına dağıtarak imgedeki düşük görünürlüğü iyileştirir ve genel kontrastı artırır[cite: 15].
* [cite_start]**Otomatik Bir Süreç Olması:** Görüntü iyileştirme için kullanılan "Histogram Germe" (Stretching) işleminde sınırların kullanıcı tarafından belirlenmesi gerekirken; histogram eşitleme tamamen görüntünün kendi istatistiğine dayanan, dışarıdan parametre gerektirmeyen otomatik bir prosedürdür[cite: 49, 50].
* [cite_start]**Detayları Ortaya Çıkarmak:** Renk değerleri düzgün dağılımlı olmayan resimlerde birbirine çok yakın tonlar yüzünden kaybolan detaylar, bu işlemle belirginleşir[cite: 51, 52]. [cite_start]Bu yüzden özellikle medikal radyolojik görüntülerde veya endüstriyel analizlerde detayları yakalamak için kritik bir adımdır[cite: 53].

---

## Proje Çıktıları ve Kod

[cite_start]Aşağıda, düşük kontrastlı orijinal bir görüntünün ve histogram eşitleme işlemi uygulandıktan sonraki halinin karşılaştırmasını görebilirsiniz[cite: 16, 25, 48].


### [cite_start]Python Kodumuz (Görsel 3) [cite: 119]

[cite_start]*(Not: Buraya PDF'teki Görsel 3'te yer alan temiz Python kodunuzu yapıştırabilirsiniz[cite: 55].)*

```python
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Kodunuzun devamını buraya ekleyin...
