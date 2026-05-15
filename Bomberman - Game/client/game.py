"""
Multiplayer Bomberman - İstemci (game.py)
Python + Pygame ile ağ üzerinden oynanabilen labirent oyunu.
"""

import pygame
import socket
import threading
import time
import json
import sys

# ─── KURULUM: IP ve OYUNCU NO SOR ──────────────────────────
print("=" * 52)
print("          MULTIPLAYER BOMBERMAN")
print("=" * 52)
print()
print("  SUNUCU BİLGİSAYAR KURULUMU:")
print("  1) server.py dosyasini calistir")
print("  2) CMD'ye  ipconfig  yaz")
print("  3) 'IPv4 Adresi' satirindaki adresi not al")
print()
print("  Ornek adres: 192.168.1.45")
print("-" * 52)

ip_girdi = input("Sunucu IP adresi [kendi bilgisayarinsa Enter]: ").strip()
HOST = ip_girdi if ip_girdi else "127.0.0.1"

print()
print("  Oyuncu secimi:")
print("  [1] 1. Oyuncu  (Sol ust kose - Mavi)")
print("  [2] 2. Oyuncu  (Sag alt kose - Kirmizi)")
print()

while True:
    secim = input("Oyuncu numaraniz (1 veya 2): ").strip()
    if secim in ("1", "2"):
        PLAYER_ID = int(secim) - 1
        break
    print("  Lutfen 1 veya 2 gir!")

PORT = 5555
print()
print(f"  Baglaniliyor -> {HOST}:{PORT}  |  Oyuncu {PLAYER_ID + 1}")
print("=" * 52)
print()

# ─── SABİTLER ───────────────────────────────────────────────
TILE = 64
FPS  = 60

DUVAR_RENK   = (60,  60,  80)
ZEMIN_RENK   = (200, 195, 180)
OYUNCU_RENK  = [(70, 130, 255), (255, 90, 70)]
BOMBA_RENK   = (30,  30,  30)
PATLAMA_RENK = (255, 160,  0)
ARKA_PLAN    = (30,  30,  40)

# ─── ADIM 2: HARİTA (IZGARA) SİSTEMİ ───────────────────────
game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

SATIR     = len(game_map)
SUTUN     = len(game_map[0])
GENISLIK  = SUTUN * TILE
YUKSEKLIK = SATIR * TILE + 60

BASLANGIC = [(1, 1), (SUTUN - 2, SATIR - 2)]


# ─── ADIM 4: BOMBA SINIFI ───────────────────────────────────
class Bomba:
    def __init__(self, gx, gy, patlama_zamani):
        self.gx = gx
        self.gy = gy
        self.patlama_zamani = patlama_zamani

    def patlamis_mi(self):
        return time.time() >= self.patlama_zamani

    def etkilenen_kareler(self, uzunluk=2):
        kareler = [(self.gx, self.gy)]
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            for i in range(1, uzunluk + 1):
                nx, ny = self.gx + dx * i, self.gy + dy * i
                if 0 <= ny < SATIR and 0 <= nx < SUTUN:
                    if game_map[ny][nx] == 1:
                        break
                    kareler.append((nx, ny))
        return kareler


# ─── OYUNCU SINIFI ──────────────────────────────────────────
class Oyuncu:
    def __init__(self, pid):
        self.pid   = pid
        bx, by     = BASLANGIC[pid]
        self.gx    = bx
        self.gy    = by
        self.canli = True

    # ─── ADIM 3: HAREKET ve ÇARPIŞMA ────────────────────────
    def hareket_et(self, dx, dy):
        nx, ny = self.gx + dx, self.gy + dy
        if 0 <= ny < SATIR and 0 <= nx < SUTUN:
            if game_map[ny][nx] != 1:
                self.gx = nx
                self.gy = ny

    def ciz(self, surface):
        if not self.canli:
            return
        renk = OYUNCU_RENK[self.pid]
        px = self.gx * TILE + TILE // 2
        py = self.gy * TILE + TILE // 2
        pygame.draw.circle(surface, renk, (px, py), TILE // 2 - 6)
        font = pygame.font.SysFont(None, 28)
        yazi = font.render(str(self.pid + 1), True, (255, 255, 255))
        surface.blit(yazi, (px - 7, py - 9))


# ─── ADIM 5: THREADING - PAYLAŞILAN DEĞİŞKENLER ────────────
dusmanx          = BASLANGIC[1 - PLAYER_ID][0]
dusmany          = BASLANGIC[1 - PLAYER_ID][1]
dusman_canli     = True
dusman_bombalari = []
lock             = threading.Lock()
client_socket    = None


def receive_data(sock):
    """ADIM 5: Alt thread — sadece veri günceller, çizim YOK!"""
    global dusmanx, dusmany, dusman_canli, dusman_bombalari
    buffer = ""
    while True:
        try:
            chunk = sock.recv(1024).decode("utf-8", errors="ignore")
            if not chunk:
                break
            buffer += chunk
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                if not line.strip():
                    continue
                try:
                    msg = json.loads(line)
                    with lock:
                        dusmanx      = msg.get("x", dusmanx)
                        dusmany      = msg.get("y", dusmany)
                        dusman_canli = msg.get("alive", dusman_canli)
                        if msg.get("bomb"):
                            bx, by = msg["bomb"]
                            dusman_bombalari.append(Bomba(bx, by, time.time() + 2))
                except json.JSONDecodeError:
                    pass
        except Exception:
            break


def gonder(sock, msg: dict):
    try:
        sock.sendall((json.dumps(msg) + "\n").encode())
    except Exception:
        pass


# ─── ANA DÖNGÜ ──────────────────────────────────────────────
def main():
    global client_socket, dusman_bombalari

    pygame.init()
    screen = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    pygame.display.set_caption(f"Bomberman — Oyuncu {PLAYER_ID + 1}")
    clock = pygame.time.Clock()

    # Sunucuya bağlan
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print(f"[BAĞLANTI] {HOST}:{PORT} sunucusuna bağlandı.")
    except Exception as e:
        print(f"\n[HATA] Sunucuya bağlanılamadı: {e}")
        print("Kontrol et: server.py çalışıyor mu? IP doğru mu?")
        input("Çıkmak için Enter'a bas...")
        pygame.quit()
        return

    # ADIM 5: Daemon thread başlat
    t = threading.Thread(target=receive_data, args=(client_socket,), daemon=True)
    t.start()

    oyuncu          = Oyuncu(PLAYER_ID)
    bombalar        = []
    patlamalar      = []
    son_hareket     = 0
    hareket_gecikme = 180

    font_bilgi = pygame.font.SysFont(None, 32)
    font_buyuk = pygame.font.SysFont(None, 72)

    running = True
    while running:
        clock.tick(FPS)

        # ── OLAYLAR ─────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and oyuncu.canli:
                if event.key == pygame.K_SPACE:
                    bombalar.append(Bomba(oyuncu.gx, oyuncu.gy, time.time() + 2))
                    gonder(client_socket, {
                        "x": oyuncu.gx, "y": oyuncu.gy,
                        "alive": oyuncu.canli,
                        "bomb": [oyuncu.gx, oyuncu.gy]
                    })

        # ── HAREKET (ADIM 3) ────────────────────────────────
        simdi = pygame.time.get_ticks()
        if oyuncu.canli and simdi - son_hareket > hareket_gecikme:
            keys = pygame.key.get_pressed()
            dx = dy = 0
            if keys[pygame.K_LEFT]  or keys[pygame.K_a]: dx = -1
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx =  1
            if keys[pygame.K_UP]    or keys[pygame.K_w]: dy = -1
            if keys[pygame.K_DOWN]  or keys[pygame.K_s]: dy =  1
            if dx or dy:
                oyuncu.hareket_et(dx, dy)
                son_hareket = simdi
                gonder(client_socket, {
                    "x": oyuncu.gx, "y": oyuncu.gy,
                    "alive": oyuncu.canli
                })

        # ── KENDİ BOMBALARIMIZ (ADIM 4) ─────────────────────
        yeni_bombalar = []
        for b in bombalar:
            if b.patlamis_mi():
                kareler = b.etkilenen_kareler()
                patlamalar.append((kareler, time.time() + 0.6))
                with lock:
                    if (dusmanx, dusmany) in kareler and dusman_canli:
                        pass
            else:
                yeni_bombalar.append(b)
        bombalar = yeni_bombalar

        # ── DÜŞMAN BOMBALARI ─────────────────────────────────
        with lock:
            yeni_db = []
            for b in dusman_bombalari:
                if b.patlamis_mi():
                    kareler = b.etkilenen_kareler()
                    patlamalar.append((kareler, time.time() + 0.6))
                    if (oyuncu.gx, oyuncu.gy) in kareler and oyuncu.canli:
                        oyuncu.canli = False
                        gonder(client_socket, {
                            "x": oyuncu.gx, "y": oyuncu.gy,
                            "alive": False
                        })
                else:
                    yeni_db.append(b)
            dusman_bombalari = yeni_db

        # Süresi dolan patlamaları temizle
        patlamalar = [(k, t) for k, t in patlamalar if time.time() < t]

        # ── ÇİZİM — SADECE ANA DÖNGÜDE! ─────────────────────
        screen.fill(ARKA_PLAN)

        # ADIM 2: Haritayı çiz (iç içe for döngüsü)
        for gy in range(SATIR):
            for gx in range(SUTUN):
                rect = pygame.Rect(gx * TILE, gy * TILE, TILE, TILE)
                if game_map[gy][gx] == 1:
                    pygame.draw.rect(screen, DUVAR_RENK, rect)
                    pygame.draw.rect(screen, (80, 80, 100), rect, 2)
                else:
                    pygame.draw.rect(screen, ZEMIN_RENK, rect)
                    pygame.draw.rect(screen, (180, 175, 160), rect, 1)

        # Patlamaları çiz
        patlayan_kareler = set()
        for kareler, _ in patlamalar:
            for kare in kareler:
                patlayan_kareler.add(kare)
        for (gx, gy) in patlayan_kareler:
            rect = pygame.Rect(gx * TILE + 4, gy * TILE + 4, TILE - 8, TILE - 8)
            pygame.draw.rect(screen, PATLAMA_RENK, rect, border_radius=8)

        # Bombaları çiz — snapshot al, sonra çiz (thread-safe)
        with lock:
            db_snap = list(dusman_bombalari)

        for b in bombalar:
            cx = b.gx * TILE + TILE // 2
            cy = b.gy * TILE + TILE // 2
            kalan = max(0, b.patlama_zamani - time.time())
            r = int(10 + 8 * (1 - kalan / 2))
            pygame.draw.circle(screen, BOMBA_RENK, (cx, cy), r)
            pygame.draw.circle(screen, (80, 80, 80), (cx, cy), r, 2)

        for b in db_snap:
            cx = b.gx * TILE + TILE // 2
            cy = b.gy * TILE + TILE // 2
            kalan = max(0, b.patlama_zamani - time.time())
            r = int(10 + 8 * (1 - kalan / 2))
            pygame.draw.circle(screen, (50, 50, 50), (cx, cy), r)
            pygame.draw.circle(screen, (100, 100, 100), (cx, cy), r, 2)

        # Oyuncuları çiz
        oyuncu.ciz(screen)

        with lock:
            dx_snap, dy_snap, dc_snap = dusmanx, dusmany, dusman_canli
        if dc_snap:
            renk = OYUNCU_RENK[1 - PLAYER_ID]
            cx = dx_snap * TILE + TILE // 2
            cy = dy_snap * TILE + TILE // 2
            pygame.draw.circle(screen, renk, (cx, cy), TILE // 2 - 6)
            font_num = pygame.font.SysFont(None, 28)
            yazi = font_num.render(str(2 - PLAYER_ID), True, (255, 255, 255))
            screen.blit(yazi, (cx - 7, cy - 9))

        # Bilgi çubuğu
        bilgi_y = SATIR * TILE + 10
        durum = f"Oyuncu {PLAYER_ID + 1}  |  WASD / Ok tusları: Hareket  |  SPACE: Bomba"
        screen.blit(font_bilgi.render(durum, True, (220, 220, 220)), (10, bilgi_y))

        # Oyun sonu mesajı
        if not oyuncu.canli:
            yazi = font_buyuk.render("KAYBETTIN!", True, (255, 60, 60))
            screen.blit(yazi, (GENISLIK // 2 - yazi.get_width() // 2, YUKSEKLIK // 2 - 40))
        elif not dc_snap:
            yazi = font_buyuk.render("KAZANDIN!", True, (60, 255, 120))
            screen.blit(yazi, (GENISLIK // 2 - yazi.get_width() // 2, YUKSEKLIK // 2 - 40))

        pygame.display.flip()

    client_socket.close()
    pygame.quit()


if __name__ == "__main__":
    main()
