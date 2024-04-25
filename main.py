import tkinter as tk
import subprocess
import sys

def run_game(game_file):
    subprocess.Popen([sys.executable, game_file])

def main():
    root = tk.Tk()
    root.title("Oyun Launcher")

    # Pencere boyutunu ayarlayalım
    root.geometry("750x750")

    # Başlık için yeni bir font ve büyük boyut
    title_label = tk.Label(root, text="Oyun Launcher", font=("Helvetica", 20))
    title_label.pack(pady=10)

    games = [
        ("Connect 4", "connect4.py"),
        ("Connect 4 against AI", "connect4withai.py"),
        ("2048 Oyunu","2048.py"),
        ("Sudoku","Sudoku.py"),
        ("Flappy Bird","FlappyBird.py"),
        ("Angry Birds" , "")
    ]

    # Butonları düzenli bir şekilde yerleştirelim
    for game_name, game_file in games:
        button = tk.Button(root, text=game_name, command=lambda file=game_file: run_game(file), width=20, height=2)
        button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    try:
        import numpy
        import pygame
    except ImportError:
        print("Gerekli modül(numpy ve pygame) yüklenemedi.")
    else:
        main()
