m, n = map(int, input().split())
dp = [[0 for _ in range(n)] for _ in range(m)]
dp[0][n-1] = 2
minus = [(0, n-1)]
s = set()
def f():
    l, k = minus.pop()
    for i in range(l, m):
        for j in range(k, -1, -1):
            if i==l and j==k:
                pass
            elif i==l or j==k or i-l==k-j:
                dp[i][j] = 1

while dp[m-1][0] == 0:
    while minus:
        f()
    for i in range(m):
        j = n-1
        while j>=0 and dp[i][j]==1:
            j-=1
        if j>=0 and all([dp[o][j]==1 for o in range(i)]):
            dp[i][j]=2
            minus.append((i, j))

print(dp[m-1][0])
            
