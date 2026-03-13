# scoreboard.py - En yüksek skorları dosyaya kaydeder (Bonus özellik)

import json
import os

SCORES_FILE = "highscores.json"
MAX_ENTRIES = 5  # En fazla kaç skor saklanacak


def load_scores():
    """Kaydedilmiş skorları dosyadan yükler. Dosya yoksa boş liste döner."""
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_score(player_name, score, treasures_found, moves):
    """Yeni bir skoru kaydeder. Sadece en yüksek MAX_ENTRIES skoru saklar."""
    scores = load_scores()
    new_entry = {
        "name": player_name,
        "score": score,
        "treasures": treasures_found,
        "moves": moves
    }
    scores.append(new_entry)
    # Puana göre azalan sırada sırala
    scores.sort(key=lambda x: x["score"], reverse=True)
    # Sadece en iyi MAX_ENTRIES skoru tut
    scores = scores[:MAX_ENTRIES]

    try:
        with open(SCORES_FILE, "w", encoding="utf-8") as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)
    except IOError:
        pass  # Kayıt yapılamazsa sessizce geç

    return scores


def get_top_scores():
    """En yüksek skorları döner."""
    return load_scores()


def format_scores_text():
    """Skorları okunabilir metin formatında döner."""
    scores = load_scores()
    if not scores:
        return "Henüz kayıtlı skor yok."

    lines = ["🏅 EN YÜKSEK SKORLAR\n" + "─" * 30]
    for i, entry in enumerate(scores, 1):
        lines.append(
            f"{i}. {entry['name']:<12} {entry['score']:>5} puan  "
            f"({entry['treasures']} hazine, {entry['moves']} hamle)"
        )
    return "\n".join(lines)
