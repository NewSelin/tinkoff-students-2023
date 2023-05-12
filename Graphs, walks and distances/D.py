from collections import defaultdict
import heapq
from sys import setrecursionlimit
setrecursionlimit(100000)
k = int(input())
g = defaultdict(list)
for i in range(k):
    g[i].append(((i+1)%k, 1))
    g[i].append(((i*10)%k, 0))
dist = [float("Inf")] * k
dist[1] = 0
q = list(zip(dist, range(k)))
heapq.heapify(q)
while len(q) > 0:
    d, v = heapq.heappop(q)
    for u, w in g[v]:
        if dist[u] > d + w:
            dist[u] = d + w
            heapq.heappush(q, (dist[u], u))
print(dist[0]+1)