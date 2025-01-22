spisok_filmiv = []

print("\n1. Додати фільм")
print("2. Показати список фільмів")
print("3. Видалити фільм")
print("4. Вихід")

вибір = input("Обери дію: ")

if вибір == "1":
    spisok_filmiv.append(input("Назва фільму: "))
    print("Фільм додано")
elif вибір == "2":
    print("Список фільмів:")
    print("1.", spisok_filmiv[0]) if len(spisok_filmiv) > 0 else None
    print("2.", spisok_filmiv[1]) if len(spisok_filmiv) > 1 else None
    print("3.", spisok_filmiv[2]) if len(spisok_filmiv) > 2 else None
elif вибір == "3":
  номер = int(input("Номер фільму: "))
  spisok_filmiv.pop(номер - 1)
  print("Фільм видалено.")
else:
  print("Невірна дія.")