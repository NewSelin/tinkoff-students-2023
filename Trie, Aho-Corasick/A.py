s, subs = input(), input()
n = len(subs)
s = subs + "#" + s
pi, ans = [0] * len(s), []
for i in range(1, len(s)):
    k = pi[i-1]
    while True:
        if s[i] == s[k]:
            if k+1 == n:
                ans.append(i-2*n)
            pi[i] = k+1
            break
        if k == 0:
            break
        k = pi[k-1]
print(*ans)