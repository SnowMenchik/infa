def f(x):
    d = 2
    ok = []
    while d*d <= x:
        if x % d == 0:
            if d % 2 == 0:
                ok += [d]
        d += 1
    if len(ok) == 4:
        ok.sort()
        a = ok[-1]
        b = ok[-2]
        return a,b
for x in range(190201, 190261):
    if f(x) != None:
        print(f(x))