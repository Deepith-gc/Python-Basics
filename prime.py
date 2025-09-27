for i in range(2, 11):
    a = 1
    c = 0
    while a <= i:
        if i % a == 0:
            c += 1
        a += 1
    if c == 2:
        print(i)

