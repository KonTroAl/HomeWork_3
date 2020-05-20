def int_func(n):
    a = "R"
    for i in n:
        if ord(i) >= 122 or ord(i) <= 97:
            a = "Error"
            break
    if a != "Error":
        print(n.title())
    else:
        print(a)


int_func("text")
