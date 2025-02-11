try:
    name = input("Назва задачі: ")
    category = input("Категорія: ")
    file = open("my_tasks.txt", "a")
    file.write(category)
    file.close()
    print(" Категорія збережена!")
except:
    print(" Помилочка! Не вдалося записати у файл.")

    