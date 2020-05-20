def my_func():
    result = 0
    num = 0
    while True:
        if input('Для выхода из программы нажимте "Q", для продолжения "Enter": ').upper() == 'Q':
            break
        num += 1
        n = input("Введите набор числе через пробел: ").split()
        b = []
        try:
            for i in range(len(n)):
                m = int(n[i])
                b.append(m)
            result_1 = sum(b)
            result += result_1
            print(f"Сумма ваших чисел равна: {result}")
        except ValueError:
            for i in range(len(n)):
                if n[i].upper() == 'Q':
                    result_1 = sum(b)
                    result += result_1
                    print(f"Сумма ваших чисел равна: {result}")
            break


my_func()
