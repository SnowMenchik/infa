from functools import *

@lru_cache(None)
def f(x, y, num):
    if x==y: return 1
    if x < y or x ==num: return 0
    return f(x-1, y, num) + f(x-3, y, num) + f(x//3, y, num)

# 40 30 не содержит 20
# 30 20 не содержит 40
# 40 20 не содержит 30

a = f(49, 40, 20) * f(40, 30, 20) * f(30, 12, 20)
b = f(49, 30, 40) * f(30, 20, 40) * f(20, 12, 40)
c = f(49, 40, 30) * f(40, 20, 30) * f(20, 12, 30)
d = f(49, 40, -2) * f(40, 30, -1) * f(30, 20, -1) *f(20, 12, -1)
print(a+ b+ c +d)
