from sys import setrecursionlimit
setrecursionlimit(100000)
n, m = map(int, input().split())
g = [[] for _ in range(n)]
g_inv = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g_inv[v-1].append(u-1)
topsort = []
used = [False] * n
def dfs(u):
    used[u] = True
    for v in g[u]:
        if not used[v]:
            dfs(v)
    topsort.append(u)
for u in range(n):
    if not used[u]:
        dfs(u)
topsort = topsort[::-1]
color = [0] * n
g_res = [set() for _ in range(n)]
def unite(v, c):
    color[v] = c
    for u in g_inv[v]:
        if color[u] == 0:
            unite(u, c)
        elif color[u] != c:
            g_res[color[u]].add(c)
c = 1
for v in topsort:
    if color[v] == 0:
        unite(v, c)
        c += 1
print(c-1)
print(*color)