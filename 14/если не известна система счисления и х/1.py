for i in range(11, 36):
    n1 = int('29A1', i)
    n2 = int('47771', i)
    n3 = int('12A', i)
    for x in range(1, 500001):
        num = n1 + n2 + n3 - 1000000 - x
        if num ==0:
            print(i)
