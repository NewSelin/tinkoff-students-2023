n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]
if n == m == 1:
    print(1)
    print(1, 1)
else:
    maxx = 0
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] != 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            if dp[i][j] >= maxx:
                maxx = dp[i][j]
                ii, jj = i, j
    print(maxx)
    print(ii - maxx + 2, jj - maxx  + 2)
