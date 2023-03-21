from collections import deque
n, k = map(int, input().split())
l = list(map(int, input().split()))
d = deque()
ans = list()
for i in range(n):
    while d and l[i] < d[-1]:
        d.pop()
    d.append(l[i])
    if i >= k and l[i-k] == d[0]:
        d.popleft()
    if i >= k-1:
        ans.append(d[0])
print(*ans)