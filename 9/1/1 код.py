f = open('1 9 baza')
m = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    nepov = [x for x in a if a.count(x) == 1]
    if (a.count(a[-1]) == 3 and len(nepov) == 5) or (a.count(a[-1]) == 4 and len(nepov) == 4):
        if max(nepov) + min(nepov) <= sum(nepov[1:-1]):
            m+=1
print(m)
