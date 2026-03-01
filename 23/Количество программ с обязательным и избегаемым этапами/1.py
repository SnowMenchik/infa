from functools import *

@lru_cache(None)

def f(a, b, not_number):
    if a == b:
        return 1
    elif a > b or a == not_number:
        return 0
    else:
        return (f(a + 1, b, not_number) + f(a + 2, b, not_number) + f(a + 4, b, not_number) + f(a + 8, b, not_number))
    
#Траектория содержит 24, но не содержит 32
ans1 = f(16,24,32) * f(24,48,32)
#Траектория содержит 32, но не содержит 24
ans2 = f(16, 32, 24) * f(32, 48, 24)
print(ans1 + ans2)
