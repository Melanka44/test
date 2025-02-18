import tkinter as tk
import random

def change_border_color():
    colors = ["red", "blue", "green", "purple", "orange", "pink", "yellow", "cyan"]
    button.config(highlightbackground=random.choice(colors), highlightcolor=random.choice(colors))

root = tk.Tk()
root.title("Змінюємо колір рамки")

button = tk.Button(root, text="Натисни мене!", command=change_border_color, font=("Arial", 14), padx=12, pady=6)
button.pack(pady=25)

root.mainloop()
