print("Кулькулятор")
print("1. Сложить")
print("2. Вычесть")
print("3. Умножить")
print("4. Поделить")
print("5. Выход")
chisl = 0
while chisl != "5":
    a = int(input("Первое число: "))
    b = int(input("Втоорое число: "))
    chisl = input("Выбери действие: ")
    if chisl == "1":
        print("Сложил: ", a+b)

    elif chisl == "2":
        print("Вычел: ", a-b)

    elif chisl == "3":
        print("Умножил: ", a*b)

    elif chisl == "4":
        print("Поделил: ", a/b)

    elif chisl == "5":
        print("Вышел (0)_(0)")

    else:
        print("Такого нет")