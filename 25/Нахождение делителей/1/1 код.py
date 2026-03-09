def f(d, n):
    for d in range(2, int(n**0.5)+1):
        if n % d==0:
            return [d] + f(d, n //d)
    return [n]


k=0
for x in range(7305678, 7515678):
    if k==5: break
    m = f(2, x)
    if len(m) == 4 and str(sum(m)) == str(sum(m))[::-1]:
        print(x, sum(m))
        k+=1
