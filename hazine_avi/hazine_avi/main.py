# main.py - Programı başlatır

import tkinter as tk
from gui import GameGUI

def main():
    """Ana fonksiyon: pencereyi oluşturur ve oyunu başlatır."""
    root = tk.Tk()
    app = GameGUI(root, map_size=5)   # 5x5 harita
    root.mainloop()

if __name__ == "__main__":
    main()
