# PNG dosyasının sonuna gizli mesaj eklemek için Python kodu

def png_dosyasina_gizli_mesaj_ekle(png_dosya, mesaj, cikti_dosya):
    try:
        # Orijinal PNG dosyasını oku
        with open(png_dosya, "rb") as dosya:
            veri = dosya.read()
        
        # Mesajı PNG dosyasının sonuna ekle
        mesaj_bayt = mesaj.encode("utf-8")  # Mesajı byte formatına çevir
        yeni_veri = veri + b"\n" + mesaj_bayt
        
        # Yeni dosyayı kaydet
        with open(cikti_dosya, "wb") as cikti:
            cikti.write(yeni_veri)
        
        print(f"Gizli mesaj başarıyla eklendi! Yeni dosya: {cikti_dosya}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Kullanım
png_dosyasina_gizli_mesaj_ekle(
    png_dosya="1.png",  # Orijinal PNG dosyanızın adı
    mesaj="3000 love you <3 Kanala abone olllllunnn",  # Eklemek istediğiniz gizli mesaj
    cikti_dosya="gizli_mesaj_ekli.png"  # Yeni dosyanın adı
)
