import customtkinter as ctk

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("Калькулятор")
app.geometry("250*250")

def on_button_click(button):
    pass

def set_theme(theme):
    if theme == "light":
        app.configure(bg='white')
        display.configure(bg='lightgray', fg='black')
    elif theme == "dark":
        app.configure(bg='black')
        display.configure(bg='gray', fg='white')
    for button in buttons:
        button.configure(bg='lightgray' if theme == "light" else 'darkgray' if theme == "dark" else 'lightblue', fg='black' if theme != "dark" else 'white')

display = ctk.CTkEntry(app, font=("Arial", 24), width=150, justify='right')
display.pack(pady=10)

buttons_frame = ctk.CTkFrame(app)
buttons_frame.pack()

buttons = []
button_labels = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]
button_colors = ["red3", "orange red", "yellow2", "olive drab", "royalblue2", "purple1", "hotpink1", "aquamarine2", "coral", "maroon"]

for row in button_labels:
    row_frame = ctk.CTkFrame(buttons_frame)
    row_frame.pack()
    for label in row:
        color = button_colors[len(buttons) % len(button_colors)]
        button = ctk.CTkButton(row_frame, text=label, width=5, font=("Arial", 18), fg_color=color, command=lambda l=label: on_button_click(l))
        button.pack(side="left", padx=5, pady=5)
        buttons.append(button)

app.mainloop()

