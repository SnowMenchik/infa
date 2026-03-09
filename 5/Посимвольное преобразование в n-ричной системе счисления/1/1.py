def f(n, o):
    s = ''
    while n > 0:
        s= str(n%o) + s
        n//=o
    return s

a=[]
for n in range(1,1000, 2):
    r = f(n, 3)
    if n % 3 == 0:
        r = r + str(r[-2:])
    else:
        r = r + str(f(sum(map(int, r)) * 3, 3))
    if int(r, 3) > 208:
        a.append(int(r, 3))
print(min(a))
