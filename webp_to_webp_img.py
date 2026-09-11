from PIL import Image
import os

# Kaynak klasör (resimlerin olduğu klasör)
kaynak_klasor = "."

# Hedef klasör
hedef_klasor = "kaydedildi"
os.makedirs(hedef_klasor, exist_ok=True)

for i in range(1, 427):
    kaynak_dosya = os.path.join(kaynak_klasor, f"{i}.webp")
    hedef_dosya = os.path.join(hedef_klasor, f"{i}.webp")

    if not os.path.exists(kaynak_dosya):
        print(f"❌ {i}.webp bulunamadı, geçiliyor.")
        continue

    try:
        # WEBP dosyasını aç
        with Image.open(kaynak_dosya) as img:
            # Yeniden WEBP olarak kaydet
            img.save(
                hedef_dosya,
                format="WEBP",
                quality=80,      # İstersen 100 yapabilirsin.
                method=6          # En iyi WEBP sıkıştırma yöntemi.
            )

        # Yeni dosya oluşturulduysa eskiyi sil
        if os.path.exists(hedef_dosya):
            os.remove(kaynak_dosya)
            print(f"✅ {i}.webp dönüştürüldü ve eski dosya silindi.")

    except Exception as e:
        print(f"⚠️ {i}.webp hata: {e}")

print("\n🎉 Tüm işlem tamamlandı.")
