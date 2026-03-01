def f(x, y):
    if x==y: return 1
    if x>y +1 or x%3 ==0: return 0
    return f(x-1, y) + f(x+3, y) + f(x*2, y)
print(f(5, 100))
