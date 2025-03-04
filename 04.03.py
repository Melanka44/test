
import customtkinter as ctk

def save_login():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        with open("logins.txt", "a") as file:
            file.write(f"{username}:{password}\n")
        result_label.configure(text=" Логін збережено!", text_color="green")
    else:
        result_label.configure(text=" Будь ласка, заповніть усі поля!", text_color="red")

window = ctk.CTk()
window.title("Сторінка логіна")
window.geometry("300x250")

label_title = ctk.CTkLabel(window, text="Вхід", font=("Arial", 20))
label_title.pack(pady=10)

label_username = ctk.CTkLabel(window, text="Логін:")
label_username.pack()
entry_username = ctk.CTkEntry(window, width=200)
entry_username.pack()

label_password = ctk.CTkLabel(window, text="Пароль:")
label_password.pack()
entry_password = ctk.CTkEntry(window, show="*", width=200)
entry_password.pack()
btn_login = ctk.CTkButton(window, text="Увійти", command=save_login, fg_color="#4CAF50")
btn_login.pack(pady=10)
result_label = ctk.CTkLabel(window, text="", text_color="red")
result_label.pack(pady=5)

window.mainloop()


