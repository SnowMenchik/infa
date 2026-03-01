#  1 способ
from itertools import *
c = 0
for i in permutations('0234567', r=5):
    s = "".join(i)
    if  all((int(i[p]) % 2 == 0 and int(i[p+ 1]) % 2 != 0) or ((int(i[p + 1]) % 2 == 0 and int(i[p]) % 2 != 0)) for p in range(4)) and s[0] != '0':
        c += 1
print(c)

#  2 способ 
m = 0
for i in permutations('0234567', r = 5):
    num = ''.join(i)
    if num[0] != '0':
        num = num.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*').replace('1', '.').replace('3', '.').replace('5', '.').replace('7', '.')
        if  ('**' not in num) and  ('..' not in num):
            print(num)
            m += 1
print(m)
