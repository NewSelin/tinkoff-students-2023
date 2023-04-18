from sys import setrecursionlimit
setrecursionlimit(100000)
n = int(input())
weights = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(lst[0]):
        g[i].append(lst[j+1]-1)
topsort = []
used = [False] * n
def dfs(v):
    used[v] = True
    for u in g[v]:
        if not used[u]:
            dfs(u)
    topsort.append(v+1)
dfs(0)
print(sum(map(lambda v: weights[v-1], topsort)), len(topsort))
print(*topsort)