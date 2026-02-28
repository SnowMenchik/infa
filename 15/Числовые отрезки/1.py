def f(a,b,x):
    return a <= x < b

mx = 0

for a in range(0, 100):
    for b in range(a, 100):
        flag = True
        for i in range(2, 200):
            x = i / 2
            if (f(5, 30, x) == f(14, 23, x)) and f(a, b, x):
                flag = False
        if flag:
            mx = max(mx, b-a)
print(mx)