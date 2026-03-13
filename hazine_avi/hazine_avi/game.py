# game.py - Oyun kurallarını ve mantığını içerir

from map_generator import (
    generate_map, count_treasures, get_hint_message,
    TREASURE, TRAP, HINT, EMPTY
)
from player import Player

# Puan tablosu
SCORE_TABLE = {
    TREASURE: 10,
    TRAP: -5,
    HINT: 0,
    EMPTY: 0
}

# Maksimum hamle sayısı (oyun sonu koşulu)
MAX_MOVES = 30


class Game:
    def __init__(self, map_size=5):
        self.map_size = map_size
        self.game_map = []
        self.player = Player(0, 0)
        self.total_treasures = 0
        self.found_treasures = 0
        self.is_over = False
        self.message = ""
        self.on_update = None  # GUI güncelleme callback'i

    def new_game(self):
        """Yeni bir oyun başlatır."""
        self.game_map = generate_map(self.map_size)
        self.player.reset(self.map_size)
        self.total_treasures = count_treasures(self.game_map)
        self.found_treasures = 0
        self.is_over = False
        self.message = "🗺️ Oyun başladı! Hazineleri bul!"
        # Başlangıç hücresini işle
        self._process_cell(0, 0)

    def move_player(self, direction):
        """
        Oyuncuyu hareket ettirir ve hücre etkisini uygular.
        Sonuç mesajını döner.
        """
        if self.is_over:
            return "Oyun bitti! Yeni oyun başlatın."

        moved = self.player.move(direction, self.map_size)
        if not moved:
            self.message = "⚠️ Bu yöne gidemezsiniz!"
            return self.message

        row, col = self.player.get_position()
        self._process_cell(row, col)
        self._check_game_over()
        return self.message

    def _process_cell(self, row, col):
        """Hücre türüne göre etki uygular."""
        cell = self.game_map[row][col]

        # Hücreyi ortaya çıkar
        cell["revealed"] = True

        cell_type = cell["type"]

        if cell_type == TREASURE:
            self.player.add_score(SCORE_TABLE[TREASURE])
            self.found_treasures += 1
            cell["type"] = EMPTY  # Hazine alındı, boş yap
            self.message = f"🏆 Hazine buldun! +{SCORE_TABLE[TREASURE]} puan!"

        elif cell_type == TRAP:
            self.player.add_score(SCORE_TABLE[TRAP])
            cell["type"] = EMPTY  # Tuzak tetiklendi
            self.message = f"💥 Tuzağa düştün! {SCORE_TABLE[TRAP]} puan!"

        elif cell_type == HINT:
            hint_msg = get_hint_message(self.game_map, row, col, self.map_size)
            self.message = hint_msg
            cell["type"] = EMPTY  # İpucu kullanıldı

        else:
            self.message = "Boş bir alan. Devam et!"

    def _check_game_over(self):
        """Oyun bitiş koşullarını kontrol eder."""
        # Tüm hazineler bulundu mu?
        if self.found_treasures >= self.total_treasures:
            self.is_over = True
            self.message = f"🎉 Tebrikler! Tüm hazineleri buldun! Toplam puan: {self.player.score}"
            return

        # Hamle sınırına ulaşıldı mı?
        if self.player.moves >= MAX_MOVES:
            self.is_over = True
            remaining = self.total_treasures - self.found_treasures
            self.message = (
                f"⏰ Hamle hakkın bitti! {remaining} hazine kaldı. "
                f"Toplam puan: {self.player.score}"
            )

    def get_remaining_moves(self):
        """Kalan hamle sayısını döner."""
        return MAX_MOVES - self.player.moves

    def get_state(self):
        """Oyunun mevcut durumunu bir dict olarak döner."""
        return {
            "map": self.game_map,
            "player_pos": self.player.get_position(),
            "score": self.player.score,
            "moves": self.player.moves,
            "remaining_moves": self.get_remaining_moves(),
            "found_treasures": self.found_treasures,
            "total_treasures": self.total_treasures,
            "is_over": self.is_over,
            "message": self.message
        }
