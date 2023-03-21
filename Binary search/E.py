a, b, c, d = map(int, input().split())
def f(x):
    return a*x**3 + b*x**2 + c*x + d
if d >= 0:
    r = 0
    l = 1
    while f(l) >= 0:
        l *= -2
else:
    l = 0
    r = 1
    while f(r) < 0:
        r *= -2
while abs(f(r) - f(l)) >= 10**(-13):
    s = (l + r) / 2
    if s == l or s == r:
        break
    if f(s) < 0:
        l = s
    else:
        r = s
print(s)