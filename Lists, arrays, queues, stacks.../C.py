n = int(input())
l = list(map(int, input().split()))
stack = []
nl = list(range(n, 0, -1))
ans = []
c, m, t = 0, 0, 0
for i in l:
    stack.append(i)
    m += 1
    if i == nl[-1]:
        c += 1
        ans.append((1, m))
        m = 0
        while stack and stack[-1] == nl[-1]:
            t += 1
            stack.pop()
            nl.pop()
        c += 1
        ans.append((2, t))
        t = 0
if stack:
    print(0)
else:
    print(c)
    for j in ans:
        print(*j)
