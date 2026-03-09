cc = 1000001
a = [x for x in range(222, 1000000, 222) if all(i not in '13579' for i in str(x))]
b = [5**x for x in range(1, 20)]

ok = []

for i in a:
    for j in b:
        if i + j >= cc:
            ok.append([i + j, j])
            ok.sort()
for x, y in ok[:5]:
    print(x, y)
