n, m = map(int, input().split())
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1
def f(i, j):
    if 0 <= i <= n-1 and 0 <= j <= m-1:
        if not dp[i][j]:
            dp[i][j] = f(i+1, j-2) + f(i-1, j-2) + f(i-2, j+1) + f(i-2, j-1)
        return dp[i][j]
    return 0
print(f(n-1, m-1))
