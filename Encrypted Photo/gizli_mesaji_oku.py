def png_dosyasindan_gizli_mesaj_oku(png_dosya):
    try:
        # PNG dosyasını oku
        with open(png_dosya, "rb") as dosya:
            veri = dosya.read()
        
        # Son satırı ayıkla
        son_mesaj = veri.split(b"\n")[-1].decode("utf-8")
        print(f"Gizli Mesaj: {son_mesaj}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Kullanım
png_dosyasindan_gizli_mesaj_oku("gizli_mesaj_ekli.png")
