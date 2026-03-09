from functools import *
@lru_cache(None)

def f(x, y):
    if x == y: return 1
    if x > y: return 0
    return f(x*2, y) + f(x**2, y) + f(x**3, y)
print(f(2, 131072) - (f(2, 4) * f(4, 16) * f(16, 131072)))