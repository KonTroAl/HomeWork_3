def my_func(a, b, c):
    t = [a, b, c]
    max_1 = max(t)
    t.pop()
    max_2 = max(t)
    result = max_1 + max_2
    print(result)


my_func(23, 25, 48)
