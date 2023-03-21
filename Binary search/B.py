n, k = map(int, input().split())
lst = list(map(int, input().split()))
arr = list(map(int, input().split()))
for i in arr:
    l = 0
    r = n-1
    while True:
        if l + 1 == r:
            if i - lst[l] <= lst[r] - i:
                print(lst[l])
            else:
                print(lst[r])
            break
        s = (l + r) // 2
        if lst[s] <= i:
            l = s
        else:
            r = s