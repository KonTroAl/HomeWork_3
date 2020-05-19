# version 1
"""
Для реализации данной версии необходимо было ввести дополнительную переменную,
которая бы запоминала значение предыдущей операции в цикле
"""


def my_func(x, y):
    b = 1
    i = 0
    while i < abs(y):
        result = (1 / x)
        i += 1
        b *= result
    print(b)


my_func(2, -3)


# version 2

def func(x, y):
    print(1 / (x ** abs(y)))


func(2, -3)
