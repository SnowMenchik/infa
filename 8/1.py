from itertools import *
c = 0
for i in permutations('0234567', r=5):
    s = "".join(i)
    if  all((int(i[p]) % 2 == 0 and int(i[p+ 1]) % 2 != 0) or ((int(i[p + 1]) % 2 == 0 and int(i[p]) % 2 != 0)) for p in range(4)) and s[0] != '0':
        c += 1
print(c)