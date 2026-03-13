# gui.py - Grafik arayüz

import tkinter as tk
from tkinter import messagebox, simpledialog

from game import Game, MAX_MOVES
from scoreboard import save_score, format_scores_text

CELL = 60

class GameGUI:
    def __init__(self, root, map_size=5):
        self.root = root
        self.map_size = map_size
        self.game = Game(map_size)
        self.timer_running = False
        self.elapsed_time = 0
        self.timer_id = None

        self.root.title("Hazine Avi")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        self._build_ui()
        self._bind_keys()
        self.start_new_game()

    def _build_ui(self):
        # Baslik
        tk.Label(self.root, text="Hazine Avi Oyunu",
                 font=("Arial", 16, "bold"), bg="white").pack(pady=8)

        # Puan ve hamle bilgisi
        info = tk.Frame(self.root, bg="white")
        info.pack()
        self.score_var = tk.StringVar()
        self.moves_var = tk.StringVar()
        self.time_var  = tk.StringVar()
        tk.Label(info, text="Puan:", bg="white", font=("Arial", 11)).grid(row=0, column=0, padx=6)
        tk.Label(info, textvariable=self.score_var, bg="white", font=("Arial", 11, "bold")).grid(row=0, column=1, padx=6)
        tk.Label(info, text="Kalan Hamle:", bg="white", font=("Arial", 11)).grid(row=0, column=2, padx=6)
        tk.Label(info, textvariable=self.moves_var, bg="white", font=("Arial", 11, "bold")).grid(row=0, column=3, padx=6)
        tk.Label(info, text="Sure:", bg="white", font=("Arial", 11)).grid(row=0, column=4, padx=6)
        tk.Label(info, textvariable=self.time_var, bg="white", font=("Arial", 11, "bold")).grid(row=0, column=5, padx=6)

        # Harita (matematiksel matris gorunumu)
        map_frame = tk.Frame(self.root, bg="white")
        map_frame.pack(pady=8)

        # Sol koşeli parantez
        tk.Label(map_frame, text="⎡\n⎢\n⎢\n⎢\n⎣",
                 font=("Courier New", 22), bg="white", fg="black").grid(row=0, column=0)

        # Hucre grid
        grid = tk.Frame(map_frame, bg="white")
        grid.grid(row=0, column=1, padx=2)

        self.cells = []
        for r in range(self.map_size):
            row = []
            for c in range(self.map_size):
                lbl = tk.Label(grid, text=" ", width=3, height=1,
                               font=("Courier New", 14, "bold"),
                               bg="lightgray", relief="solid", bd=1)
                lbl.grid(row=r, column=c, padx=2, pady=2)
                row.append(lbl)
            self.cells.append(row)

        # Sag koşeli parantez
        tk.Label(map_frame, text="⎤\n⎥\n⎥\n⎥\n⎦",
                 font=("Courier New", 22), bg="white", fg="black").grid(row=0, column=2)

        # Yon butonlari
        btn_frame = tk.Frame(self.root, bg="white")
        btn_frame.pack(pady=6)
        tk.Button(btn_frame, text="↑", width=4, command=lambda: self.handle_move("up"),
                  font=("Arial", 12)).grid(row=0, column=1, padx=3, pady=3)
        tk.Button(btn_frame, text="←", width=4, command=lambda: self.handle_move("left"),
                  font=("Arial", 12)).grid(row=1, column=0, padx=3, pady=3)
        tk.Button(btn_frame, text="↓", width=4, command=lambda: self.handle_move("down"),
                  font=("Arial", 12)).grid(row=1, column=1, padx=3, pady=3)
        tk.Button(btn_frame, text="→", width=4, command=lambda: self.handle_move("right"),
                  font=("Arial", 12)).grid(row=1, column=2, padx=3, pady=3)

        # Mesaj alani
        self.msg_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.msg_var,
                 font=("Arial", 11), bg="white", fg="blue",
                 wraplength=400).pack(pady=4)

        # Alt butonlar
        alt = tk.Frame(self.root, bg="white")
        alt.pack(pady=6)
        tk.Button(alt, text="Yeni Oyun", command=self.start_new_game,
                  font=("Arial", 10), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(alt, text="Skorlar", command=self.show_scoreboard,
                  font=("Arial", 10), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(alt, text="Cikis", command=self.root.quit,
                  font=("Arial", 10), width=10).pack(side=tk.LEFT, padx=5)

    def _bind_keys(self):
        for key, d in [("<Up>","up"),("<Down>","down"),("<Left>","left"),("<Right>","right"),
                       ("<w>","up"),("<s>","down"),("<a>","left"),("<d>","right")]:
            self.root.bind(key, lambda e, d=d: self.handle_move(d))
        self.root.bind("<r>", lambda e: self.start_new_game())

    def start_new_game(self):
        self.game.new_game()
        self.elapsed_time = 0
        self._stop_timer()
        self._start_timer()
        self.refresh_ui()

    def handle_move(self, direction):
        if self.game.is_over:
            return
        self.game.move_player(direction)
        self.refresh_ui()
        if self.game.is_over:
            self._on_game_over()

    def refresh_ui(self):
        state = self.game.get_state()
        pr, pc = state["player_pos"]

        for r in range(self.map_size):
            for c in range(self.map_size):
                cell = state["map"][r][c]
                lbl = self.cells[r][c]

                if r == pr and c == pc:
                    lbl.config(text=" P ", bg="royalblue", fg="white")
                elif cell["revealed"]:
                    ct = cell["type"]
                    if ct == "treasure":
                        lbl.config(text=" T ", bg="gold", fg="black")
                    elif ct == "trap":
                        lbl.config(text=" X ", bg="tomato", fg="white")
                    elif ct == "hint":
                        lbl.config(text=" ? ", bg="skyblue", fg="black")
                    else:
                        lbl.config(text="   ", bg="white", fg="black")
                else:
                    lbl.config(text=" . ", bg="lightgray", fg="gray")

        self.score_var.set(str(state["score"]))
        self.moves_var.set(str(state["remaining_moves"]))
        self.msg_var.set(state["message"])

    def _start_timer(self):
        self.timer_running = True
        self._tick()

    def _tick(self):
        if self.timer_running:
            self.elapsed_time += 1
            m, s = divmod(self.elapsed_time, 60)
            self.time_var.set(f"{m:02d}:{s:02d}")
            self.timer_id = self.root.after(1000, self._tick)

    def _stop_timer(self):
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def _on_game_over(self):
        self._stop_timer()
        state = self.game.get_state()
        name = simpledialog.askstring(
            "Oyun Bitti",
            f"Puan: {state['score']}\nAdin nedir?",
            parent=self.root
        ) or "Anonim"
        save_score(name, state["score"], state["found_treasures"], state["moves"])
        messagebox.showinfo("Tamam", f"Skor kaydedildi!", parent=self.root)

    def show_scoreboard(self):
        win = tk.Toplevel(self.root)
        win.title("Skorlar")
        win.configure(bg="white")
        t = tk.Text(win, font=("Courier New", 10), width=40, height=10)
        t.insert(tk.END, format_scores_text())
        t.config(state=tk.DISABLED)
        t.pack(padx=10, pady=10)
        tk.Button(win, text="Kapat", command=win.destroy).pack(pady=5)
