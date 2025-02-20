from tkinter import *
from tkinter import messagebox

def start_autoclicker():
    messagebox.showinfo("Auto Clicker", "Автоклікер запущено!")

root = Tk()
root.title("Auto Clicker")
root.geometry("400x300")

title_label = Label(root, text="Auto Clicker", font=("Arial", 20, "bold"), bg="#c3e6eb", fg="#00796f")
title_label.pack(pady=10)

clicks_label = Label(root, text="Кліків на секунду:", font=("Arial", 12), bg="#c3e6eb", fg="black")
clicks_label.pack()

clicks_entry = Entry(root, font=("Arial", 14), width=15, justify="center")
clicks_entry.pack(pady=5)

button_frame = Frame(root, bg="#c3e6eb")
button_frame.pack(pady=20)

start_button = Button(button_frame, text="Почати", font=("Arial", 12, "bold"),
                      bg="#3a913e", fg="white", width=10, height=2, command=start_autoclicker)
start_button.grid(row=0, column=0, padx=10)

exit_button = Button(button_frame, text="Вийти", font=("Arial", 12, "bold"),
                     bg="#eb4034", fg="white", width=10, height=2, command=root.destroy)
exit_button.grid(row=0, column=1, padx=10)

root.mainloop()
