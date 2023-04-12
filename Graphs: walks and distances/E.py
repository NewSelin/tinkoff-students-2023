from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(100000)
n, m, s, t = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    b, e, w = map(int, input().split())
    g[b-1].append((e-1, w))
topsort = []
used = [False] * n
def dfs(u):
    used[u] = True
    if u in g.keys():
        for v, w in g[u]:
            if not used[v]:
                dfs(v)
    topsort.append(u)
for u in range(n):
    if not used[u]:
        dfs(u)
dist = [float("Inf")] * n
dist[s-1] = 0
while topsort:
    u = topsort.pop()
    for v, w in g[u]:
        dist[v] = min(dist[v], dist[u] + w)
if dist[t-1] == float("Inf"):
    print("Unreachable")
else:
    print(dist[t-1])