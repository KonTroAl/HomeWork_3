def my_func(arg_1, arg_2):
    try:
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        result = arg_1 / arg_2
        print(result)
    except ZeroDivisionError:
        print("Деление на 0 запрещено!")


n1 = input("Введите делимое число: ")
n2 = input("Введите делитель: ")
my_func(n1, n2)
