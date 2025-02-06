from easygui import *

filename = "hello.txt"

while True:
    choice = buttonbox(
        "Виберіть дію:",
        "Запис у файл",
        ["Додати", "Переглянути", "Видалити", "Вихід"]
    )

    if choice == "Вихід":
        break

    elif choice == "Додати":
        data = multenterbox(
            "Введіть свої дані:",
            "Запис у файл",
            ["Ім'я", "Хобі", "Улюблена їжа"]
        )

        if data:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"Ім'я: {data[0]}\n")
                file.write(f"Хобі: {data[1]}\n")
                file.write(f"Улюблена їжа: {data[2]}\n")

            msgbox("Дані успішно записані!", "Успіх")

    elif choice == "Переглянути":
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
            msgbox(content, "Вміст файлу")
        except FileNotFoundError:
            msgbox("Файл ще не створений!", "Помилка")

    elif choice == "Видалити":
        import os
        if os.path.exists(filename):
            os.remove(filename)
            msgbox("Файл видалено!", "Успіх")
        else:
            msgbox("Файл не існує!", "Помилка")