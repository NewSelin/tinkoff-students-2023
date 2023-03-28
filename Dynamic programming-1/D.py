s1, s2 = input(), input()
n, m = len(s1), len(s2)
dp = [list(range(m+1))] + [[j] + [0 for _ in range(1, m+1)] for j in range(1, n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] != s2[j-1]:
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        else:
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1])
        if i >= 2 and j >= 2 and s1[i-2] == s2[j-1] and s1[i-1] == s2[j-2]:
            dp[i][j] = min(dp[i][j], dp[i-2][j-2] + 1)
print(dp[n][m])
