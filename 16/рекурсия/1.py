from functools import *
@lru_cache(None)
def f(n):
    if n == 0:
        return 1
    if n>0  and n % 2 !=0:
        return f(n//100) * (n%10)
    if n >0 and n %2 ==0:
        return f(n//100)

for i in range(1234, 12345):
    f(i)
print(f(1239) - f(123))
