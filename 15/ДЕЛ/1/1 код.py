for a in range(1,1000):
    f = True
    for x in range(1, 1001):
        if not((x % a == 0) or ((x % 6 != 0) or (x % 4 != 0))):
            f = False
    if f:
        print(a)
#По условию берем максимальное, т.е. овтет 12