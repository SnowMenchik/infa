from itertools import *
c = 0
for t in range(1,11):
    for i in permutations(sorted('0123456789'), t):
        s = "".join(i)
        if s[0] != '0' and int(s) % 5 == 0 or s == '0':
            c += 1
print(c)