print("Кулькулятор")
print("1. Сложить")
print("2. Вычесть")
print("3. Умножить")
print("4. Выход")
chisl = 0
while chisl != "4":
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
        print("Выход...")

    else:
        print("Такого нет")