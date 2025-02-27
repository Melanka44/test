import mouse
import time
import keyboard
from PIL import Image
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("800x800")
window.title("Auto Clicker")
window.config(bg="#def6fa")

running = False

def start_clicker(): # для запуску автоклікера
    global running, delay
    try:
        clicks_per_second = int(entry.get())  #
        delay = 1 / clicks_per_second
        messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
        running = True
    except ValueError:
        messagebox.showerror("Помилка", "Введіть ціле число!")

def show_info(event):

    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

def exit_app():
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    window.destroy()

def on_hover(event):
    print("Ви навели мишку на картинку")

img = PhotoImage('chigiri our princess.jpg')
label = Label(window, image=img)
label.pack()

label.bind("<Enter>", on_hover)


Label(window, font=("", 24), text="Auto Clicker", bg="#def6fa", pady=10, fg="#027870").place(relx=0.5, rely=0.1, anchor="center")
Label(window, font=("", 14), text="Кліків на секунду:", bg="#def6fa", pady=10, fg="#027870").place(relx=0.5, rely=0.25, anchor="center")
entry = Entry(window, font=("", 16))
entry.place(relx=0.5, rely=0.3125, anchor="n")
Button(window, bg="#4dae4f", activebackground="#4dae4f", text="Почати", fg="white", command=start_clicker).place(relx=0.4, rely=0.5, anchor="center")
Button(window, bg="#f44132", activebackground="#f44132", text="Вийти", fg="white", command=exit_app).place(relx=0.6, rely=0.5, anchor="center")

click_label = Label(window, font=("", 14), text="Кліки: 0", bg="#def6fa", fg="#027870")
click_label.place(relx=0.5, rely=0.7, anchor="center")

window.bind("i", show_info)

keyboard.add_hotkey('esc', exit_app)

window.mainloop()
