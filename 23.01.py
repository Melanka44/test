spisok_filmiv = []

print("\n1. Додати фільм")
print("2. Вивести список фільмів")
print("3. Видалити фільм")
print("4. Вихід")

вибір = input("Оберіть дію: ")

if вибір == "1":
    spisok_filmiv.append(input("Назва фільму: "))
    print("Фільм добавлено")
elif вибір == "2":
    print("Список фільмів:")
    if len(spisok_filmiv) > 0:
        print("1.", spisok_filmiv[0])
    if len(spisok_filmiv) > 1:
        print("2.", spisok_filmiv[1])
    if len(spisok_filmiv) > 2:
        print("3.", spisok_filmiv[2])
elif вибір == "3":
    номер = int(input("Номер фільму: "))
    spisok_filmiv.pop(номер - 1)
    print("Фільм видалено.")
else:
    print("Невірна дія.")
