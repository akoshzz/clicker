import tkinter as tk
root = tk.Tk()
root.title("Clicker akoshzz")
root.geometry("300x200")
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack(pady=10)

button = tk.Button(root, text="Click Me")
button.pack(pady=10)

root.mainloop()

class Player:
    def __init__(self):
        self.score=0
def add_score():
    Player.score +=1
    score_label.config(text=f"Score: {Player.score}")


    