import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Music Player")
root.geometry("350x500")
root.configure(bg="#D8BFD8")

image = Image.open("MIZI.jpg")
image = image.resize((300, 300))
img = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=img, bg="#D8BFD8")
image_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#D8BFD8")
button_frame.pack()

prev_button = tk.Button(button_frame, text="⏮", font=("Arial", 14), width=5, bg="#E6C3E6")
prev_button.grid(row=0, column=0, padx=5)

play_pause_button = tk.Button(button_frame, text="⏸", font=("Arial", 14), width=5, bg="#E6C3E6")
play_pause_button.grid(row=0, column=1, padx=5)

next_button = tk.Button(button_frame, text="⏭", font=("Arial", 14), width=5, bg="#E6C3E6")
next_button.grid(row=0, column=2, padx=5)

menu_button = tk.Button(root, text="Menu", font=("Arial", 12), bg="#E6C3E6", width=10)
menu_button.pack(pady=5)

hearts_frame = tk.Frame(root, bg="#D8BFD8")
hearts_frame.pack()
for _ in range(3):
    heart_label = tk.Label(hearts_frame, text="💜", font=("Arial", 16), bg="#D8BFD8")
    heart_label.pack(side="left", padx=3)

root.mainloop()
