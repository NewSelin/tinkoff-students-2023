from sys import setrecursionlimit

setrecursionlimit(100000)
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i-1].append(j-1)
    graph[j-1].append(i-1)
used = [False] * n


def dfs(i):
    component.append(i+1)
    used[i] = True
    for j in graph[i]:
        if not used[j]:
            dfs(j)


connect_components = []
for i in range(n):
    if not used[i]:
        component = []
        dfs(i)
        connect_components.append(component)
print(len(connect_components))
for component in connect_components:
    print(len(component))
    print(*sorted(component))