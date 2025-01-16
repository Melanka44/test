# Ініціалізація порожньої телефонної книги
phonebook = {}


# Функція для додавання або оновлення контакту
def add_contact(name, phone_number):
    phonebook[name] = phone_number
    print(f"Контакт {name} додано/оновлено.")


# Функція для пошуку контакту за ім'ям
def search_contact(name):
    if name in phonebook:
        print(f"Номер телефону для {name}: {phonebook[name]}")
    else:
        print(f"Контакт {name} не знайдено.")


# Функція для видалення контакту за ім'ям
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Контакт {name} видалено.")
    else:
        print(f"Контакт {name} не знайдено.")


# Функція для відображення меню
def show_menu():
    print("\nМеню Телефонної Книги:")
    print("1. Додати/оновити контакт")
    print("2. Пошук контакту")
    print("3. Видалити контакт")
    print("4. Вихід")


# Головне меню програми
def main():
    while True:
        show_menu()
        choice = input("Оберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я: ")
            phone_number = input("Введіть номер телефону: ")
            add_contact(name, phone_number)
        elif choice == '2':
            name = input("Введіть ім'я для пошуку: ")
            search_contact(name)
        elif choice == '3':
            name = input("Введіть ім'я для видалення: ")
            delete_contact(name)
        elif choice == '4':
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
