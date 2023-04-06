n, m = map(int, input().split())
lst = list(map(int, input().split()))
def f(n, i, l):
    if n == 0:
        return l
    if i == len(lst):
        return []
    new_l1 = f(n, i+1, l)
    new_l2,  new_l3 = [], []
    if n - lst[i] >= 0:
        new_l2 = f(n - lst[i], i+1, l + [lst[i]])
    if n - 2*lst[i] >= 0:
        new_l3 = f(n - 2*lst[i], i+1, l + [lst[i], lst[i]])
    ans = list(filter(lambda x: x, [new_l1, new_l2, new_l3]))
    if ans:
        return min(ans, key=lambda x: len(x))
    return ans


if 2*sum(lst) < n:
    print(-1)
else:
    l = f(n, 0, [])
    if l == []:
        print(0)
    else:
        print(len(l))
        print(*l)