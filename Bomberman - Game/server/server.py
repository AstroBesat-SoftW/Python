"""
Multiplayer Bomberman - Sunucu (server.py)
İki oyuncudan veri alır ve birbirlerine iletir.
"""

import socket
import threading
import json

clients = []
lock = threading.Lock()

def handle_client(conn, addr, player_id):
    print(f"[BAĞLANDI] Oyuncu {player_id} -> {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Gelen veriyi diğer oyunculara ilet
            with lock:
                for other_conn, other_id in clients:
                    if other_id != player_id:
                        try:
                            other_conn.sendall(data)
                        except:
                            pass
    except Exception as e:
        print(f"[HATA] Oyuncu {player_id}: {e}")
    finally:
        with lock:
            clients[:] = [(c, i) for c, i in clients if i != player_id]
        conn.close()
        print(f"[AYRILDI] Oyuncu {player_id}")

def start_server(host="0.0.0.0", port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(2)
    print(f"[SUNUCU] {host}:{port} adresinde dinleniyor...")

    player_id = 0
    while True:
        conn, addr = server.accept()
        with lock:
            clients.append((conn, player_id))
        t = threading.Thread(target=handle_client, args=(conn, addr, player_id), daemon=True)
        t.start()
        player_id += 1

if __name__ == "__main__":
    start_server()
