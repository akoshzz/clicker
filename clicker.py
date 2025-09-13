import tkinter as tk
from tkinter import messagebox

class Player:
    def __init__(self):
        self.score = 0

class Level:
    def __init__(self):
        self.level = 1

    def update(self, score):
        if score >= 20:
            self.level = 3
        elif score >= 10:
            self.level = 2
        else:
            self.level = 1
        return self.level

class Game:
    def __init__(self, root):
        self.root = root
        self.player = Player()
        self.level = Level()

        self.root.title("Clicker with levels")
        self.root.geometry("400x300")

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.level_label = tk.Label(root, text="Level: 1", font=("Arial", 14))
        self.level_label.pack(pady=10)

        self.button_click = tk.Button(root, text="Click Me", command=self.add_score)
        self.button_click.pack(pady=10)

        self.button_reset = tk.Button(root, text="Reset", command=self.reset)
        self.button_reset.pack(pady=10)

    def add_score(self):
        self.player.score += 1
        self.score_label.config(text=f"Score: {self.player.score}")
        old_level = self.level.level
        new_level = self.level.update(self.player.score)
        self.level_label.config(text=f"Level: {new_level}")
        if new_level != old_level:
            messagebox.showinfo("Level up!", f"You reached level {new_level}!")

    def reset(self):
        self.player.score = 0
        self.level.level = 1
        self.score_label.config(text="Score: 0")
        self.level_label.config(text="Level: 1")

root = tk.Tk()
game = Game(root)
root.mainloop()    