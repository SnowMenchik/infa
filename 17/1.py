f = open('17 baza')
a = [int(s) for s in f]
maxa = max([x**2 for x in a if len(str(abs(x)))==4 and abs(x)%100==43])
par = []
for i in range(len(a)-1):
    if (len(str(abs(a[i]))) ==4 or len(str(abs(a[i+1])))==4) :
        if (a[i] + a[i+1])**2 < maxa:
            par.append(a[i] + a[i+1])
print(len(par), max(par)**2)
