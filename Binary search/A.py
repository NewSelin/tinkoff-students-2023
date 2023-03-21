n, k = map(int, input().split())
lst = list(map(int, input().split()))
arr = list(map(int, input().split()))
for i in arr:
    l = 0
    r = n-1
    while True:
        if lst[l] == i or lst[r] == i:
            print("YES")
            break
        elif l + 1 == r:
            print("NO")
            break
        s = (l + r) // 2
        if lst[s] <= i:
            l = s
        else:
            r = s