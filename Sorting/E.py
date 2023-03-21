n = int(input())
l = [0] * n
arr = list(map(int, input().split()))
ans = [1]
m = 0
r = n-1
for e, i in enumerate(arr[:n-1]):
    l[i-1] = 1
    while l[r] == 1:
        m += 1
        r -= 1
    ans.append(e + 2 - m)
ans.append(1)
print(*ans)