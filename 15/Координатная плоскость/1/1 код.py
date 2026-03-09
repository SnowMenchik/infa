m = []
t = 200
for a in range(-t, t):
    f = True
    for x in range(0, t + 1):
        for y in range(0, t + 1):
            if ((not(x <= 9) or (x**2 <= a)) and (not(y**2 <= a) or (y <= 9))) == False:
                f = False
    if f == True:
        m.append(a)
print(max(m))