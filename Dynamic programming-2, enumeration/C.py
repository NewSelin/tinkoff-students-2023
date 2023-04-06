t = int(input())
fib = [1, 1]
temp = dict()
for _ in range(3, 90):
    fib.append(fib[-1] + fib[-2])
def f(x, i):
    if x == 1:
        return 1
    if i < 2:
        return 0
    if (x, i) in temp:
        return temp[(x, i)]
    if x % fib[i] == 0:
        temp[(x, i)] = f(x, i-1) + f(x//fib[i], i)
    else:
        temp[(x, i)] = f(x, i - 1)
    return temp[(x, i)]
for _ in range(t):
    m = int(input())
    j = 89
    for i in range(2, 90):
        if fib[i] >= m:
            j = i
            break
    print(f(m, j))