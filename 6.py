def int_func(n):
    b = []
    for i in n:
        b.append(i)
        if 97 <= ord(i) <= 122:
            print("".join(b).title())
        else:
            print("Error")




int_func("textа")