# player.py - Oyuncu bilgilerini tutar

class Player:
    def __init__(self, start_row=0, start_col=0):
        """Oyuncuyu başlangıç konumuna yerleştir."""
        self.row = start_row
        self.col = start_col
        self.score = 0
        self.moves = 0
        self.visited = []  # Ziyaret edilen hücreler listesi

    def move(self, direction, map_size):
        """
        Oyuncuyu belirtilen yönde hareket ettirir.
        Harita sınırlarını kontrol eder.
        Geçerli hareket ise True, değilse False döner.
        """
        new_row = self.row
        new_col = self.col

        if direction == "up":
            new_row -= 1
        elif direction == "down":
            new_row += 1
        elif direction == "left":
            new_col -= 1
        elif direction == "right":
            new_col += 1

        # Sınır kontrolü
        if 0 <= new_row < map_size and 0 <= new_col < map_size:
            self.row = new_row
            self.col = new_col
            self.moves += 1
            self.visited.append((self.row, self.col))
            return True
        return False

    def add_score(self, points):
        """Oyuncunun puanını günceller."""
        self.score += points

    def get_position(self):
        """Oyuncunun mevcut konumunu döner."""
        return (self.row, self.col)

    def reset(self, map_size):
        """Oyuncuyu sıfırlar."""
        self.row = 0
        self.col = 0
        self.score = 0
        self.moves = 0
        self.visited = [(0, 0)]
