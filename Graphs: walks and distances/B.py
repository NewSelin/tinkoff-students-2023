from sys import setrecursionlimit

setrecursionlimit(100000)
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i-1].append(j-1)
used, out_ = [False] * n, [False] * n


def dfs(i):
    used[i] = True
    for j in graph[i]:
        if used[j] and not out_[j]:
            return True
        if not used[j]:
            c = dfs(j)
            if c:
                return True
    out_[i] = True
    return False


for i in range(n):
    if not used[i]:
        c = dfs(i)
    if c:
        break
print(1 if c else 0)