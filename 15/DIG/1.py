def dig(x, y):
    return str(x)[0] == str(y)[0]

for a in range(1, 100):
    res = 1
    for x in range(1, 100):
        res *= (not dig(x, 28) and dig(x, 47)) <= (x > a - 20)
        if not res:
            break
    if res:
        print(a)
