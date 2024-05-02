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
    title_label = tk.Label(root, text="MULTIGAME LAUNCHER ATARI by Ebubekir Kurt", font=("Helvetica", 20))
    title_label.pack(pady=10)

    games = [
        ("Connect 4", "connect4.py"),
        ("Connect 4 against AI", "connect4withai.py"),
        ("2048 Oyunu","2048.py"),
        ("Sudoku","Sudoku.py"),
        ("Flappy Bird","FlappyBird.py"),
        ("Angry Birds", "C:/Users/90541/PycharmProjects/OyunSkor/AngryBirdsOyunu/AngryBirds.py")
    ]

    # Butonları 2 sıra ve her sırada 3'er tane olacak şekilde düzenli bir şekilde yerleştirdik
    for i in range(0, len(games), 3):
        frame = tk.Frame(root)
        frame.pack()

        for j in range(3):
            index = i + j
            if index < len(games):
                game_name, game_file = games[index]
                button = tk.Button(frame, text=game_name, command=lambda file=game_file: run_game(file), width=20, height=2)
                button.grid(row=i, column=j, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    try:
        import numpy
        import pygame
    except ImportError:
        print("Gerekli modül(numpy) yüklenemedi.")
    else:
        main()
