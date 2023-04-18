from sys import setrecursionlimit
setrecursionlimit(100000)
n = int(input())
m = int(input())
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
g_res = [[] for _ in range(n+1)]
def unite(v, c):
    color[v] = c
    for u in g_inv[v]:
        if color[u] == 0:
            unite(u, c)
        elif color[u] != c:
            g_res[color[u]].append(c)
c = 1
for v in topsort:
    if color[v] == 0:
        unite(v, c)
        c += 1
def dfs2(v) :
    stock = color_new[v] = True
    for u in g_res[v]:
        if color_new[u] == 0:
            stock = False
            dfs2(u)
        if color_new[u] == 2 or color_new[u] == 1:
            color_new[v] = 2
            break
    if color_new[v] == True and stock:
        color_new[v] = 1
color_new = [0] * c
for i in range(1, c):
    if not color_new[i]:
        dfs2(i)
print(color_new.count(1))