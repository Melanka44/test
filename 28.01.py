print("Вводь числа для підсумовування. Напиши 0, щоб завершити.")
vsogo = 0
number = int(input("Введи число: "))
while number != 0:
    vsogo += number
    number = int(input("Введи наступне число: "))
print("Сума всіх чисел:", vsogo)