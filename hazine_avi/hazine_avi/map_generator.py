# map_generator.py - Haritayı rastgele oluşturur

import random

# Hücre türleri için sabitler
EMPTY = "empty"
TREASURE = "treasure"
TRAP = "trap"
HINT = "hint"

# Hücre sembolleri (görsel gösterim için)
SYMBOLS = {
    EMPTY:    "·",
    TREASURE: "T",
    TRAP:     "X",
    HINT:     "?",
    "player": "P",
    "fog":    " "   # Keşfedilmemiş hücre
}

# Hücre renkleri (tkinter için)
COLORS = {
    EMPTY:    "#d4edda",
    TREASURE: "#ffd700",
    TRAP:     "#f8d7da",
    HINT:     "#cce5ff",
    "player": "#6f42c1",
    "fog":    "#adb5bd"
}


def generate_map(size=5):
    """
    Belirtilen boyutta rastgele bir harita oluşturur.
    İki boyutlu liste (list of lists) döner.
    Her hücre bir dict'tir: {type, revealed}
    """
    # Önce tüm hücreleri boş yap
    game_map = []
    for r in range(size):
        row = []
        for c in range(size):
            row.append({"type": EMPTY, "revealed": False})
        game_map.append(row)

    total_cells = size * size
    # Başlangıç hücresi (0,0) her zaman boş ve görünür
    game_map[0][0]["revealed"] = True

    # Yerleştirme sayıları (toplam hücre miktarına göre oransal)
    num_treasures = max(3, total_cells // 6)
    num_traps = max(2, total_cells // 8)
    num_hints = max(3, total_cells // 7)

    # Yerleştirilen konumları takip et
    placed = {(0, 0)}  # Başlangıç noktasına bir şey koyma

    def place_items(item_type, count):
        """Haritaya belirli türde eleman yerleştirir."""
        placed_count = 0
        attempts = 0
        while placed_count < count and attempts < 200:
            r = random.randint(0, size - 1)
            c = random.randint(0, size - 1)
            if (r, c) not in placed:
                game_map[r][c]["type"] = item_type
                placed.add((r, c))
                placed_count += 1
            attempts += 1

    place_items(TREASURE, num_treasures)
    place_items(TRAP, num_traps)
    place_items(HINT, num_hints)

    return game_map


def count_treasures(game_map):
    """Haritadaki toplam hazine sayısını döner."""
    count = 0
    for row in game_map:
        for cell in row:
            if cell["type"] == TREASURE:
                count += 1
    return count


def get_hint_message(game_map, player_row, player_col, size):
    """
    Oyuncunun bulunduğu konuma göre en yakın hazinenin yönünü döner.
    """
    treasures = []
    for r in range(size):
        for c in range(size):
            if game_map[r][c]["type"] == TREASURE and not game_map[r][c]["revealed"]:
                treasures.append((r, c))

    if not treasures:
        return "Haritada keşfedilmemiş hazine kalmadı!"

    # En yakın hazineyi bul (Manhattan mesafesi)
    nearest = min(treasures, key=lambda t: abs(t[0] - player_row) + abs(t[1] - player_col))
    tr, tc = nearest
    dr = tr - player_row
    dc = tc - player_col

    directions = []
    if dr < 0:
        directions.append("yukarı")
    elif dr > 0:
        directions.append("aşağı")
    if dc < 0:
        directions.append("sola")
    elif dc > 0:
        directions.append("sağa")

    dist = abs(dr) + abs(dc)
    if directions:
        return f"💡 İpucu: En yakın hazine {' ve '.join(directions)} yönünde, ~{dist} adım uzakta!"
    return "💡 İpucu: Hazine tam bu hücrenin yakınında!"
