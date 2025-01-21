import random

def randnumber():
    # Генеруємо випадкове число від 1 до 10
    randnumber = random.randint(1, 10)
    print("Я загадав число від 1 до 10. Спробуй його вгадати!")

    # Цикл працює до тих пір, поки бро не вгадає число
    while True:
        try:
             # бро вводить своє припущення
            user_guess = int(input("Введи своє число: "))

            # чекаєм чи правильне число
            if user_guess == randnumber:
                print("Вітаю! Ти вгадав число!")
                break  # Завершуємо гру
            elif user_guess < randnumber:
                print("Ні, загаданe число більше.")
            else:
                print("Ні, загаданe число менше.")
        except ValueError:
            # Якщо бро ввів не число, повідомляємо його про це
            print("Будь ласка, введи правильне число.")

# Викликаємо функцію гри
randnumber()
