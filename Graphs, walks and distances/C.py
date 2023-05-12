from collections import deque
n = int(input())
s1, s2 = map(int, input().split())
t1, t2 = map(int, input().split())
def f(v1, v2):
    lst = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i*j != 0 and abs(abs(i) - abs(j)) == 1:
                lst.append((v1 + i, v2 + j))
    return filter(lambda x: 1 <= x[0] <= n and 1 <= x[1] <= n, lst)
dist = [["inf"] * (n+1) for _ in range(n+1)]
dist[s1][s2] = 0
q = deque([(s1, s2)])
matr = [[(None, None)] * (n+1) for _ in range(n+1)]
def bfs():
    while len(q) > 0:
        v1, v2 = q.popleft()
        for u1, u2 in f(v1, v2):
            if (u1, u2) == (t1, t2):
                matr[u1][u2] = (v1, v2)
                return dist[v1][v2] + 1
            if dist[u1][u2] == "inf":
                dist[u1][u2] = dist[v1][v2] + 1
                matr[u1][u2] = (v1, v2)
                q.append((u1, u2))
print(bfs())
lst = [(t1, t2)]
while (s1, s2) != (t1, t2):
    t1, t2 = matr[t1][t2]
    lst.append((t1, t2))
for v1, v2 in lst[::-1]:
    print(v1, v2)


