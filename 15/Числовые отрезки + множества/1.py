def f(x, y):
    a = 6<=x<=46
    b = 161 % x ==0 and x not in [1, 161]
    c = y%x ==0 and x not in [1, y]
    return (not b and a) or (not(c))

for y in range(1, 10000):
    d = [i for i in range(2, y) if y%i==0]
    if d and all(f(x, y) for x in range(1, 10000)):
        print(y)
