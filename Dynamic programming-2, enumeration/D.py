n = int(input())
def f(lst, maxx, n):
    if n == 0:
        print(*lst)
        return
    for i in range(1, min(maxx, n)+1):
        lst.append(i)
        f(lst, i, n-i)
        lst.pop()
f([], n, n)