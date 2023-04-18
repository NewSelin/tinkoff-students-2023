from sys import setrecursionlimit, stdin
setrecursionlimit(100000)
def f(line):
    n, m = map(int, line.split())
    g = [[] for _ in range(2*n)]
    g_inv = [[] for _ in range(2*n)]
    for _ in range(m):
        u, e_u, v, e_v = map(int, stdin.readline().split())
        g[u + n*int(not e_u)].append(v + n * e_v)
        g[v + n * int(not e_v)].append(u + n * e_u)
        g_inv[v + n * e_v].append(u + n*int(not e_u))
        g_inv[u + n * e_u].append(v + n * int(not e_v))
    topsort = []
    used = [False] * (2*n)
    def dfs(u):
        used[u] = True
        for v in g[u]:
            if not used[v]:
                dfs(v)
        topsort.append(u)
    for u in range(2*n):
        if not used[u]:
            dfs(u)
    topsort = topsort[::-1]
    color = [0] * (2*n)
    def unite(v, c):
        color[v] = c
        for u in g_inv[v]:
            if color[u] == 0:
                unite(u, c)
    c = 1
    for v in topsort:
        if color[v] == 0:
            unite(v, c)
            c += 1
    s = ""
    for i in range(n):
        if color[i] < color[i + n]:
            s += "1"
        else:
            s += "0"
    print(s)
for line in stdin:
    f(line)
