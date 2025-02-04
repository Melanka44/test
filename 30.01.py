print("Простий калькулятор. Введи 'вийти', щоб завершити.")
while True:
    number1 = input("Введи перше число: ")
    if number1.lower() == "вийти":
        break
    operator = input("Оберіть операцію (+, -, *, /): ")
    if operator.lower() == "вийти":
        break
    number2 = input("Введи друге число: ")
    if number2.lower() == "вийти":
        break
    if operator == "+":
        print("Результат:", int(number1) + int(number2))
    elif operator == "-":
        print("Результат:", int(number1) - int(number2))
    elif operator == "*":
        print("Результат:", int(number1) * int(number2))
    elif operator == "/":
        if number2 == "0":
            print("Помилка! Ділення на нуль.")
        else:
            print("Результат:", int(number1) // int(number2))
    else:
        print("Невідома операція.")