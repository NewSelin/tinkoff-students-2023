c = float(input())
def f(x):
    return x**2 + (x+1)**(1/2)
l = 0
r = 100000
while f(r) - f(l) >= 10**(-8):
    d = (l+r) / 2
    if d == l or d == r:
        break
    if f(d) < c:
        l = d
    else:
        r = d
print(d)