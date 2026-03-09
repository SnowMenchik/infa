def f(x, y,s):
    if x==y and 'AA' not in s: return 1
    if x > y+5 or 'AA' in s: return 0
    return f(x-1, y, s + 'A') + f(x*2, y, s+'B') + f(x*3, y, s + 'C')
print(f(3, 15, ''))
