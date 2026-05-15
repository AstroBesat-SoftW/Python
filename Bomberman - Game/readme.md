# 🎮 Çok Oyunculu Oyun - Kurulum ve Kullanım Kılavuzu

Bu proje, yerel ağ (LAN) üzerinden iki farklı bilgisayarın birlikte oynamasına olanak tanıyan bir yapıya sahiptir. Oyuna başlamadan önce lütfen aşağıdaki adımları sırasıyla takip edin.

<img width="524" height="450" alt="image" src="https://github.com/user-attachments/assets/96a7414f-4b9b-4b6c-95aa-2d600d65b22b" />

---

## ⚠️ Önemli Uyarı
Bağlantının kurulabilmesi için **her iki bilgisayarın da aynı Wi-Fi ağına bağlı olması** gerekmektedir.

---

## 🚀 Başlatma Adımları

### 1. Sunucu (Host) Bilgisayar İşlemleri
Oyunu kuracak (sunucu olacak) bilgisayarda:

1.  Önce terminal üzerinden `server.py` dosyasını çalıştırın:
    ```bash
    python server.py
    ```
2.  Ardından `game.py` dosyasını çalıştırın:
    ```bash
    python game.py
    ```
3.  Ekranda **Enter** tuşuna basın ve ardından kullanıcı seçiminizi yaparak beklemeye geçin.

### 2. İstemci (Diğer) Bilgisayar İşlemleri
Oyuna sonradan katılacak bilgisayarda:

1.  `game.py` dosyasını çalıştırın:
    ```bash
    python game.py
    ```
2.  Ekranda sizden bir IP adresi istenecektir. Sunucu bilgisayarın IP adresini buraya girin ve oyunu başlatın.

---

## 🔍 IP Adresimi Nasıl Öğrenirim?

Sunucu bilgisayarın IP adresini bulmak için:

1.  Sunucu bilgisayarda **CMD (Terminal)** ekranını açın.
2.  `ipconfig` yazıp Enter tuşuna basın.
3.  Çıkan sonuçlarda **IPv4 Address** yazan yerdeki bilgiyi (Örn: `192.168.1.45`) not alın. 
4.  Bu adresi, oyuna bağlanacak olan ikinci bilgisayara girmeniz gerekecektir.

---

## 🛠️ Bağlantı Sorunu Yaşıyorsanız (Güvenlik Duvarı)

Eğer ikinci bilgisayar bağlanamıyorsa, muhtemelen sunucu bilgisayarın güvenlik duvarı bağlantıyı engelliyordur. Geçici olarak çözmek için:

1.  **Windows Defender Güvenlik Duvarı** ayarlarına girin.
2.  Sol menüden **"Windows Defender Güvenlik Duvarı'nı etkinleştir veya devre dışı bırak"** kısmına tıklayın.
3.  **Ortak ağ ayarları** altındaki **"Windows Defender Güvenlik Duvarı'nı kapat"** seçeneğini işaretleyin.

> **Not:** Güvenliğiniz için oyun bittikten sonra bu ayarı tekrar eski haline (açık) getirmeniz önerilir.

---

## 💻 Gereksinimler
* Python 3.x
* Aynı yerel ağ (Wi-Fi) bağlantısı
